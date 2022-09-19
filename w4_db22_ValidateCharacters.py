# This question is asked by Google. Given a string only containing the following characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order.


brackets = input()

def validBrackets(brackets):
  hash = {
    "{": "}",
    "(": ")",
    "[": "]"
  }
  stack = []
  for char in brackets:
    if char in hash:
      stack.append(char)

    else:
      if len(stack) and hash[stack[-1]] == char:
        print(len(stack))
        print(hash[stack[-1]])
        stack.pop()
      else:
        return False

  if len(stack) == 0:
    return True
  return False

print(validBrackets(brackets))