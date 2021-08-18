from sys import stdin
from s_help import *
from define import *
from s_typeX import *


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


stopCode = False
while(pc<len(memory)):
    if stopCode:
        break
    pc_print = convertToBin(pc,8)
    # converts the program counter to 8 bit binary
    currFlag = registerStored["111"]
    registerStored["111"] = 0
    op = memory[pc][0:5]
    if(opcodes[op] == "hlt"):
        stopCode = True

    if((opcodes[op] == "add") or (opcodes[op] == "sub") or 
    (opcodes[op] == "mul") or (opcodes[op] == "xor") or (opcodes[op] == "or") 
    or (opcodes[op] == "and")):
        sTypeA(memory[pc])

    if((opcodes[op] == "ld") or (opcodes[op] == "st")):
        sTypeD(memory[pc])

    pc_reg_dump(pc_print)

    pc += 1
    

memory_dump(memory)