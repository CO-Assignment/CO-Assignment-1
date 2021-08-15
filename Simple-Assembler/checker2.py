from definitions import registerStored, Register, variables, labels


def checkA2(inst, j):
    if len(inst) != 4:
        return False

    if (
        (inst[1] not in registerStored)
        or (inst[2] not in registerStored)
        or (inst[3] not in registerStored)
    ):
        return False
    if (inst[1] == "FLAGS") or (inst[2] == "FLAGS") or (inst[3] == "FLAGS"):
        return False

    return True


def checkB2(inst, j):
    if len(inst) != 3:
        return False
    if ((inst[1] in Register.keys()) and
            ('$' in inst[2]) and
            (int(inst[2][1:]) < 256)):

        if(inst[1] != 'FLAGS'):
            return True
        else:
            return False
            
    if inst[1] not in Register.keys():
        return False
    else:
        return False


def checkC2(inst, j):
    if not (len(inst) == 3):
        return False
    if(inst[1] == "FLAGS"):
        return False
    if inst[1] in Register.keys() and inst[2] in Register.keys():
        return True
    if not (inst[1] in Register.keys()):
        return False
    if not (inst[2] in Register.keys()):
        return False
    return False


def checkD2(inst, j):
    if (
        (inst[1] in Register.keys())
        and (inst[2] in variables.keys())
        and (inst[1] != "FLAGS")
    ):
        return True
    if not (len(inst) == 3):
        return False
    elif (inst[1] == "FLAGS") or not (inst[1] in Register.keys()):
        return False
    elif not (inst[2] in variables.keys()):
        return False
    return False


def checkE2(inst, j):
    if len(inst) != 2:
        return False
    if inst[1] not in labels.keys():
        if inst[1] in variables.keys():
            return False
        return False
    return True
    
def checkVar(inst):
    if(len(inst) == 2):
        return True
    else:
        return False