import socket 
import threading
import time
from constants import PORT
import main

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname('localhost')
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(server.__exit__)
work_client1 =[
    ("site search", 2),
    ("book search", 3)
]
work_client2 =[
    ("images search", 2),
    ("videos search", 1)
]
work_client3 =[
    ("presontation_models search", 1),
    ("presontation_software search", 2)
]

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            conn.send(f"{msg}........".encode(FORMAT))
            if msg == "work_client1" :
                main._Threads(work_client1)
            elif msg =="work_client2":
                main._Threads(work_client2)
            elif msg =="work_client3":
                main._Threads(work_client3)
            if msg == DISCONNECT_MESSAGE:
                connected = False
    conn.close()
        


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


star = time.perf_counter()
print("[STARTING] server is starting...")
start()
