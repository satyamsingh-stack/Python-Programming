def nsel(arr, n):
    nselIndex = []
    s = []
    for i in range(0, n):
        while (len(s) != 0 and s[-1][0] <= arr[i]):
            s.pop()
        if len(s) == 0:
            nselIndex.append(-1)
        else:
            nselIndex.append(s[-1][1])
        s.append([arr[i], i])
    print(nselIndex)
    return nselIndex
def nser(arr,n):
    nserIndex = []
    s = []
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and s[-1][0] <= arr[i]):
            s.pop()
        if len(s) == 0:
            nserIndex.append(n)
        else:
            nserIndex.append(s[-1][1])
        s.append([arr[i], i])
    nserIndex.reverse()
    print(nserIndex)
    return nserIndex
def maxAreaHistogram(arr, n):
    nselIndexArray = nsel(arr, n)
    nserIndexArray = nser(arr, n)
    ans = []
    maxArea = 0
    for i in range(n):
        ans.append((nserIndexArray[i] - nselIndexArray[i] - 1) * arr[i])
        if (maxArea < ans[i]):
            maxArea = ans[i]
    return maxArea
if __name__ == '__main__':
    arr = [6, 2, 5, 4, 5, 1, 6]
    ans = maxAreaHistogram(arr, len(arr))
    print(ans)