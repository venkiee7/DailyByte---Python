# This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

str1 = input()

def vaccuumCleaner(input):
    x = input.count("L") - input.count("R")
    y = input.count("U") - input.count("D")
    return x==0 and y==0

print(vaccuumCleaner(str1))