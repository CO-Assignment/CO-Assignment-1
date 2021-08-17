from sys import stdin
from s_help import *
from define import *
from s_typeX import *

memory = []
for line in stdin:
    line = line.strip()
    if(line == ""):
        continue
    
    # TODO: remove the below two lines before submission (only for testing)
    if line == "s":
        break 
    memory.append(line)

    



while(pc<len(memory)):
    pc_print = convertToBin(pc,8)
    # converts the program counter to 8 bit binary
    currFlag = registerStored["111"]
    registerStored["111"] = 0
    op = memory[pc][0:5]

    if((opcodes[op] == "add") or (opcodes[op] == "sub") or 
    (opcodes[op] == "mul") or (opcodes[op] == "xor") or (opcodes[op] == "or") 
    or (opcodes[op] == "and")):
        sTypeA(memory[pc])

    pc_reg_dump(pc_print)
    pc += 1
    

