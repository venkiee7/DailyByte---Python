# This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

from operator import le


s=input()

def removeAdjacent(s):
    stack = []
    for char in s:
        if len(stack) and stack[-1] == char:  
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)

print(removeAdjacent(s))
