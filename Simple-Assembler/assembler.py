from definitions import *
from helpers import *
from typex import *

# r0 = [0]*16
# r1 = [0]*16
# r2 = [0]*16
# r3 = [0]*16
# r4 = [0]*16
# r5 = [0]*16
# r6 = [0]*16



labels = {}
memory = []

for i in range(256):
    memory.append([0, 0])

varsDone = False
stopCode = False

while True:

    

    currInput = input().strip()
    print("Input is", currInput)
    
    if stopCode:
        if currInput != None:
            raise Exception(
                "hlt must be used only once and at the end of instruction set"
            )
        else:
            break

    if len(instructions) == 256:
        raise Exception("Memory overflow! 256 lines limit has been reached!")

    if currInput == "":
        continue

    if ":" in currInput:
        lineNo = len(instructions)
        # TODO: #2 this should be len(instructions) - 1
        indexToSplit = currInput.index(":")
        labels[currInput[0:indexToSplit]] = lineNo
        instructions.append((currInput[indexToSplit, -1]).strip())
        continue

    if varsDone == False and currInput[0:3] != "var":
        varsDone = True

    elif varsDone == True and currInput[0:3] == "var":
        raise Exception("Variables should only be declared in the starting.")

    instructions.append(currInput)

    if currInput == "hlt":
        stopCode = True

    # TODO: #1 Make sure each instruction resets the FLAG variable





# TODO: #3 Recheck flag declaration, shouldn't it be like Flag = '0'*12 + 4 flag bits

for j in range(len(instructions)):
    currFlagState = flags.copy
    flags = [False] * 4
    i = instructions[j]
    curOp = i.split()[0]

    # Type A handling
    if (
        curOp == "add" or curOp == "sub" or curOp == "mul"
        or curOp == "xor" or curOp == "or" or curOp == "and"
    ):
        print(TypeA(i))

    # Type B handling
    # handling mov
    elif curOp == "mov":
        if "$" in curOp[-1]:
            print(TypeB(i))
        else:
            print(TypeC(i))

    # handling rest of TypeB
    elif curOp == "rs" or curOp == "ls":
        print(TypeB(i))

    # TypeC handling
    elif curOp == "div" or curOp == "not" or curOp == "cmp":
        print(TypeC(i))

    # TypeD handling
    elif curOp == "ld" or curOp == "st":
        print(TypeD(i))

    # TypeE handling
    elif curOp == "jmp" or curOp == "jlt" or curOp == "jgt" or curOp == "je":
        print(TypeE(i))

    # TypeF handling
    elif curOp == "hlt":
        print(str(opcodes[curOp] + ("0" * 11)))

    # Unexpected Values handling
    else:
        raise Exception("Unexpected OpCode provided")
