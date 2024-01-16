import socket

UDP_MAX_SIZE = 65535

members = {}

def listen(s: socket.socket):
    while True:
        msg, addr = s.recvfrom(UDP_MAX_SIZE)

        if not msg:
            continue

        decoded_msg = msg.decode('ascii')
        if decoded_msg.startswith('__join'):
            _, nickname = decoded_msg.split(' ', 1)
            members[addr] = nickname
            print(f'{nickname} joined the chat')
            continue

        sender_nickname = members.get(addr, 'Unknown')
        broadcast_msg = f'{sender_nickname}: {decoded_msg}'

        for member_addr, _ in members.items():
            if member_addr == addr:
                continue
            s.sendto(broadcast_msg.encode('ascii'), member_addr)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 3000))
    print('Chat Server is Listening at 127.0.0.1:3000')

    while True:
        listen(s)
