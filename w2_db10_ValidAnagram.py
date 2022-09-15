# This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

s = input()
t = input()

def isAnagram(s, t):
  hash = {}           #key value pair
  for letter in s:
    if letter in hash:
      hash[letter] += 1      #hash[key] = value
    else:
      hash[letter] = 1
  for letter in t:
    if letter in hash and hash[letter] > 0:
      hash[letter] -= 1
    else:
      return False
  for letter in s:
    if hash[letter] != 0:
      return False
  return True

print(isAnagram(s, t))