# This question is asked by Amazon. Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

s=input()
t=input()

def hashRemove(s,t):
    stack_s = []
    stack_t = []

    for char in s:
        if char=="#":
            stack_s.pop()
        else:
            stack_s.append(char)
    
    for char in t:
        if char=="#":
            stack_t.pop()
        else:
            stack_t.append(char)

    stack_s = ''.join(stack_s)
    stack_t = ''.join(stack_t)
    print(stack_s)
    print(stack_t)

    
    if(stack_s == stack_t):
        return True
    else:
        return False

print(hashRemove(s,t))