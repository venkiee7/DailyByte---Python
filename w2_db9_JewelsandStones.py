# This question is asked by Amazon. Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

jewels=input()
stones=input()

def stonesAndJewels(jew,sto):
    count = 0
    for i in range(0,len(jew)):
        for j in range(0,len(sto)):
            if(jew[i]==sto[j]):
                count = count + 1
    return count

print(stonesAndJewels(jewels,stones))