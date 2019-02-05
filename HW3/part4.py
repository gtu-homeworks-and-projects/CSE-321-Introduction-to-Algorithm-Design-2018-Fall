def maxCrossingArray(arr, l, m, h):
    summary, leftSum = 0, -10000
    for i in range(m, l-1, -1):
        summary = summary + arr[i]
        leftSum = max(summary, leftSum)
    
    summary, rightSum = 0, -10000
    for i in range(m + 1, h + 1): 
        summary = summary + arr[i]
        rightSum = max(summary, rightSum)
    
    return leftSum + rightSum

def maxSubArraySum(arr, l, h): 
    maxElem = max(arr)
    if (maxElem < 0):
        return maxElem

    if (l == h):
        return arr[l]
  
    m = (l + h) // 2

    maxSoFar = max(maxSubArraySum(arr, l, m), maxSubArraySum(arr, m +1, h), maxCrossingArray(arr, l, m, h))
    return maxSoFar

a = [5, -6, 6, 7, -6, 7, -4, 3]
print("Max Sum of Contigous Subarray of", a, ":", maxSubArraySum(a, 0, len(a) - 1))