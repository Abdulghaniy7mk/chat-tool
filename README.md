# WAN Chat Tool

The **WAN Chat Tool** is a lightweight chat application that allows multiple users to communicate over a local or wide-area network. This project is beginner-friendly and provides easy setup and usage instructions for various platforms, including **Termux**, **Windows**, and **Linux**.

---

## Features

- **Real-time communication** between clients and server.
- Supports **multiple users** connecting to the same chat server.
- Simple command-line interface with **custom username**.
- **Cross-platform support** for Termux, Windows, and Linux.

---

## Requirements

Before getting started, ensure you have the following installed:

- **Python 3.8+**: Required to run the scripts.
- **Termux** (for Android users) or a terminal for Linux/Windows.
- Internet connection or a local network setup.

---

## Installation

### 1. **Termux**
1. Open Termux and update your packages:
   ```bash
   pkg update && pkg upgrade
   ```
2. Install Python:
   ```bash
   pkg install python
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/Abdulghaniy7mk/chat-tool.git
   ```
4. Navigate to the project directory:
   ```bash
   cd chat-tool
   ```

### 2. **Windows**
1. Install Python from the [official website](https://www.python.org/downloads/) if not already installed.
2. Clone the repository using Git or download the ZIP:
   ```bash
   git clone https://github.com/your-username/chat-tool.git
   ```
3. Open Command Prompt or PowerShell and navigate to the project directory:
   ```bash
   cd path\to\chat-tool
   ```

### 3. **Linux**
1. Open a terminal and update your packages:
   ```bash
   sudo apt update && sudo apt upgrade
   ```
2. Install Python:
   ```bash
   sudo apt install python3
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chat-tool.git
   ```
4. Navigate to the project directory:
   ```bash
   cd chat-tool
   ```

---

## How to Use

### 1. Start the Server
Run the `wan_chat_server.py` script to initialize the chat server. Make sure to choose a **host IP address** and **port** for the server.

```bash
python wan_chat_server.py
```

You’ll see output confirming the server is ready:
```
[SERVER STARTED] Chat server is running on IP: 127.0.0.1, Port: 1025
```

### 2. Connect as a Client
Run the `wan_chat_client.py` script on a different terminal or device to connect to the server.

```bash
python wan_chat_client.py
```

Enter the **server IP** and **port** as prompted, along with your **username**:
```
Enter server IP to connect to: 127.0.0.1
Enter port to connect to: 1025
Enter your username: JohnDoe
```

Once connected, you can start sending messages.

### 3. Chat Commands
- Type your message and press **Enter** to send.
- Type `exit` to disconnect from the chat server.

---

## Detailed Instructions

1. **Run the Server First**
   - The server script must be executed before any client can connect.
   - Ensure the server is running on a device with a stable network connection.

2. **Using the Same Network**
   - Ensure all devices are connected to the same local network for smooth communication.

3. **Accessing Across Networks**
   - If using the WAN (Wide Area Network), ensure the server's IP is accessible externally, and port forwarding is configured on your router.

---

## Example Workflow

1. **Start Server**:
   - On the device hosting the server:
     ```bash
     python wan_chat_server.py
     ```
   - The server starts at `127.0.0.1` (localhost) on port `1025`.

2. **Connect Client**:
   - On the client device:
     ```bash
     python wan_chat_client.py
     ```
   - Input `127.0.0.1` as the server IP and `1025` as the port.

3. **Start Chatting**:
   - Begin sending messages:
     ```
     Alice: Hello, everyone!
     Bob: Hi Alice, how are you?
     ```

---

## Troubleshooting

### Common Issues
1. **"Connection refused"**
   - Ensure the server is running before the client connects.
   - Check if the IP address and port are correct.

2. **"Permission denied" on Termux**
   - Grant storage permissions to Termux:
     ```bash
     termux-setup-storage
     ```

3. **Firewall Blocking**
   - Ensure the port being used is not blocked by a firewall.

---

## Contributing

If you wish to contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Push your changes and create a pull request.

---

## License

This project is licensed under the **MIT License**. Feel free to use and modify it.
