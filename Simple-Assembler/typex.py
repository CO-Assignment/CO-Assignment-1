from definitions import *
from helpers import *


def TypeA(inst):
    toRet = ""
    partWise = inst.split()
    # print(partWise)
    toRet += opcodes[partWise[0]]
    toRet += "00"
    if len(partWise) > 3:
        regNo1 = int(partWise[2][-1:])
        regNo2 = int(partWise[3][-1:])
        resultRegNo = int(partWise[1][-1])
        toRet += convertToBin(resultRegNo, 3)
        toRet += convertToBin(regNo1, 3)
        toRet += convertToBin(regNo2, 3)
        operand1 = registers[regNo1]
        operand2 = registers[regNo2]
        result = 0

        # TODO: #4 ERRORS YET TO BE HANDLED
        if partWise[0] == "add":
            result = operand1 + operand2
            resInBin = convertToBin(result, 16)
            if len(resInBin) > 16:
                resInBin = resInBin[-16:]
                flags[0] = True
                result = convertToDecimal(resInBin)

        elif partWise[0] == "sub":
            result = operand1 - operand2
            if result < 0:
                result = 0
                flags[0] = True
        elif partWise[0] == "mul":
            result = operand1 * operand2

            # Handled overflow for multiplication and addition. Tested from my side. You guys also check once.
            resInBin = convertToBin(result, 16)
            if len(resInBin) > 16:
                resInBin = resInBin[-16:]
                flags[0] = True
                result = convertToDecimal(resInBin)

        elif partWise[0] == "xor":
            result = operand1 ^ operand2
        elif partWise[0] == "or":
            result = operand1 | operand2
        elif partWise[0] == "and":
            result = operand1 & operand2
        registers[resultRegNo] = result
    return toRet


def TypeB(value):
    return value  # ['mov', 'R1', '$100']

    


def TypeC(inst):
    pass


def TypeD(inst):
    pass


def TypeE(inst):
    pass
