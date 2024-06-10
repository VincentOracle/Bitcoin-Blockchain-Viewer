import socket
import struct
import hashlib
import time
from datetime import datetime
import binascii

def connect_to_node(ip, port=8333):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

def send_message(sock, command, payload):
    magic = b'\xf9\xbe\xb4\xd9'  # Mainnet magic number
    command = command.ljust(12, b'\x00')
    length = struct.pack('<I', len(payload))
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    message = magic + command + length + checksum + payload
    sock.sendall(message)

def read_message(sock):
    magic = sock.recv(4)
    if magic != b'\xf9\xbe\xb4\xd9':
        print(f"Received magic number: {magic.hex()}")
        raise ValueError('Invalid magic number')
    command = sock.recv(12).strip(b'\x00')
    length = struct.unpack('<I', sock.recv(4))[0]
    checksum = sock.recv(4)
    payload = sock.recv(length)
    if hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4] != checksum:
        raise ValueError('Invalid checksum')
    return command, payload

def create_version_payload():
    version = struct.pack('<i', 70015)
    services = struct.pack('<Q', 0)
    timestamp = struct.pack('<q', int(time.time()))
    addr_recv = struct.pack('<Q', 0) + socket.inet_aton('0.0.0.0') + struct.pack('>H', 8333)
    addr_from = struct.pack('<Q', 0) + socket.inet_aton('0.0.0.0') + struct.pack('>H', 8333)
    nonce = struct.pack('<Q', 0)
    user_agent_bytes = struct.pack('B', 0)
    start_height = struct.pack('<i', 0)
    relay = struct.pack('B', 0)
    return version + services + timestamp + addr_recv + addr_from + nonce + user_agent_bytes + start_height + relay

def handle_inv(payload):
    count = payload[0]
    inventory = []
    offset = 1
    for _ in range(count):
        inv_type = struct.unpack('<I', payload[offset:offset+4])[0]
        inv_hash = payload[offset+4:offset+36]
        inventory.append((inv_type, inv_hash))
        offset += 36
    return inventory

def request_data(sock, inventory):
    count = struct.pack('B', len(inventory))
    payload = count
    for inv_type, inv_hash in inventory:
        payload += struct.pack('<I', inv_type) + inv_hash
    send_message(sock, b'getdata', payload)

def parse_block(payload):
    block = {}
    block['version'] = struct.unpack('<I', payload[:4])[0]
    block['prev_block'] = payload[4:36]
    block['merkle_root'] = payload[36:68]
    block['timestamp'] = struct.unpack('<I', payload[68:72])[0]
    block['bits'] = struct.unpack('<I', payload[72:76])[0]
    block['nonce'] = struct.unpack('<I', payload[76:80])[0]
    block['tx_count'] = struct.unpack('<B', payload[80:81])[0]
    offset = 81
    block['transactions'] = []
    for _ in range(block['tx_count']):
        tx_len = struct.unpack('<I', payload[offset:offset+4])[0]
        block['transactions'].append(payload[offset:offset+tx_len])
        offset += tx_len
    return block

def display_block(block):
    print(f"Block Version: {block['version']}")
    print(f"Previous Block Hash: {binascii.hexlify(block['prev_block'])}")
    print(f"Merkle Root: {binascii.hexlify(block['merkle_root'])}")
    print(f"Timestamp: {datetime.utcfromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Bits: {block['bits']}")
    print(f"Nonce: {block['nonce']}")
    print(f"Number of Transactions: {block['tx_count']}")
    for tx in block['transactions']:
        print(f"Transaction: {binascii.hexlify(tx)}")

def main():
    # Try connecting to different seed nodes if the issue persists
    seed_nodes = ['seed.bitcoin.sipa.be', 'dnsseed.bluematt.me', 'dnsseed.bitcoin.dashjr.org']
    for seed in seed_nodes:
        try:
            node = connect_to_node(seed)
            break
        except Exception as e:
            print(f"Could not connect to {seed}: {e}")
            continue
    else:
        print("Could not connect to any seed nodes.")
        return

    payload = create_version_payload()
    send_message(node, b'version', payload)
    while True:
        try:
            command, payload = read_message(node)
            if command == b'inv':
                inventory = handle_inv(payload)
                request_data(node, inventory)
            elif command == b'block':
                block = parse_block(payload)
                display_block(block)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
