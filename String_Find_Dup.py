# Find the duplicate characters in a string and return the number of times it occurs

s = "test string"

def find_dup(s):
    di = {}
    for i in s:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    for i in di:
        if di[i]>1:
            print(i,di[i])

find_dup(s)