# This question is asked by Amazon. Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

sentence1=input()
sentence2=input()

sentence1 = sentence1.split(' ')
sentence1 = list(map(lambda x: str(x), sentence1))
sentence2 = sentence2.split(' ')
sentence2 = list(map(lambda x: str(x), sentence2))

def uncommonWords(s1,s2):
    hash1={}
    hash2={}
    results=[]
    for word in s2:
        if word not in hash1:
            hash1[word] = True

    for word in s1:
        if word not in hash1:
            results.append(word)
        if word not in hash2:
            hash2[word] = True

    for word in s2:
        if word not in hash2:
            results.append(word)

    return results

print(uncommonWords(sentence1, sentence2))