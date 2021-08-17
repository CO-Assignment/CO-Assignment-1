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

def sTypeC(i):
    pass

def sTypeD(i):
    pass

def sTypeE(i):
    pass
