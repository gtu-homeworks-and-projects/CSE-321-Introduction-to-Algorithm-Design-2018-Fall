# Finds the same value of index in a List
def findSameValAsIndex(array):
    first = 0
    last = len(array) - 1
    return findSameValAsIndexRec(array, first, last)

def findSameValAsIndexRec(array, first, last):
    midPoint = (first + last) // 2
    if (first > last):
        return False
    if (array[midPoint] == midPoint):
        return True
    elif (array[midPoint] > midPoint):
        return findSameValAsIndexRec(array, first, midPoint - 1)
    else:
        return findSameValAsIndexRec(array, midPoint + 1, last)

mySortedList = [-1, 0, 1, 3, 5]

if (findSameValAsIndex(mySortedList)):
    print(mySortedList, "contains at least one value of which its index is equal to itself.")
else:
    print(mySortedList, "does not contain a value of which its index is equal to itself.")