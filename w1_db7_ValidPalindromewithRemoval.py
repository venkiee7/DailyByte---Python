# This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

str1 = input()

def almostPalindrome(input):
  low = 0
  high = len(input) - 1
  skipped = False
  while low < high:
    if input[low] == input[high]:
      low += 1
      high -= 1
    else:
      if skipped:
        return False
      if input[low + 1] == input[high]:
        low += 1
        high -= 1
        skipped = True
      elif input[low] == input[high - 1]:
        low += 1
        high -= 1
        skipped = True
      else:
        return False
  return True

print(almostPalindrome(str1))