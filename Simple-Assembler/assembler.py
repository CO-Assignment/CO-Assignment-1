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

# r0 = [0]*16
# r1 = [0]*16
# r2 = [0]*16
# r3 = [0]*16
# r4 = [0]*16
# r5 = [0]*16
# r6 = [0]*16

registers = [0]*7
flags = [False]*4
labels = {}
memory = []
for i in range(256):
    memory.append([0,0])

def convertToBin(numToCovert, noOfBits):
    ans = ""
    while numToCovert>1:
        ans = str(numToCovert%2)+ans
        numToCovert = int(numToCovert/2)
    ans = "1"+ans
    bitsLeft = noOfBits - len(ans)
    ans = ("0"*bitsLeft) + ans
    return ans


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
    inst = input().strip()
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
    # print(partWise)
    toRet+=opcodes[partWise[0]]
    toRet +="00"
    if len(partWise)>3:
        regNo1 = int(partWise[2][-1:])
        regNo2 = int(partWise[3][-1:])
        resultRegNo = int(partWise[1][-1])
        toRet+=convertToBin(resultRegNo,3)
        toRet+=convertToBin(regNo1,3)
        toRet+=convertToBin(regNo2,3)
        operand1 = registers[regNo1]
        operand2 = registers[regNo2]
        result = 0

        # OVERFLOW(fr add and mul only) AND ERRORS YET TO BE HANDLED
        if(partWise[0]=="add"):
            result = operand1+operand2
        elif partWise[0]=="sub":
            result = operand1-operand2
            if(result<0):
                result = 0
                flags[0]= True
        elif partWise[0]=="mul":
            result = operand1*operand2
        elif partWise[0]=="xor":
            result = operand1^operand2
        elif partWise[0]=="or":
            result = operand1 | operand2
        elif partWise[0]=="and":
            result = operand1 & operand2
        registers[resultRegNo]=result
    return toRet

for i in instructions:
    curOp = i.split()[0]
    
    if(curOp=="add" or curOp=="sub" or curOp=="mul" or curOp=="xor" or curOp=="or" or curOp=="and"):
        print(TypeA(i))
    elif(curOp=="hlt"):
        print(opcodes[curOp]+("0"*11))
    



#code checked today working perfectly as expected
       