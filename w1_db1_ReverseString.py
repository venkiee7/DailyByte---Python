# This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

str1 = input()
# print(str1)

def reverseString(input):
    output = ""
    for char in input:                        #for a in abc -> output = a+"" = a , #for b in abc -> output = ba and so on...
        output = char + output
    return output

    # return(input[::-1])

print(reverseString(str1))