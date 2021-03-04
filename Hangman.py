try:
    import random
    amtFileWords = 0
    fileWords = open("words.txt", "r+").readlines()
    for line in fileWords:
        amtFileWords = +1
    words = []

    print(title)  # Prints the title variable
    showWord = ""  # Declaration of initial values of variables
    guesses = [" "]
    amtWords = 0
    attempts_remaining = 6
    guessed_letters = []
    guess = ""
    a = ""
    allowed_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Allowed input answers

    if amtFileWords < 1: # If the text file has insufficient values, it will use this default array.
        words = ["CAT", "DOG", "APPLE", "CAR"]
    elif amtFileWords > 0:
        for line in fileWords:
            words.append(line.strip())

    try:
        for word in words:
            amtWords = amtWords + 1
        if amtWords < 1:
            print("Please enter words into the 'words' array.")
    except Exception as e:
        print("Please enter words into the 'words' array.")
        exit()

    word = random.randint(1, amtWords-1)   # Generates a random number to select a word
    word = (words[word])
    wordLength = len(word)
    for i in word:
        if i == " ":
            wordLength = wordLength - 1

    print(str("This is a {} letter word.").format((wordLength))) # I bet you're happy about this :)

    for i in word:
        a = a+i+" "
    for letter in word:
        if letter in guesses:
            showWord = showWord + letter
            if letter == " ":
                wordLength = wordLength-1
        else:
            showWord = showWord + "_"

    while True:  # This is the actual game code.
        if attempts_remaining > 0:
            print("\n"+showWord)
            guess = input("Please enter a letter\n> ").upper()
            if len(guess) > 1:
                input('Your input was greater than one digit, please try again. [PRESS ENTER]')
                guess = ""
            showWord = ""
            if guess not in allowed_values:
                input("Please only use the Alphanumeric alphabet. [PRESS ENTER]")
            else:
                if guess in word:  # Function for writing the found letters
                    showWord = ""
                    guesses.append(guess)
                    for letter in word:
                        if letter in guesses:
                            showWord = showWord + letter
                        else:
                            showWord = showWord + "_"
                else:
                    print('Incorrect guess, '+ str(attempts_remaining - 1)+" guesses remaining.\n\n")
                    attempts_remaining = attempts_remaining - 1
                    showWord = ""
                    guesses.append(guess)
                    for letter in word:
                        if letter in guesses:
                            showWord = showWord + letter
                        else:
                            showWord = showWord + "_"

            if showWord == word:
                print("\nYou WIN!, the answer was: "+word)
                #print(guessed_letters)
                exit()
        else:
            print("You lose, the answer was "+ word.strip())
            exit()
    else:
        "You found my secret message :)"
except Exception as e:
    print(("An error has ocurred: {}").format(e))
