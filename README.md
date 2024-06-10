Bitcoin Blockchain Viewer



Were Vincent Ouma

Bitcoin Blockchain Viewer
GUI OUTPUT

![image](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/c96b776b-3a3b-4570-b835-97134a2eba7b)

CONNECT TO Bitcoin Viewer

![image](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/fdac8eac-e8b8-4bf0-9a4c-20ee29c4345e)

![image](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/5201353b-87e0-45fe-82d1-9fd19fe5f028)


 DISCONNECT TO Bitcoin Viewer

![image](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/735e1e22-b996-4250-92ff-942cba7c17e7)



# README: HOW TO RUN THE CODE
## Bitcoin Blockchain Viewer
### Description
This is a Python-based GUI application that connects to the Bitcoin network and displays information about newly mined blocks in real-time. The application is built using the Tkinter library for the GUI and sockets for network communication. The displayed information includes the block version, previous block hash, Merkle root, timestamp, bits, nonce, and number of transactions.
#### a.Features
i.Connect to the Bitcoin network
ii.Display block information in real-time
iii.User-friendly GUI with styled output

#### b.Prerequisites
i.Python 3.6+
ii.Tkinter library (usually included with Python installations)
iii.Network connection to access the Bitcoin nodes

#### c.Installation
Clone the repository
git clone https://github.com/yourusername/bitcoin-blockchain-viewer.git
cd bitcoin-blockchain-viewer
Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install any required dependencies
i.pip install -r requirements.txt
ii.pip install requests
iii.pip install pycrypto
Running the Application

#### d.Activate the virtual environment (if using)
source venv/bin/activate   # On Windows: venv\Scripts\activate
#### e.Run the application
BitCoinBlockChainViwerGUI.py

## Code Overview
The code is organized into a single main class BitcoinViewer that handles the GUI and network operations. Below is a brief decomposition of the program;
### BitcoinViewer Class
#### Attributes
master: The main Tkinter window.
sock: The socket object for network communication.

#### Methods
__init__(self, master): Initializes the GUI elements and configures the main window.
connect_to_node(self): Connects to a Bitcoin node, displays a dummy block, and starts receiving blocks.
disconnect_from_node(self): Disconnects from the Bitcoin node.
receive_blocks(self): Continuously receives and processes blocks from the Bitcoin network.
parse_block(self, payload): Parses the block data from the received payload.
display_block(self, block): Displays the block information in the GUI.
display_dummy_block(self): Displays a dummy block for testing purposes.

### Example Usage
#### Starting the application
When you run the BitCoinBlockChainViwerGUI.py script, a GUI window will open. Click on "Connect to Bitcoin Network" to start receiving block information.

#### Future Enhancements
i.Improve error handling and resilience.
ii.Add more detailed transaction information within blocks.
iii.Enhance GUI with more interactive features.
iv.By following the above instructions, you should be able to run the Bitcoin Blockchain Viewer and see block information in real-time.

### ****THE END****
