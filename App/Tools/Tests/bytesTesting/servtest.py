import socket
import pickle


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((socket.gethostname(), 60000))
        s.listen(1)
        print("===SERVER===")
        print("Server Loaded")
        conn, addr = s.accept()
        print("=== SERVER ===")
        print(f"Connected by {addr}")

        header = int.from_bytes(conn.recv(8), "little")
        print("Header Value = ", header)

        data = pickle.loads(conn.recv(header))
        print("Data Value", data)

