# This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
# Note: you may assume all strings only contain lowercase alphabetical characters.

arr_input = [input(), input(), input(), input()]

def commonPrefix(arr_input):
  checked = list(filter(lambda x: arr_input[0][0] == x[0], arr_input))
  if (len(checked) != len(arr_input)):
    return ""

  minWord = min(arr_input, key=len)
  half = int(len(minWord) / 2) + 1
  minWidth = 0
  while half < minWidth or half > len(minWord):
    checked = list(filter(lambda x: minWord[:half] in x, arr_input))
    if (len(checked) == len(arr_input)):
      half += 1
      minWidth = half
    else:
      half -= 1
  return minWord[:half]
print(commonPrefix(arr_input))