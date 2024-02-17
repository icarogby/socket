import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {address}: {data.decode('utf-8')}")

    print(f"Connection from {address} closed")

def start_server():
    server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server.bind(('2804:25ac:40e:8b00:a13b:e094:9f58:820b', 8888))
    server.listen(5)

    print("Server listening on port 8888...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
