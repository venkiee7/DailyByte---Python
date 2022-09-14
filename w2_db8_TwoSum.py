# This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

a=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)

k = int(input())

def checkPair(arr,num,key):
    for i in range(0,num-1):
        for j in range(i+1,num):
            if(arr[i]+arr[j] == key):
                return True
    return False    

print(checkPair(a,n,k))