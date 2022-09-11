# This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

str1=input()

def palindromeCheck(input):
    output=""
    input = input.lower()
    input = input.replace(" ","")
    input = input.replace(",","")
    input = input.replace(":","")
    # input = ''.join(list(filter(lambda x: x.islower(), input)))
    print(input)
    for char in input:
        output=char+output
    
    print(output)

    if(input==output):
        print("True")
    else:
        print("False")

palindromeCheck(str1)