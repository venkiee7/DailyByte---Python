# This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
# Note: neither binary string will contain leading 0s unless the string itself is 0

input1 = input()
input2 = input()

def binarySum(num1, num2):
    return str(bin(int(num1,2)+int(num2,2)))[2:]
    
print(binarySum(input1,input2))