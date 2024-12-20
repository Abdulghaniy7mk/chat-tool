import socket
import threading
import sys
import os  # For clearing the terminal screen
import time

# ANSI escape codes for color styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"

def clear_screen():
    """Function to clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display the chat tool banner."""
    print(f"""{CYAN}
   _____ _           _       _____ _           _
  / ____| |         | |     / ____| |         | |
 | |    | |__   __ _| |_   | |    | |__   __ _| |_
 | |    | '_ \ / _` | __|  | |    | '_ \ / _` | __|
 | |____| | | | (_| | |_   | |____| | | | (_| | |_
  \_____|_| |_|\__,_|\__|   \_____|_| |_|\__,_|\__|
{RESET}""")
    print(f"{CYAN}{BOLD}Welcome to the WAN Chat Tool! by Abdul Ghaniy{RESET}\n")

def receive_messages(client_socket):
    """Function to handle incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"{CYAN}{message}{RESET}\n")  # Added newline after each received mes>
        except:
            print(f"{RED}[ERROR] Connection lost.{RESET}\n")
            client_socket.close()
            sys.exit()

def start_client(server_ip, port, username):
    """Function to connect to the chat server and send/receive messages."""
    try:
        client_socket.connect((server_ip, port))
        print(f"{GREEN}[CONNECTED] Connected to the chat server!{RESET}\n")
        threading.Thread(target=receive_messages, args=(client_socket,)).start()

        while True:
            message = input(f"{YELLOW}{username}: {RESET}")
            if message.lower() == 'exit':
                print(f"{RED}[EXITING] Disconnecting from the chat...{RESET}\n")
                client_socket.close()
                break
            client_socket.send(f"{username}: {message}\n".encode())  # Added newline af>
            print(f"{YELLOW}{username}: {message}{RESET}")  # Show the sent message for>
    except Exception as e:
        print(f"{RED}[ERROR] {e}{RESET}\n")
        client_socket.close()


if __name__ == "__main__":
    clear_screen()  # Clear the terminal screen before starting

    print_banner()

    # Ask user for username before connection
    username = input(f"{GREEN}Enter your username: {RESET}")
    server_ip = input(f"{CYAN}Enter server IP to connect to: {RESET}")
    port = int(input(f"{CYAN}Enter port to connect to: {RESET}"))

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        start_client(server_ip, port, username)
    except Exception as e:
        print(f"{RED}[ERROR] {e}{RESET}\n")

