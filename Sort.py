def sort012(arr):
        
    sort = [0] * len(arr)
    n = 0
    
    for i in arr:
        if i == 0:
            sort[n] = i
            n += 1
    
    for i in arr:
        if i == 1:
            sort[n] = i
            n += 1
    
    for i in arr:
        if i == 2:
            sort[n] = i
            n += 1
    
    return sort
    
        # code here
        
arr = [2, 1, 0, 1, 0, 2, 1, 0, 2, 0, 1]

arr = sort012(arr)

for i in arr:
    print(i)