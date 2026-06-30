# Bitcoin Blockchain Viewer

**Real-Time Bitcoin Network Monitor**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/pulls)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Code Structure](#-code-structure)
- [Usage Guide](#-usage-guide)
- [Technical Details](#-technical-details)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🚀 Overview

**Bitcoin Blockchain Viewer** is a Python-based GUI application that connects directly to the Bitcoin network and displays real-time information about newly mined blocks. Built with **Tkinter** for the graphical interface and **socket programming** for network communication, this tool provides an intuitive window into the Bitcoin blockchain.

The application parses and displays critical block data including:
- **Block Version** – Protocol version indicator
- **Previous Block Hash** – Link to the previous block in the chain
- **Merkle Root** – Cryptographic hash of all transactions in the block
- **Timestamp** – Block creation time (Unix epoch)
- **Bits** – Difficulty target for mining
- **Nonce** – Random number used in mining
- **Transaction Count** – Number of transactions included

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Real-Time Monitoring** | Live display of newly mined blocks as they are added to the blockchain |
| **User-Friendly GUI** | Clean, styled interface with color-coded information |
| **Connect/Disconnect** | Simple toggle to start or stop receiving block data |
| **Dummy Block Test** | Built-in test mode to demonstrate functionality without network connection |
| **Scrollable History** | View historical blocks with auto-scrolling output |
| **Lightweight** | Minimal dependencies, runs on any system with Python 3.6+ |

---

## 📸 Screenshots

### Main Interface
![Bitcoin Blockchain Viewer Main Interface](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/c96b776b-3a3b-4570-b835-97134a2eba7b)

*Application startup screen with connect/disconnect controls*

---

### Connected to Bitcoin Network
![Connected to Bitcoin Network](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/fdac8eac-e8b8-4bf0-9a4c-20ee29c4345e)

*Real-time block information displayed with styled formatting*

---

### Block Data Display
![Block Data Display](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/5201353b-87e0-45fe-82d1-9fd19fe5f028)

*Detailed block information including version, hash, Merkle root, timestamp, bits, nonce, and transaction count*

---

### Disconnected State
![Disconnected from Network](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/assets/104081669/735e1e22-b996-4250-92ff-942cba7c17e7)

*Application state when disconnected from the Bitcoin network*

---

## 🏗️ Architecture

The application follows a **single-class MVC-like architecture** where the `BitcoinViewer` class manages both the GUI and network operations.

```
┌─────────────────────────────────────────────────────────────┐
│                    Bitcoin Blockchain Viewer                 │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                   BitcoinViewer Class                    │ │
│  ├─────────────────────────────────────────────────────────┤ │
│  │  • __init__()         - Initialize GUI & window        │ │
│  │  • connect_to_node()  - Establish network connection   │ │
│  │  • disconnect_from_node() - Close connection           │ │
│  │  • receive_blocks()   - Continuously receive blocks    │ │
│  │  • parse_block()      - Parse block data from payload  │ │
│  │  • display_block()    - Render block in GUI            │ │
│  │  • display_dummy_block() - Show test block             │ │
│  └─────────────────────────────────────────────────────────┘ │
│                          │                                   │
│  ┌───────────────────────▼─────────────────────────────────┐ │
│  │                 Network Layer (Sockets)                  │ │
│  │  • Connects to Bitcoin node via TCP/IP                  │ │
│  │  • Receives raw block data                              │ │
│  └─────────────────────────────────────────────────────────┘ │
│                          │                                   │
│  ┌───────────────────────▼─────────────────────────────────┐ │
│  │                      GUI Layer (Tkinter)                │ │
│  │  • Main window with styled text output                  │ │
│  │  • Connect/Disconnect buttons                           │ │
│  │  • Scrolling text area for block display                │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Prerequisites

- **Python 3.6** or higher
- **Tkinter** library (usually included with Python installations)
- **Active internet connection** to access Bitcoin nodes
- **Basic understanding** of Bitcoin blockchain concepts

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer.git
cd Bitcoin-Blockchain-Viewer
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
# OR individually:
pip install requests
pip install pycrypto
```

### 4. Verify Installation

```bash
python -c "import tkinter; print('Tkinter installed successfully')"
```

---

## 🚀 Running the Application

### Quick Start

```bash
python BitCoinBlockChainViwerGUI.py
```

### Step-by-Step Instructions

1. **Open Terminal/Command Prompt**
   - Navigate to the project directory

2. **Activate Virtual Environment** (if using)
   ```bash
   venv\Scripts\activate    # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Launch Application**
   ```bash
   python BitCoinBlockChainViwerGUI.py
   ```

4. **Use the Application**
   - Click **"Connect to Bitcoin Network"** to start receiving blocks
   - View real-time block information in the display area
   - Click **"Disconnect"** to stop receiving data

---

## 📂 Code Structure

### Directory Layout

```
Bitcoin-Blockchain-Viewer/
│
├── BitCoinBlockChainViwerGUI.py    # Main application file
├── requirements.txt                 # Python dependencies
├── LICENSE                          # MIT License
├── README.md                        # Documentation
└── screenshots/                     # Application screenshots
    ├── main.png
    ├── connected.png
    ├── block-data.png
    └── disconnected.png
```

### Class Breakdown

#### `BitcoinViewer` Class

| Method | Description |
|--------|-------------|
| `__init__(self, master)` | Initializes the GUI elements, configures the main window, sets up buttons and text display area |
| `connect_to_node(self)` | Establishes connection to a Bitcoin node, displays a dummy block for testing, and starts receiving real-time blocks |
| `disconnect_from_node(self)` | Closes the network connection and resets the application state |
| `receive_blocks(self)` | Continuously listens for and processes new blocks from the Bitcoin network using socket communication |
| `parse_block(self, payload)` | Parses raw block data from the received payload, extracting version, hash, Merkle root, timestamp, bits, nonce, and transaction count |
| `display_block(self, block)` | Formats and displays the parsed block information in the GUI with styled colors and organization |
| `display_dummy_block(self)` | Displays a sample block for testing purposes when no network connection is available |

---

## 📖 Usage Guide

### Connecting to the Network

1. Launch the application
2. Click the **"Connect to Bitcoin Network"** button
3. A dummy block will be displayed to confirm functionality
4. The application will begin receiving real-time block data
5. Each new block appears with formatted information

### Understanding the Display

```
┌─────────────────────────────────────────────────────────────┐
│ 🟦 Block #XXXXXX                                           │
│ ─────────────────────────────────────────────────────────── │
│ Version:      0x20000000                                   │
│ Previous Hash: 0000000000000000000...                     │
│ Merkle Root:   4a5e1e...                                   │
│ Timestamp:     2025-01-15 14:32:07                        │
│ Bits:          0x170f2e48                                  │
│ Nonce:         0x1d3c8f2a                                  │
│ Transaction:   2,456 transactions                          │
└─────────────────────────────────────────────────────────────┘
```

### Disconnecting

- Click **"Disconnect"** to stop receiving blocks
- The connection will be gracefully closed
- You can reconnect at any time

---

## 🔬 Technical Details

### Network Communication

The application uses **TCP sockets** to connect to Bitcoin nodes:

```python
# Simplified socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('bitcoin-node-address', 8333))
```

### Data Parsing

Block data is parsed from raw binary payload:

| Field | Bytes | Description |
|-------|-------|-------------|
| Version | 4 | Protocol version |
| Previous Block Hash | 32 | Link to previous block |
| Merkle Root | 32 | Transactions hash root |
| Timestamp | 4 | Unix timestamp |
| Bits | 4 | Difficulty target |
| Nonce | 4 | Mining random number |

### GUI Styling

- **Color-coded** information for better readability
- **Scrollable** text area for block history
- **Responsive** button states (enabled/disabled)
- **Styled fonts** for professional appearance

---

## 🚀 Future Enhancements

| Enhancement | Description | Priority |
|-------------|-------------|----------|
| **Transaction Details** | Display detailed transaction information within blocks | High |
| **Block Explorer** | Click on a block to view full transaction list | High |
| **Error Handling** | Improved resilience and automatic reconnection | Medium |
| **Export Data** | Save block data to CSV or JSON format | Medium |
| **Charts & Analytics** | Visualize network activity trends | Medium |
| **Dark/Light Mode** | Theme toggle for better user experience | Low |
| **Multi-Node Support** | Connect to multiple Bitcoin nodes simultaneously | Low |
| **Mobile App** | Port to mobile platforms using Kivy | Future |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Reporting Issues

- Use the [GitHub Issues](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/issues) tracker
- Provide clear description and steps to reproduce
- Include screenshots if applicable

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Vincent Ouma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---

## 👨‍💻 Author

**Were Vincent Ouma**

[![GitHub](https://img.shields.io/badge/GitHub-VincentOracle-181717?style=flat&logo=github)](https://github.com/VincentOracle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Vincent%20Were-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/vincent-were-4339313a0)
[![Twitter](https://img.shields.io/badge/Twitter-@Vincent_Ouma-1DA1F2?style=flat&logo=twitter)](https://twitter.com)
[![Email](https://img.shields.io/badge/Email-oumawere2001@gmail.com-D14836?style=flat&logo=gmail)](mailto:oumawere2001@gmail.com)

- **Portfolio:** [vincent.eontechsystems.com](https://vincent.eontechsystems.com)
- **GitHub:** [github.com/VincentOracle](https://github.com/VincentOracle)
- **LinkedIn:** [linkedin.com/in/vincent-were-4339313a0](https://linkedin.com/in/vincent-were-4339313a0)

---

## 🙏 Acknowledgments

- Bitcoin community for the open protocol
- Python developers for the excellent libraries
- Open source contributors who make tools like this possible

---

## 📊 Project Status

[![Project Status](https://img.shields.io/badge/Status-Active-success.svg)]()
[![Last Commit](https://img.shields.io/github/last-commit/VincentOracle/Bitcoin-Blockchain-Viewer)](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/commits)
[![Stars](https://img.shields.io/github/stars/VincentOracle/Bitcoin-Blockchain-Viewer)](https://github.com/VincentOracle/Bitcoin-Blockchain-Viewer/stargazers)

---

**⭐ Star this repository** if you found it useful!

---

*Built with ❤️ and Python*
