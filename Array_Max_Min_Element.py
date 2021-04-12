arr = [1,9,5,10,88,0,101]

def Max_Min(arr):
    current_max = arr[0]
    current_min = arr[1]
    for i in arr:
        if i>current_max:
            current_max = i
        if i<current_min:
            current_min = i
    return [current_max,current_min]


print(Max_Min(arr))


