def retrieveIntFromUser(userPromptMessage, inputMessage, errorMessage, inputCheckFunc):
    print(userPromptMessage)
    while True:
        integer = input(inputMessage)
        try:
            integer = int(integer)
            if (inputCheckFunc(integer)):
                break
            else: 
                raise ValueError(int)
        except ValueError:
            print(errorMessage)
    return integer

def nimGame():
    chipCount = retrieveIntFromUser("Player 1 decides chip count: ", "Enter chip count: ", "Chip count must be positive integer!!", lambda x: x > 0)
    print("Total chip count:", chipCount)

    whoGoesFirst = retrieveIntFromUser("Player 2 decides who will start: ", "Enter Player Number: ", "Only 1 and 2 is valid player numbers!!", lambda x: x == 1 or x == 2)
    print("Player {x} starts".format(x = whoGoesFirst))
    currentPlayer = whoGoesFirst

    while True:
        chipsToRemove = retrieveIntFromUser("----- Player {x} Turn -----".format(x = currentPlayer), 
        "Enter number of chips to remove: ", 
        "You can only remove 1 or 2 chips at a time!!", 
        lambda x: x == 1 or x == 2)
        chipCount = chipCount - chipsToRemove
        if (chipCount <= 0):
            print("Player {x} wins!!!".format(x = currentPlayer))
            break
        else:
            print("There are {x} chip(s) left!".format(x = chipCount))
            currentPlayer = 1 if currentPlayer == 2 else 2

nimGame()
