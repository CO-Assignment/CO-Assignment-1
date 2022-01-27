
def convertToBin(numToCovert, noOfBits):
    """Helper function to convert a number from base 10 to base 2 with padded zeros if needed"""
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


def decimalToBinary(n):
    """Helper function to convert a number from decimal to binary"""    
    return int(bin(n).replace("0b", ""))


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
