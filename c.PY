import socket

def start_client():
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(('2804:25ac:40e:8b00:a13b:e094:9f58:820b', 8888))  # Connect to the server on localhost (::1) and port 8888

    while True:
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    start_client()
