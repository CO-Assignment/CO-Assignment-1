from definitions import registerStored, Register, variables, labels

# Functions to check (and throw exceptions if needed) whether an instruction provided is valid or not.

def checkA(inst, j):
    if len(inst) != 4:
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
            Type A commands require 3 operands"""
        )

    if (
        (inst[1] not in registerStored)
        or (inst[2] not in registerStored)
        or (inst[3] not in registerStored)
    ):
        raise Exception(
            f"Error in line no {j+1+len(variables)}: Invalid register provided"
        )
    if (inst[1] == "FLAGS") or (inst[2] == "FLAGS") or (inst[3] == "FLAGS"):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             Cannot use type A instruction for FLAG register"""
        )

    return True


def checkB(inst, j):
    if len(inst) != 3:
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             wrong command given for Type B"""
        )
    if (inst[1] in Register.keys()) and ("$" in inst[2]) and (int(inst[2][1:]) < 256):

        if inst[1] != "FLAGS":
            return True
        else:
            raise Exception(
                f"""Error in line no {j+1+len(variables)}:
                 Cannot write to the flag register."""
            )
    if inst[1] not in Register.keys():
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             {inst[1]} not a valid register"""
        )
    else:
        raise Exception(
            f"Error in line no {j+1+len(variables)}: invalid immediate value"
        )


def checkC(inst, j):
    if not (len(inst) == 3):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             wrong command given for Type C"""
        )
    if inst[1] == "FLAGS":
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             You cannot write values into the FLAGS register."""
        )
    if inst[1] in Register.keys() and inst[2] in Register.keys():
        return True
    if not (inst[1] in Register.keys()):
        raise Exception(
            inst[1],
            f"""Error in line no {j+1+len(variables)}:
             not a valid register""",
        )
    if not (inst[2] in Register.keys()):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             {inst[2]} not a valid register"""
        )
    return False


def checkD(inst, j):
    if (
        (inst[1] in Register.keys())
        and (inst[2] in variables.keys())
        and (inst[1] != "FLAGS")
    ):
        return True
    if not (len(inst) == 3):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             wrong command given for Type D"""
        )
    elif (inst[1] == "FLAGS") or not (inst[1] in Register.keys()):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
             {inst[1]} not a valid value for register"""
        )
    elif not (inst[2] in variables.keys()):
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
            {inst[2]} not a  valid variable"""
        )
    return False


def checkE(inst, j):
    if len(inst) != 2:
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
            Type E commands have only 1 operand which is
             the memory address ( {len(inst)-1} ) specified"""
        )
    if inst[1] not in labels.keys():
        if inst[1] in variables.keys():
            raise Exception(
                f"""Error in line no {j+1+len(variables)}:
                 Variable specified instead of label"""
            )
        raise Exception(
            f"""Error in line no {j+1+len(variables)}:
                Label does not exist"""
        )
    return True
