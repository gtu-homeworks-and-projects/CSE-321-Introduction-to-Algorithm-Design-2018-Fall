validPunctuation = {
    ".": True,
    ",": True,
    "!": True,
    ";": True,
    ":": True,
    "?": True,
    "'": True
}

def isStringReconstructable(badString, validWords):
    i = 0
    while i < len(badString):
        j = i + 1
        splittedString = badString[i: j]
        if validPunctuation.__contains__(splittedString):
            i = i + 1
            continue
        while (not validWords.__contains__(splittedString) or validWords[splittedString] != True) and j < len(badString):
            j += 1
            splittedString = badString[i: j]
        else:
            if (not validWords.__contains__(splittedString) or validWords[splittedString] != True):
                return False
            i = j - 1
        i += 1
    return True
    

def main():
    testString = "itwasthebestoftimes..."

    validWordsDict = { 
        "it": True,
        "was": True,
        "the": True,
        "best": True,
        "of": True,
        "times": True,
        "twa": False,
        "asth": False,
    }

    print("String  '", testString, "'  is reconstructable?", isStringReconstructable(testString, validWordsDict))

main()