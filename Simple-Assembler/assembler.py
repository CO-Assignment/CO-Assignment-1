instructions = []
opcodes = {
    "add":"00000",
    "sub":"00001",
    "movI":"00010",
    "movR":"00011",
    "ld":"00100",
    "st":"00101",
    "mul":"00110",
    "div":"00111",
    "rs":"01000",
    "ls":"01001",
    "xor":"01010",
    "or":"01011",
    "and":"01100",
    "not":"01101",
    "cmp":"01110",
    "jmp":"01111",
    "jlt":"10000",
    "jgt":"10001",
    "je":"10010",
    "hlt":"10011"
    }
# op code checked and are correct

r0 = [0]*16
r1 = [0]*16
r2 = [0]*16
r3 = [0]*16
r4 = [0]*16
r5 = [0]*16
r6 = [0]*16
flags = [0]*4
labels = {}
memory = []
for i in range(256):
    memory.append([0,0])



def convertToDecimal(bin_str):
    """Handles binary number as strings"""
    bin_num = str(bin_str)
    print(bin_num)
    toRet = 0
    n = len(bin_num)
    for i in range(n):
        if(bin_num[n-i-1]=="1"):
            toRet += pow(2,i)
        else:
            continue
    return toRet


varsDone = False

while True:
    # print(instructions)
    # print(labels)
    inst = input()
    if len(instructions)==256:
        raise Exception("Memory overflow! 256 lines limit has been reached!")
    
    if ":" in inst:
        lineNo = len(instructions)
        indexToSplit = inst.index(":")
        labels[inst[0:indexToSplit]]=lineNo
        instructions.append(inst.split(":")[1].strip())
        continue

    if(varsDone==False and inst[0:3]!="var"):
        
        varsDone = True

    if(inst==""):
        continue
    
    if(inst[0:3]=="var" and varsDone==True):
        raise Exception("Variables should only be declared in the starting.")

    instructions.append(inst)
    if inst=="hlt":
        break
    

def TypeA(inst):
    toRet = ""
    partWise = inst.split()
    toRet+=opcodes[partWise[0]]
    return toRet

for i in instructions:
    print(TypeA(i))



#code checked today working perfectly as expected
       