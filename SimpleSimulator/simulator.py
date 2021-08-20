import matplotlib.pyplot as plt
from sys import stdin
from s_help import *
from define import *
from s_typeX import *

x = []
y = []
for line in stdin:
    line = line.strip()
    if(line == ""):
        continue

    # TODO: remove the below two lines before submission (only for testing)
    if line == "s":
        memory.append("1001100000000000")
        break
    memory.append(line)

while(len(memory) <256 ):
    memory.append(convertToBin(0,16))

cycleNo = 0
stopCode = False
while(pc<len(memory)):
    

    if stopCode:
        break

    x.append(cycleNo)
    y.append(pc)
    cycleNo += 1

    pc_print = convertToBin(pc,8)
    currFlagR = registerStored["111"]
    # registerStored["111"] = 0
    # converts the program counter to 8 bit binary
    currFlagR = registerStored["111"]
    registerStored["111"] = 0
    op = memory[pc][0:5]
    if(opcodes[op] == "hlt"):
        stopCode = True

    if((opcodes[op] == "add") or (opcodes[op] == "sub") or
    (opcodes[op] == "mul") or (opcodes[op] == "xor") or (opcodes[op] == "or")
    or (opcodes[op] == "and")):
        sTypeA(memory[pc])

    elif ((opcodes[op] == "cmp") or (opcodes[op] == "movR") or (opcodes[op] == "div") or (opcodes[op] == "not")):
        sTypeC(memory[pc], currFlagR)

    elif((opcodes[op] == "movI") or (opcodes[op] == "ls") or (opcodes[op] =="rs")):
        sTypeB(memory[pc])


    elif((opcodes[op] == "ld") or (opcodes[op] == "st")):
        cycleNo -= 1
        x.append(cycleNo)
        y.append(pc)
        cycleNo += 1
        sTypeD(memory[pc])

    elif ((opcodes[op] == "jmp") or (opcodes[op] == "jgt") or (opcodes[op] == "jlt")
    or (opcodes[op] == "je")):
        pc = sTypeE(memory[pc], currFlagR, pc)
        pc_reg_dump(pc_print)
        continue


    pc_reg_dump(pc_print)

    pc += 1


memory_dump(memory)

plt.plot(x,y,'o')

#change this path according to your own laptop
plt.savefig('/home/naman/CO-Assignment-1/SimpleSimulator/graph.png')

