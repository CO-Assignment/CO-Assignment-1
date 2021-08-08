instructions = []
opcodes = {"add":"00000", "sub":"00001", "ld":"00100", "st":"00101", "mul":"00110", "div":"00111", "rs":"01000", "ls":"01001", "xor":"01010", "or":"01011", "and":"01100", "not":"01101", "cmp":"01110", "jmp":"01111", "jlt":"10000", "jgt":"10001", "je":"10010", "hlt":"10011"}
# mov not added due to conlict


r0 = [0]*16
r1 = [0]*16
r2 = [0]*16
r3 = [0]*16
r4 = [0]*16
r5 = [0]*16
r6 = [0]*16
flags = [0]*4

def convertToDecimal(bin_str):
    """Handles binary number as strings"""
    bin_num = str(bin_str)
    print(bin_num)
    toRet = 0
    n = len(bin_num)
    for i in range(n):
        if(bin_num[n-i-1]=="1"):
            toRet += pow(2,i)
        else:
            continue
    return toRet




while True:
    inst = input()
    if(inst==""):
        continue

    instructions.append(inst)
    if inst=="hlt":
        break
    