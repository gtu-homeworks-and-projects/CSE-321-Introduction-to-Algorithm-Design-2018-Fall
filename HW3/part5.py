def isMatch(string, pattern):
    map = {}  
    return isMatchRec(string, 0, pattern, 0, map)

def isMatchRec(string, i, pattern, j, map):
    # Base Case
    if (i == len(string) and j == len(pattern)):
        return True
    if (i == len(string) or j == len(pattern)):
        return False

    # Get current pattern character
    c = pattern[j]

    # If the pattern character exists
    if (map.keys().__contains__(c)):
        s = map[c]

        # Then check if we can use it to match str[i...i+s.length()]
        if (i + len(s) > len(string) or not string[i: i + len(s)] == s ):
            return False

        # If it can match, great, continue to match the rest
        return isMatchRec(string, i + len(s), pattern, j + 1, map)

    # pattern character does not exist in the map
    for k in range(i, len(string)):
        # create or update the map
        map[c] = string[i : k + 1]

        # continue to match the rest
        if (isMatchRec(string, k + 1, pattern, j + 1, map)):
            return True
    map.pop(c)
    return False
    
string = "tobeornottobe"
pattern = "ABCDAB"
print("String '", string, "' has pattern", pattern, ":", isMatch(string, pattern))