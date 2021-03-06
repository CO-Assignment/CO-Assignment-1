from definitions import (
    flags,
    labels,
    variables,
    Register,
    opcodes,
    registerStored,
    variablesStored,
)

from helpers import convertToBin, convertToDecimal


# the following functions are used to process a certain query of a given type as mentioned in the declaration of function.

def TypeA(inst, j):
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
            raise Exception(
                f"""Error in line no {j+1+len(variables)}:
                 Invalid register provided"""
            )
        if "FLAGS" in partWise:
            raise Exception(
                f"""Error in line no {j+1+len(variables)}:
                 FLAGS register cannot be used for a Type A instruction."""
            )
        toRet += convertToBin(int(resultRegNo[-1:]), 3)
        toRet += convertToBin(int(regNo1[-1:]), 3)
        toRet += convertToBin(int(regNo2[-1:]), 3)
        operand1 = registerStored[regNo1]
        operand2 = registerStored[regNo2]
        result = 0

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

            # Handled overflow for multiplication and addition.
            # Tested from my side. You guys also check once.
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
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             Illegal type A instruction"""
        )

    return toRet


def TypeB(value, j):
    caller = "movI" if (value[0] == "mov") else value[0]
    imm = int(value[-1].split("$")[-1])
    if (imm > 255) or (imm < 0):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
            The immediate value has to be in the inclusive range of 0 & 255"""
        )
    recBin = convertToBin(imm, 8)
    toshift = str(convertToBin(registerStored[value[1]], 16))
    shiftby = "0" * imm

    if caller == "movI":
        answer = imm

    elif caller == "ls":
        tocrop = toshift + shiftby
        answer = tocrop[-16:]
        answer = convertToDecimal(answer)

    elif caller == "rs":
        tocrop = shiftby + toshift
        answer = tocrop[:16]
        answer = convertToDecimal(answer)

    registerStored[value[1]] = answer
    mainBinary = opcodes[caller] + Register[value[1]] + recBin
    return mainBinary


def checkTypeC(inst, j):
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
                raise Exception(
                    f"""Error in line no {j+1+len(variables)}:
                     {inst[2]} is not a valid register"""
                )
        else:
            raise Exception(
                f"""Error in line no {j+1+len(variables)}:
                 inst[1] is not  valid register"""
            )
    else:
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             inst[0] is not a valid opcode"""
        )

    return False


def TypeC(inst, j):

    if inst[0] == "mov":    # The following command helps in moving data from one register to another register.
        registerStored[inst[1]] = registerStored[inst[2]]
        return (
            opcodes[inst[0] + "R"] + ("0" * 5) + Register[inst[1]] + Register[inst[2]]
        )

    elif inst[0] == "cmp":  # The following command compares two registers and stores it inside FLAGS register.
        reg1 = registerStored[inst[1]]
        reg2 = registerStored[inst[2]]
        if reg1 > reg2:
            flags[-2] = True
        elif reg2 > reg1:
            flags[-3] = True
        else:
            flags[-1] = True
    elif inst[0] == "div":  # the following command divides the vale of two registers and stores its quotient in R0 and remainder in R1.
        quotient = (registerStored[inst[1]]) // (registerStored[inst[2]])
        remainder = registerStored[inst[1]] % registerStored[inst[2]]
        registerStored["R0"] = quotient
        registerStored["R1"] = remainder
    elif inst[0] == "not":  # The following command inverts the value in a given register.

        noToFlip = convertToBin(registerStored[inst[2]], 16)

        inverting = ""
        for ch in range(len(noToFlip)):
            if noToFlip[ch] == "1":
                inverting = inverting + "0"
            else:
                inverting = inverting + "1"

        flippedNo = convertToDecimal(inverting)

        registerStored[inst[1]] = flippedNo

    return opcodes[inst[0]] + ("0" * 5) + Register[inst[1]] + Register[inst[2]]




def TypeD(inst, j):
    if inst[1] == "FLAGS":
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             ld and st are invalid commands for the FLAGS register."""
        )
    if inst[0] == "ld":
        registerStored[inst[1]] = variablesStored[inst[2]]

    if inst[0] == "st":
        variablesStored[inst[2]] = registerStored[inst[1]]
    return (
        opcodes[inst[0]] + Register[inst[1]] + convertToBin(int(variables[inst[2]]), 8)
    )


def TypeE(inst, flagsC, j):
    toRet = ""
    lineToJump = -1
    toRet += opcodes[inst[0]]
    toRet += "0" * 3

    if inst[1] not in labels.keys():
        raise Exception(
            f"Error in line no {j+1+len(variables)}:Illegal label specified"
        )

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
