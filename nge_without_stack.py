def printNGE(arr):
    s=[]
    for i in range(0, len(arr), 1):
        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        s.append(next)
    print(s)
arr = [11, 1, 21, 3]
printNGE(arr)