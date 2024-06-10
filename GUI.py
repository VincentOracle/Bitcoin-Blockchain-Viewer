import socket
import struct
import hashlib
import time
from tkinter import *
from tkinter import scrolledtext
from datetime import datetime

class BitcoinViewer:
    def __init__(self, master):
        self.master = master
        master.title("Bitcoin Blockchain Viewer")

        # Configure the main window
        master.configure(bg="#2c3e50")
        master.geometry("800x600")

        self.label = Label(master, text="Bitcoin Blockchain Viewer", font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, width=90, height=25, bg="#34495e", fg="#ecf0f1", font=("Courier", 10))
        self.text_area.pack(padx=10, pady=10)

        self.button_frame = Frame(master, bg="#2c3e50")
        self.button_frame.pack(pady=10)

        self.connect_button = Button(self.button_frame, text="Connect to Bitcoin Network", command=self.connect_to_node, bg="#1abc9c", fg="#ecf0f1", font=("Helvetica", 12))
        self.connect_button.grid(row=0, column=0, padx=10)

        self.disconnect_button = Button(self.button_frame, text="Disconnect", command=self.disconnect_from_node, state=DISABLED, bg="#e74c3c", fg="#ecf0f1", font=("Helvetica", 12))
        self.disconnect_button.grid(row=0, column=1, padx=10)

        self.exit_button = Button(self.button_frame, text="Exit", command=master.quit, bg="#95a5a6", fg="#ecf0f1", font=("Helvetica", 12))
        self.exit_button.grid(row=0, column=2, padx=10)

        self.sock = None

    def connect_to_node(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('seed.bitcoin.sipa.be', 8333))
            self.text_area.insert(END, "Connected to Bitcoin node.\n", "info")
            self.connect_button.config(state=DISABLED)
            self.disconnect_button.config(state=NORMAL)
            self.receive_blocks()
        except Exception as e:
            self.text_area.insert(END, f"Error connecting to Bitcoin node: {e}\n", "error")

    def disconnect_from_node(self):
        if self.sock:
            self.sock.close()
            self.text_area.insert(END, "Disconnected from Bitcoin node.\n", "info")
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
                self.text_area.insert(END, f"Error receiving blocks: {e}\n", "error")
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
        self.text_area.insert(END, f"Block Version: {block['version']}\n", "block_info")
        self.text_area.insert(END, f"Previous Block Hash: {block['prev_block'].hex()}\n", "block_info")
        self.text_area.insert(END, f"Merkle Root: {block['merkle_root'].hex()}\n", "block_info")
        self.text_area.insert(END, f"Timestamp: {datetime.utcfromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}\n", "block_info")
        self.text_area.insert(END, f"Bits: {block['bits']}\n", "block_info")
        self.text_area.insert(END, f"Nonce: {block['nonce']}\n", "block_info")
        self.text_area.insert(END, f"Number of Transactions: {block['tx_count']}\n\n", "block_info")

        # Tag configurations for text styles
        self.text_area.tag_config('info', foreground='#1abc9c', font=("Helvetica", 10, "bold"))
        self.text_area.tag_config('error', foreground='#e74c3c', font=("Helvetica", 10, "bold"))
        self.text_area.tag_config('block_info', foreground='#ecf0f1', font=("Courier", 10))

def main():
    root = Tk()
    bitcoin_viewer = BitcoinViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
