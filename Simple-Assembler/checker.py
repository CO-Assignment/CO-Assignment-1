from definitions import *

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
    pass


def checkD(inst):
    pass


def checkE(inst):
    pass
