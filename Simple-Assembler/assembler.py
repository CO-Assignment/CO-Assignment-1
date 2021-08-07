instructions = []
while True:
    inst = input()
    if(inst==""):
        continue

    instructions.append(inst)
    if inst=="hlt":
        break
    # if(len(instructions)>256):