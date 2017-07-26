import socket
import sys

server_addres = ('localhost', 1500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addres)

try:
    while True:
        resp_no_dec = sock.recv(2048).strip()
        try:
            resp = resp_no_dec.decode('utf-8')
        except:
            resp = resp_no_dec
        print(resp)
        msg = input("")
        if msg == 'sair':
            break
        b = bytearray()
        b.extend(map(ord, msg))
        sock.send(b)
finally:
    sock.close()