from definitions import registerStored, Register, variables, labels


def checkA(inst):
    if len(inst) != 4:
        raise Exception("Type A commands require 3 operands")

    if (
        (inst[1] not in registerStored)
        or (inst[2] not in registerStored)
        or (inst[3] not in registerStored)
    ):
        raise Exception("Invalid register provided")
    if (inst[1] == "FLAGS") or (inst[2] == "FLAGS") or (inst[3] == "FLAGS"):
        raise Exception("Cannot use type A instruction for FLAG register")

    return True


def checkB(inst):
    if len(inst) != 3:
        raise Exception('wrong command given for Type B')
    if ((inst[1] in Register.keys()) and
            ('$' in inst[2]) and
            (int(inst[2][1:]) < 256)):

        if(inst[1] != 'FLAGS'):
            return True
        else:
            raise Exception("Illegal command")
    if inst[1] not in Register.keys():
        raise Exception(inst[1], "not a valid register")
    else:
        raise Exception('invalid immediate value')


def checkC(inst):
    if not (len(inst) == 3):
        raise Exception("wrong command given for Type C")
    if(inst[1] == "FLAGS"):
        raise Exception("You cannot write values into the FLAGS register.")
    if inst[1] in Register.keys() and inst[2] in Register.keys():
        return True
    if not (inst[1] in Register.keys()):
        raise Exception(inst[1], " not a valid register")
    if not (inst[2] in Register.keys()):
        raise Exception(f"{inst[2]} not a valid register")
    return False


def checkD(inst):
    if (
        (inst[1] in Register.keys())
        and (inst[2] in variables.keys())
        and (inst[1] != "FLAGS")
    ):
        return True
    if not (len(inst) == 3):
        raise Exception("wrong command given for Type D")
    elif (inst[1] == "FLAGS") or not (inst[1] in Register.keys()):
        raise Exception(inst[1], " not a valid value for register")
    elif not (inst[2] in variables.keys()):
        raise Exception(inst[2], " not a  valid variable")
    return False


def checkE(inst):
    if len(inst) != 2:
        raise Exception("""Type E commands have only 1 operand which is
            the memory address (""", len(inst)-1, ") specified")
    if inst[1] not in labels.keys():
        if inst[1] in variables.keys():
            raise Exception("Variable specified instead of label")
        raise Exception("Label does not exist")
    return True
