import socket
import struct
import hashlib
import time
from tkinter import *
from datetime import datetime

class BitcoinViewer:
    def __init__(self, master):
        self.master = master
        master.title("Bitcoin Blockchain Viewer")

        self.label = Label(master, text="Bitcoin Blockchain Viewer")
        self.label.pack()

        self.text_area = Text(master, width=80, height=20)
        self.text_area.pack()

        self.connect_button = Button(master, text="Connect to Bitcoin Network", command=self.connect_to_node)
        self.connect_button.pack()

        self.disconnect_button = Button(master, text="Disconnect", command=self.disconnect_from_node, state=DISABLED)
        self.disconnect_button.pack()

        self.exit_button = Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

        self.sock = None

    def connect_to_node(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('seed.bitcoin.sipa.be', 8333))
            self.connect_button.config(state=DISABLED)
            self.disconnect_button.config(state=NORMAL)
            self.receive_blocks()
        except Exception as e:
            self.text_area.insert(END, f"Error connecting to Bitcoin node: {e}\n")

    def disconnect_from_node(self):
        if self.sock:
            self.sock.close()
            self.text_area.insert(END, "Disconnected from Bitcoin node.\n")
            self.connect_button.config(state=NORMAL)
            self.disconnect_button.config(state=DISABLED)

    def receive_blocks(self):
        while True:
            try:
                magic = self.sock.recv(4)
                if magic != b'\xf9\xbe\xb4\xd9':
                    raise ValueError('Invalid magic number')
                command = self.sock.recv(12).strip(b'\x00')
                length = struct.unpack('<I', self.sock.recv(4))[0]
                checksum = self.sock.recv(4)
                payload = self.sock.recv(length)
                if hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4] != checksum:
                    raise ValueError('Invalid checksum')
                
                if command == b'block':
                    block = self.parse_block(payload)
                    self.display_block(block)
                
                time.sleep(1)  # Wait for a while before receiving the next block
            except Exception as e:
                self.text_area.insert(END, f"Error receiving blocks: {e}\n")
                break

    def parse_block(self, payload):
        block = {}
        block['version'] = struct.unpack('<I', payload[:4])[0]
        block['prev_block'] = payload[4:36]
        block['merkle_root'] = payload[36:68]
        block['timestamp'] = struct.unpack('<I', payload[68:72])[0]
        block['bits'] = struct.unpack('<I', payload[72:76])[0]
        block['nonce'] = struct.unpack('<I', payload[76:80])[0]
        block['tx_count'] = struct.unpack('<B', payload[80:81])[0]
        return block

    def display_block(self, block):
        self.text_area.insert(END, f"Block Version: {block['version']}\n")
        self.text_area.insert(END, f"Previous Block Hash: {block['prev_block'].hex()}\n")
        self.text_area.insert(END, f"Merkle Root: {block['merkle_root'].hex()}\n")
        self.text_area.insert(END, f"Timestamp: {datetime.utcfromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.text_area.insert(END, f"Bits: {block['bits']}\n")
        self.text_area.insert(END, f"Nonce: {block['nonce']}\n")
        self.text_area.insert(END, f"Number of Transactions: {block['tx_count']}\n")
        self.text_area.insert(END, "\n")

def main():
    root = Tk()
    bitcoin_viewer = BitcoinViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
