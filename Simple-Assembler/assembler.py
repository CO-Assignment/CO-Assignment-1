from definitions import *
from helpers import *
from typex import *
from sys import stdin


varsDone = False

for line in stdin:
    #print(labels)
    #print(instructions)
    line = line.strip()

    if len(instructions) == 256:
        raise Exception("Memory overflow! 256 lines limit has been reached!")

    if line == "":
        continue

    if varsDone == False and line[0:3] != "var":
        varsDone = True

    elif varsDone == True and line[0:3] == "var":
        raise Exception("Variables should only be declared in the starting.")

    if "hlt" == str(line):
        instructions.append(line)
        break

    if ":" in line:
        lineNo = len(instructions)
        # TODO: #2 this should be len(instructions) - 1
        indexToSplit = line.index(":")
        labels[line[0:indexToSplit]] = lineNo
        instructions.append((line[indexToSplit + 1 :]).strip())
        continue

    # TODO: #7 major error handling left
    # TODO: #8 Make sure that instructions is provided with only correct values and thus all syntax error is reported here only

    instructions.append(line)

    # TODO: #1 Make sure each instruction resets the FLAG variable

count = 0
for i in instructions:
    if "var" not in i:
        break
    count += 1
numberOfLines = len(instructions) - count

for i in range(count):
    k = (instructions[i]).split()
    variables[k[1]] = numberOfLines + i
    variablesStored[k[1]] = 0
# print(variables,variablesStored)
# print(instructions)
realInstructions = instructions[count:]
# print(realInstructions)
for j in range(len(realInstructions)):
    # print(registerStored)
    currFlagState = flags.copy
    flags = [False] * 4

    i = realInstructions[j]
    #print(i)
    i = i.split()
    curOp = i[0]
    #print(curOp)

    # Type A handling
    if (
        curOp == "add"
        or curOp == "sub"
        or curOp == "mul"
        or curOp == "xor"
        or curOp == "or"
        or curOp == "and"
    ):
        print(TypeA(i))

    # Type B handling
    # handling mov
    elif curOp == "mov":
        if "$" in i[-1]:
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
    elif (curOp == "jmp") or (curOp == "jlt") or (curOp == "jgt") or (curOp == "je"):
        result = TypeE(i, currFlagState)
        if result[0] == -1:
            print(result[1])
        else:
            j = result[0]
            print(result[1])

    # TypeF handling
    elif curOp == "hlt":
        print(opcodes[curOp] + ("0" * 11))

    # Unexpected Values handling
    else:
        raise Exception("Unexpected OpCode provided")
