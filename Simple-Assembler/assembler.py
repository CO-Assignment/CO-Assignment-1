from definitions import (
    instructions,
    flags,
    labels,
    variables,
    output,
    opcodes,
    registerStored,
    variablesStored,
)
from typex import TypeA, TypeB, TypeC, TypeD, TypeE
from sys import stdin
from checker import checkA, checkB, checkC, checkD, checkE

varsDone = False
# linecounter = 0
hltReached = False
tempLineNo = 0
for line in stdin:
    tempLineNo += 1
    line = line.strip()
    if hltReached:

        if line != "":
            raise Exception(
                f"""Error in line no {tempLineNo}:
                 hlt should be the last instruction"""
            )
        break

    if len(instructions) == 256:
        raise Exception(
            f"""Error in line no {tempLineNo}: Memory overflow!
             256 lines limit has been reached!"""
        )

    if line == "":
        continue

    if varsDone is False and line[0:3] != "var":
        varsDone = True

    elif varsDone is True and line[0:3] == "var":
        raise Exception(
            f"""Error in line no {tempLineNo}:
             Variables should only be declared in the starting."""
        )
    if "hlt" in str(line):
        if ":" in line:
            lineNo = len(instructions)

            indexToSplit = line.index(":")
            if " " in line[0:indexToSplit]:
                raise Exception(
                    f"""Error in line no {tempLineNo}cannot
                     have space between label name and ":" """
                )
            value23 = line[0:indexToSplit]
            if(value23 in opcodes.keys()
                or (not(value23.replace('_', '').isalnum()))
                or (value23 == "var")
              ):
                raise Exception(f'''Error in line no {tempLineNo}:
                     Improper name declaration for label ''')

            labels[line[0:indexToSplit]] = lineNo
            instructions.append((line[indexToSplit + 1:]).strip())

        elif "hlt" != line:
            raise Exception(f"""Error in line no {tempLineNo}
                            Improper hlt statement """)

        else:
            instructions.append(line)

        hltReached = True
        continue

    if ":" in line:
        lineNo = len(instructions)
        # TODO: #2 this should be len(instructions) - 1
        indexToSplit = line.index(":")
        if " " in line[0:indexToSplit]:
            raise Exception(
                f'''Error in line no {tempLineNo}:
                 cannot have space between label name and ":"'''
            )
        value23 = line[0:indexToSplit]
        if(value23 in opcodes.keys()
            or (not(value23.replace('_', '').isalnum()))
            or (value23 == "var")
        ):
            raise Exception(f'''Error in line no {tempLineNo}:
                 Improper name declaration for label ''')

        labels[line[0:indexToSplit]] = lineNo
        instructions.append((line[indexToSplit + 1:]).strip())
        continue

    instructions.append(line)

if "hlt" not in instructions[-1]:
    raise Exception("Missing or impropper Hlt use")
count = 0
for i in instructions:
    if "var" not in i:
        break
    count += 1
numberOfLines = len(instructions) - count

for i in range(count):
    k = (instructions[i]).split()

    if len(k) != 2:
        raise Exception(
            f"""Error in line {i+1}
         Invalid syntax for variable declaration """
        )

    if ((k[-1] in opcodes.keys()) or
            (not(k[-1].replace('_', '').isalnum())) or
            (k[-1] == "var")
        ):
        # print(k[-1])
        raise Exception(
            f"""Error in line {i+1}
         Improper declaration for variable"""
        )

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
    ) and checkA(i, j):
        output.append(TypeA(i, j))

    # Type B handling
    # handling mov
    elif curOp == "mov":
        if "$" in i[-1] and checkB(i, j):
            output.append(TypeB(i, j))
        elif checkC(i, j):
            output.append(TypeC(i, j))

    # handling rest of TypeB
    elif (curOp == "rs" or curOp == "ls") and checkB(i, j):
        output.append(TypeB(i, j))

    # TypeC handling
    elif (curOp == "div" or curOp == "not" or curOp == "cmp") and checkC(i, j):
        output.append(TypeC(i, j))

    # TypeD handling
    elif (curOp == "ld" or curOp == "st") and checkD(i, j):
        output.append(TypeD(i, j))

    # TypeE handling
    elif (
        (curOp == "jmp") or
        (curOp == "jlt") or
        (curOp == "jgt") or
        (curOp == "je")
    ) and checkE(i, j):
        result = TypeE(i, currFlagState, j)
        if result[0] == -1:
            output.append(result[1])
        else:
            # j = result[0]
            output.append(result[1])
            # continue

    # TypeF handling
    elif curOp == "hlt":
        output.append(opcodes[curOp] + ("0" * 11))

    # Unexpected Values handling
    else:
        raise Exception(
            f"""Unexpected OpCode provided
        at line {j+1+len(variables)}"""
        )

    j += 1

for i in output:
    print(i)
