from definitions import *
from helpers import *


def TypeA(inst):
    toRet = ""
    partWise = inst

    toRet += opcodes[partWise[0]]
    toRet += "00"
    if len(partWise) > 3:
        regNo1 = partWise[2]
        regNo2 = partWise[3]
        resultRegNo = partWise[1]
        if (
            (regNo1 not in registerStored)
            or (regNo2 not in registerStored)
            or (resultRegNo not in registerStored)
        ):
            raise Exception("Invalid register provided")
        if "FLAGS" in partWise:
            raise Exception("FLAGS register cannot be used for a Type A instruction.")
        toRet += convertToBin(int(resultRegNo[-1:]), 3)
        toRet += convertToBin(int(regNo1[-1:]), 3)
        toRet += convertToBin(int(regNo2[-1:]), 3)
        operand1 = registerStored[regNo1]
        operand2 = registerStored[regNo2]
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
        registerStored[resultRegNo] = result
    else:
        raise Exception("Illegal type A instruction")

    return toRet


def TypeB(value):
    caller = "movI" if (value[0] == "mov") else value[0]

    noToStore = int(value[-1].split("$")[-1])
    recBin = decimalToBinary(noToStore)

    toshift = str(convertToBin(registerStored[value[1]], 8))
    shiftby = "0" * noToStore

    if caller == "movI":
        answer = noToStore

    elif caller == "ls":

        tocrop = toshift + shiftby
        answer = tocrop[-8:]
        answer = convertToDecimal(answer)

    elif caller == "rs":
        tocrop = shiftby + toshift
        answer = tocrop[:8]
        answer = convertToDecimal(answer)

    registerStored[value[1]] = answer

    recBin = [str(x) for x in str(recBin)]

    finalBin = ["0" * (8 - len(recBin))]
    finalBin += recBin
    immBinary = ""
    for i in finalBin:
        immBinary += i
    mainBinary = opcodes[caller] + Register[value[1]] + immBinary
    return mainBinary


def checkTypeC(inst):
    if len(inst) == 3 and (
        (inst[1] == flags or inst[1] in Register)
        or (inst[1] == flags or inst[2] in Register)
    ):
        return True
    if len(inst) != 3:
        return False
    if inst[0] in opcodes.keys():
        if inst[1] in Register.keys():
            if inst[2] in Register.keys():
                return True
            else:
                raise Exception(inst[2] + " is not a valid register")
        else:
            raise Exception(inst[1] + "is not  valid register")
    else:
        raise Exception(inst[0] + "is not a valid opcode")

    return False


def TypeC(inst):

    if inst[0] == "mov":
        registerStored[inst[1]] = registerStored[inst[2]]
        return (
            opcodes[inst[0] + "R"] + ("0" * 5) + Register[inst[1]] + Register[inst[2]]
        )

    elif inst[0] == "cmp":
        reg1 = registerStored[inst[1]]
        reg2 = registerStored[inst[2]]
        if reg1 > reg2:
            flags[-2] = True
        elif reg2 > reg1:
            flags[-3] = True
        else:
            flags[-1] = True
    elif inst[0] == "div":
        quotient = (registerStored[inst[0]]) // (registerStored[inst[1]])
        remainder = registerStored[inst[0]] % registerStored[inst[1]]
        registerStored["R0"] = quotient
        registerStored["R1"] = remainder
    elif inst[0] == "not":
        registerStored[inst[2]] = ~registerStored[inst[1]]

    return opcodes[inst[0]] + ("0" * 5) + Register[inst[1]] + Register[inst[2]]


def TypeD(inst):

    # mainBinary = opcodes[value[0]] + Register[value[1]] + variables.get(value[-1])
    if inst[1] == "FLAGS":
        raise Exception("ld and st are invalid commands for the FLAGS register.")
    if inst[0] == "ld":
        registerStored[inst[1]] = variablesStored[inst[2]]

    if inst[0] == "st":
        variablesStored[inst[2]] = registerStored[inst[1]]
    return (
        opcodes[inst[0]] + Register[inst[1]] + convertToBin(int(variables[inst[2]]), 8)
    )


def TypeE(inst, flagsC):
    toRet = ""
    lineToJump = -1
    toRet += opcodes[inst[0]]
    toRet += "0" * 3

    if inst[1] not in labels.keys():
        raise Exception("Illegal label specified")

    if inst[0] == "je":
        if flagsC[-1]:
            lineToJump = labels[inst[1]] - len(variablesStored)
    elif inst[0] == "jgt":
        if flagsC[-2]:
            lineToJump = labels[inst[1]] - len(variablesStored)
    elif inst[0] == "jlt":
        if flagsC[-3]:
            lineToJump = labels[inst[1]] - len(variablesStored)
    elif inst[0] == "jmp":
        lineToJump = labels[inst[1]] - len(variablesStored)

    toRet += convertToBin(labels[inst[1]] - len(variablesStored), 8)

    return [lineToJump, toRet]
