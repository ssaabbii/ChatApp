import socket
import threading
import os

UDP_MAX_SIZE = 65535

def listen(s: socket.socket):
    while True:
        msg = s.recv(UDP_MAX_SIZE)
        print(f'\n{msg.decode("ascii")}\n{nickname}: ', end='')

def connect(host: str = '127.0.0.1', port: int = 3000):
    global nickname
    nickname = input('Enter your nickname: ')

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    s.send(f'__join {nickname}'.encode('ascii'))

    while True:
        msg = input(f'{nickname}: ')
        s.send(msg.encode('ascii'))

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print('Welcome to the Chat!')
    connect()
