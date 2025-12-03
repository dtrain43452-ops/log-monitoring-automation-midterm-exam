import socket

HOST = "127.0.0.1"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
        print("[CLIENT] Connected to server!")

        msg = input("Enter message to send: ")
        client.sendall(msg.encode())

        response = client.recv(1024)
        print("[CLIENT] Server responded:", response.decode())

    except ConnectionRefusedError:
        print("[CLIENT] ERROR: Could not connect. Server is not running.")
