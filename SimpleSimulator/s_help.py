from define import (registerStored)


def convertToBin(numToCovert, noOfBits):
    if numToCovert == 0:
        return "0" * noOfBits
    ans = ""
    while numToCovert > 1:
        ans = str(numToCovert % 2) + ans
        numToCovert = int(numToCovert / 2)
    ans = "1" + ans
    bitsLeft = noOfBits - len(ans)
    if bitsLeft > 0:
        ans = ("0" * bitsLeft) + ans
    return ans


def convertToDecimal(bin_str):
    """Handles binary number as strings"""
    bin_num = str(bin_str)
    # print(bin_num)
    toRet = 0
    n = len(bin_num)
    for i in range(n):
        if bin_num[n - i - 1] == "1":
            toRet += pow(2, i)
        else:
            continue
    return toRet


def pc_reg_dump(prog_count):
    print(prog_count, end=" ")
    for reg_vals in registerStored.values():
        print(convertToBin(reg_vals, 16), end=" ")
    print()


def memory_dump(mem):
    for m in range(len(mem)):
        print(mem[m])
