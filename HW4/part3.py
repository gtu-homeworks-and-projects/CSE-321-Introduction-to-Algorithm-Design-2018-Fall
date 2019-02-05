# Merges two sorted lists into one sorted list
def merge(firstList, secondList):
    mergedList = []
    i, j = 0, 0
    while i < len(firstList) and j < len(secondList):
        if firstList[i] <= secondList[j] :
            mergedList.append(firstList[i])
            i += 1
        else:
            mergedList.append(secondList[j])
            j += 1

    for i in range(i, len(firstList)):
        mergedList.append(firstList[i])
    
    for j in range(j, len(secondList)):
        mergedList.append(secondList[j])

    return mergedList

# Merges given sorted lists (as variable number of parameters) into one sorted list
def mergeMultipleLists(*lists):
    length = len(lists)
    if length == 0:
        return None
    if length == 1:
        return lists[0]

    mid = int(length / 2)
    firstHalf = lists[0: mid]
    secondHalf = lists[mid: length]

    firstHalfMerged = mergeMultipleLists(*firstHalf)
    secondHalfMerged = mergeMultipleLists(*secondHalf)

    return merge(firstHalfMerged, secondHalfMerged)

# Main driver function
def main():
    a = [1, 3, 5, 7, 11]
    b = [2, 4, 6, 9, 10]
    c = [8, 15, 21, 23, 24]
    d = [12, 13, 14, 16, 17]
    e = [18, 19, 20, 22, 25]

    print("Lists to be merged")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print("Merged List", mergeMultipleLists(e, b, c, d, a))

main()