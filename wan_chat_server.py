import socket
import threading


def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    client_socket.send("Welcome to the WAN Chat Server!\n".encode())
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[{address}] {message}")
            broadcast(message, client_socket)
        except:
            print(f"[DISCONNECTED] {address} disconnected.")
            clients.remove(client_socket)
            break


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)


def get_server_details(port):
    # Get the IP address of the server
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("\n[SERVER DETAILS]")
    print(f"IP Address: {local_ip}")
    print(f"Port: {port}\n")
    print("Share these details with clients to connect.\n")


def start_server(port):
    server.bind(('0.0.0.0', port))
    server.listen()
    print(f"[SERVER STARTED] Listening on port {port}...")
    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, address)).start()


if __name__ == "__main__":
    print("WAN Chat Server")
    port = int(input("Enter the port to start the server on (1024-65535): "))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clients = []

    # Display server details before starting
    get_server_details(port)

    try:
        start_server(port)
    except Exception as e:
        print(f"[ERROR] {e}")
        server.close()
