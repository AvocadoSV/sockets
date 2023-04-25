import socket
import threading
import os

HEADER = 64
PORT = 65433
SERVER = socket.gethostbyname(socket.gethostname())  # ip
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"пользователь {addr} подключен")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Сообщение получено".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"ждемс {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"подключено пользовательей  {threading.active_count()-1}")


print("стартуем....")
start()
