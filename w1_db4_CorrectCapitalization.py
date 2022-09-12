# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

str1 = input()

def capitalization(input):
    if(input.islower() or input.isupper()):
        return True;
    elif(input[0].isupper() and input[1:].islower()):
        return True;
    else:
        return False;

print(capitalization(str1));