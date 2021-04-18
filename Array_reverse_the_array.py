arr = [1,9,5,10,88,0,101]

def rev(arr):
    i = 0
    j = len(arr)-1
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr


print(rev(arr))


