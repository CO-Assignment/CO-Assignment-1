import matplotlib.pyplot as plt
# import random
from sys import stdin
from s_help import (convertToDecimal, convertToBin, pc_reg_dump, memory_dump)
from define import (pc, memory, opcodes, registerStored)
from s_typeX import (sTypeA, sTypeB, sTypeC, sTypeD, sTypeE)

#  The two arrays are used to plot the points on the graph 
x = []
y = []

# Taking input from stdin line by line
for line in stdin:

    # Removing trailing spaces from the input.
    line = line.strip()

    #Ignoring blank lines
    if(line == ""):
        continue

    #Added to break loop in manual testing
    if line == "s":
        memory.append("1001100000000000")
        break
    memory.append(line)

# Adding blank values of 0 to fill up memory space upto 256 lines.
while(len(memory) < 256):
    memory.append(convertToBin(0, 16))

cycleNo = 0

# A check statement which is used to break out of the loop as we reach halt statement.
stopCode = False
while(pc < len(memory)):

    if stopCode:
        break

    x.append(cycleNo)
    y.append(pc)
    cycleNo += 1

    #Converting the program counter value to a 8 bit string which has to be printed after each instruction.
    pc_print = convertToBin(pc, 8)

    # Reading flag register
    currFlagR = registerStored["111"]
    
    currFlagR = registerStored["111"]
    # Resetting the flag register.
    registerStored["111"] = 0

    # Decoding the instruction to get opcode
    op = memory[pc][0:5]

    #Each if statement checks which opcode we recieved and calls appropriate function.
    if(opcodes[op] == "hlt"):
        stopCode = True

    if(
        (opcodes[op] == "add") or
        (opcodes[op] == "sub") or
        (opcodes[op] == "mul") or
        (opcodes[op] == "xor") or
        (opcodes[op] == "or") or
        (opcodes[op] == "and")
    ):
        sTypeA(memory[pc])

    elif (
            (opcodes[op] == "cmp") or
            (opcodes[op] == "movR") or
            (opcodes[op] == "div") or
            (opcodes[op] == "not")
         ):
        sTypeC(memory[pc], currFlagR)

    elif(
            (opcodes[op] == "movI") or
            (opcodes[op] == "ls") or
            (opcodes[op] == "rs")
         ):

        sTypeB(memory[pc])

    elif(
            (opcodes[op] == "ld") or
            (opcodes[op] == "st")):
        cycleNo -= 1
        x.append(cycleNo)
        y.append(convertToDecimal(memory[pc][-8:]))
        cycleNo += 1
        sTypeD(memory[pc])

    elif(
            (opcodes[op] == "jmp") or
            (opcodes[op] == "jgt") or
            (opcodes[op] == "jlt") or
            (opcodes[op] == "je")):
        pc = sTypeE(memory[pc], currFlagR, pc)
        pc_reg_dump(pc_print)
        continue

    pc_reg_dump(pc_print)

    pc += 1

# Prints the memory dump.

memory_dump(memory)

# Plots the graph between cycle nos. and memory locations accessed.

plt.plot(x, y, 'o')
plt.title('Graph showing the memory locations accessed during different cycles')
plt.xlabel('Cycle No')
plt.ylabel('Memory location acessed')
plt.savefig('graph.png')


# Uncomment if you wish to generated separate files for the graphs.

# a = random.randint(1,100000)
# filename = "graph"+str(a)+".png"
# plt.savefig(filename)