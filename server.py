import socket

HOST = "127.0.0.1"  # localhost
PORT = 5050        # port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}...")

    conn, addr = server.accept()
    with conn:
        print(f"[SERVER] Connected to {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                print("[SERVER] Client disconnected.")
                break

            print("[SERVER] Received:", data.decode())

            response = "Message received!"
            conn.sendall(response.encode())
