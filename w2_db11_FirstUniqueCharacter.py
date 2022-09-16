# This question is asked by Microsoft. Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

str1 = input()

def firstUnique(input):
  hash = {}
  min = -1
  for i in range(len(input)):
    if input[i] in hash:
      hash[input[i]] = -1
    else:
      hash[input[i]] = i

  for char in hash.keys():
    print(char) 
    print(hash.keys())
    print(hash.values())
    if hash[char] != -1 and (min == -1 or hash[char] < min):
      print(min)
      print(hash[char])
      min = hash[char]
      print(min)
  return min

print(firstUnique(str1))