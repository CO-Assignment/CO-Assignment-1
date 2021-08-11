def convertToBin(numToCovert, noOfBits):
    ans = ""
    while numToCovert>1:
        ans = str(numToCovert%2)+ans
        numToCovert = int(numToCovert/2)
    ans = "1"+ans
    bitsLeft = noOfBits - len(ans)
    if bitsLeft>0:
        ans = ("0"*bitsLeft) + ans
    return ans

# def decimalToBinary(n):
#     return bin(n).replace("0b", "")



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

# def binaryToDecimal(binary):
     
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     print(decimal) 
