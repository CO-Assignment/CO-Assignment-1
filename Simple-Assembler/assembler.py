from definitions import (instructions, flags, labels, variables, output,
                         opcodes, registerStored, variablesStored)
from typex import TypeA, TypeB, TypeC, TypeD, TypeE
from sys import stdin
from checker import checkA, checkB, checkC, checkD, checkE

varsDone = False
linecounter = 0
hltReached = False
for line in stdin:
    line = line.strip()
    if hltReached:

        if line != '':
            raise Exception("hlt should be the last instruction")
        break

    if linecounter == 256:
        raise Exception("Memory overflow! 256 lines limit has been reached!")

    if line == "":
        continue

    if varsDone is False and line[0:3] != "var":
        varsDone = True

    elif varsDone is True and line[0:3] == "var":
        raise Exception("Variables should only be declared in the starting.")

    if "hlt" in str(line):

        if ":" in line:
            lineNo = len(instructions)

            indexToSplit = line.index(":")
            if(" " in line[0:indexToSplit]):
                raise Exception("""cannot have space 
                between label name and \":\" """)
            labels[line[0:indexToSplit]] = lineNo
            instructions.append((line[indexToSplit + 1:]).strip())
        else:
            instructions.append(line)

        hltReached = True
        continue

    if ":" in line:
        lineNo = len(instructions)
        # TODO: #2 this should be len(instructions) - 1
        indexToSplit = line.index(":")
        if(" " in line[0:indexToSplit]):
            raise Exception("cannot have space between label name and \":\"")
        labels[line[0:indexToSplit]] = lineNo
        instructions.append((line[indexToSplit + 1:]).strip())
        continue

    # TODO: #7 major error handling left
    # TODO: #8 Make sure that instructions is provided with only correct values
    #  and thus all syntax error is reported here only

    instructions.append(line)
    linecounter += 1

    # TODO: #1 Make sure each instruction resets the FLAG variable

count = 0
for i in instructions:
    if "var" not in i:
        break
    count += 1
numberOfLines = len(instructions) - count

for i in range(count):
    k = (instructions[i]).split()
    # TODO: Illegal variable error handling
    # TODO: Viva
    if (len(k) != 2):
        raise Exception("Invalid syntax for variable declaration ")
    variables[k[1]] = numberOfLines + i
    variablesStored[k[1]] = 0

realInstructions = instructions[count:]
j = 0
while j < len(realInstructions):

    currFlagState = flags[::]

    powerInd = -1
    if True in currFlagState:
        powerInd = currFlagState.index(True)
        flags[powerInd] = False
        powerInd = 3 - powerInd

    if powerInd != -1:
        registerStored["FLAGS"] = 2 ** powerInd
    else:
        registerStored["FLAGS"] = 0

    i = realInstructions[j]
    i = i.split()
    curOp = i[0]

    # Type A handling
    if (
        curOp == "add"
        or curOp == "sub"
        or curOp == "mul"
        or curOp == "xor"
        or curOp == "or"
        or curOp == "and"
    ) and checkA(i):
        output.append(TypeA(i))

    # Type B handling
    # handling mov
    elif curOp == "mov":
        if "$" in i[-1] and checkB(i):
            output.append(TypeB(i))
        elif checkC(i):
            output.append(TypeC(i))

    # handling rest of TypeB
    elif ((curOp == "rs" or curOp == "ls") and checkB(i)):
        output.append(TypeB(i))

    # TypeC handling
    elif (curOp == "div" or curOp == "not" or curOp == "cmp") and checkC(i):
        output.append(TypeC(i))

    # TypeD handling
    elif (curOp == "ld" or curOp == "st") and checkD(i):
        output.append(TypeD(i))

    # TypeE handling
    elif ((curOp == "jmp") or (curOp == "jlt") or (curOp == "jgt")
            or (curOp == "je")) and checkE(i):
        result = TypeE(i, currFlagState)
        if result[0] == -1:
            output.append(result[1])
        else:
            # print("old", end = " ")
            # print(j)
            j = result[0]
            print(result[1])
            # print("new", end = " ")
            # print(j)
            continue

    # TypeF handling
    elif curOp == "hlt":
        output.append(opcodes[curOp] + ("0" * 11))

    # Unexpected Values handling
    else:
        raise Exception("Unexpected OpCode provided")

    j += 1

for i in output:
    print(i)
