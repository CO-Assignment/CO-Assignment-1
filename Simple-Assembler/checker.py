from definitions import *
from helpers import *


def checkA(inst):
    if len(inst) != 4:
        raise Exception("Type A commands require 3 operands")

    if (
        (inst[1] not in registerStored)
        or (inst[2] not in registerStored)
        or (inst[3] not in registerStored)
    ):
        raise Exception("Invalid register provided")

    return True


def checkB(inst):
    pass


def checkC(inst):
    if not (len(inst) == 3):
        raise Exception("wrong command given for Type C")
    if inst[1] in Register.keys() and inst[2] in Register.keys():
        return True
    if not (inst[1] in Register.keys()):
        raise Exception(f"{inst[1]} not a valid register")
    if not (inst[2] in Register.keys()):
        raise Exception(f"{inst[2]} not a valid register")
    return False


def checkD(inst):
    if not (len(inst) == 3):
        raise Exception("wrong command given for Type D")
    if (inst[1] == "FLAGS") or not (inst[1] in Register.keys()):
        raise Exception(f"{inst[1]}  not a valid value for register")
    if not (inst[2] in variables.keys()):
        raise Exception(f"{inst[2]} not a  valid variable")


def checkE(inst):
    pass
