from definitions import *
from helpers     import *

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

varsDone = False
stopCode = False

while True:
    # print(instructions)
    # print(labels)
    inst = input().strip()

    if(stopCode):
        if(inst!=None):
            raise Exception("hlt must be used only once and at the end of instruction set")
        else:
            break

    if len(instructions)==256:
        raise Exception("Memory overflow! 256 lines limit has been reached!")
    
    if(inst==""):
        continue

    if ":" in inst:
        lineNo = len(instructions)  
        # TODO: #2 this should be len(instructions) - 1
        indexToSplit = inst.index(":")
        labels[inst[0:indexToSplit]]=lineNo
        instructions.append((inst[indexToSplit,-1]).strip())
        continue

    if(varsDone==False and inst[0:3]!="var"):
        varsDone = True
    
    elif(varsDone==True and inst[0:3]=="var"):
        raise Exception("Variables should only be declared in the starting.")


    instructions.append(inst)

    if inst=="hlt":
        stopCode = True
    

    # TODO: #1 Make sure each instruction resets the FLAG variable

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

        #ERRORS YET TO BE HANDLED
        if(partWise[0]=="add"):
            result = operand1+operand2
            resInBin = convertToBin(result,16)
            if len(resInBin)>16:
                resInBin = resInBin[-16:]
                flags[0]=True
                result = convertToDecimal(resInBin)

        elif partWise[0]=="sub":
            result = operand1-operand2
            if(result<0):
                result = 0
                flags[0]= True
        elif partWise[0]=="mul":
            result = operand1*operand2
            
            # Handled overflow for multiplication and addition. Tested from my side. You guys also check once.
            resInBin = convertToBin(result,16)
            if len(resInBin)>16:
                resInBin = resInBin[-16:]
                flags[0]=True
                result = convertToDecimal(resInBin)

        elif partWise[0]=="xor":
            result = operand1^operand2
        elif partWise[0]=="or":
            result = operand1 | operand2
        elif partWise[0]=="and":
            result = operand1 & operand2
        registers[resultRegNo]=result
    return toRet



def TypeB(inst):
    pass

def TypeC(inst):
    pass

def TypeD(inst):
    pass

def TypeE(inst):
    pass


for j in range(len(instructions)):
    currFlagState = flags.copy
    flags = [False]*4
    i = instructions[j]
    curOp = i.split()[0]
    
    if(curOp=="add" or curOp=="sub" or curOp=="mul" or curOp=="xor" or curOp=="or" or curOp=="and"):
        print(TypeA(i))
    elif (curOp=="ld" or curOp=="st"):
        print(TypeD(i))
    elif(curOp=="hlt"):
        print(opcodes[curOp]+("0"*11))
    



#code checked today working perfectly as expected
       