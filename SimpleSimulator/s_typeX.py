from define import *
from s_help import *



def sTypeA(i):
    opcode = i[0:5]
    dest_reg = i[7:10]
    reg1 = i[10:13]
    reg2 = i[13:]
    op1 = registerStored[reg1]
    op2 = registerStored[reg2]

    if(opcodes[opcode] == "add"):
        result = op1 + op2
        resInBin = convertToBin(result, 16)
        if len(resInBin) > 16:
            resInBin = resInBin[-16:]
            registerStored["111"] = 8
            result = convertToDecimal(resInBin)
               

    elif(opcodes[opcode] == "sub"):
        result = op1 - op2
        if (result < 0):
            result = 0
            registerStored["111"] = 8
       
    elif(opcodes[opcode] == "mul"):
        result = op1 * op2
        resInBin = convertToBin(result, 16)
        if len(resInBin) > 16:
            resInBin = resInBin[-16:]
            registerStored["111"] = 8
            result = convertToDecimal(resInBin)
       
    elif(opcodes[opcode] == "xor"):
        result = op1 ^ op2
       
    elif(opcodes[opcode] == "or"):
        result = op1 | op2
        
    elif(opcodes[opcode] == "and"):
        result = op1 & op2
    registerStored[dest_reg] = result
        
    


def sTypeB(i):
    pass

def sTypeC(i, currFlag):
    opcode = i[0:5]
    reg1 = i[10:13]
    reg2 = i[13:]
    if (opcodes[opcode] == "cmp"):
        val1 = registerStored[reg1]
        val2 = registerStored[reg2]
        if (val1 > val2):
            registerStored["111"] = 2
        elif (val1 < val2):
            registerStored["111"] = 4
        else:
            registerStored["111"] = 1

    elif (opcodes[opcode] == "not"):
        noToFlip = convertToBin(registerStored[reg2], 16)
        
        inverting = ""
        for ch in range(len(noToFlip)):
            if(noToFlip[ch] == "1"):
                inverting = inverting + "0"
            else:
                inverting = inverting + "1"
        
        flippedNo = convertToDecimal(inverting)
        
        registerStored[reg1] = flippedNo

    elif (opcodes[opcode] == "div"):
        quotient = (registerStored[reg1]) // (registerStored[reg2])
        remainder = registerStored[reg1] % registerStored[reg2]
        registerStored["000"] = quotient
        registerStored["001"] = remainder

    elif (opcodes[opcode] == "movR"):
        if(reg2 == "111"):
            registerStored[reg1] = currFlag
            return
        registerStored[reg1] = registerStored[reg2]
def sTypeD(i):
    opcode = i[0:5]
    reg = i[5:8]
    location = convertToDecimal(i[8:])
    valueToStore = registerStored[reg]
    valueToLoad = convertToDecimal(memory[location])


    if(opcodes[opcode] == "st"):
        memory[location] = convertToBin(valueToStore, 16)

    elif (opcodes[opcode] == "ld"):
        registerStored[reg] = valueToLoad
        

def sTypeE(i):
    pass