while True:
    #Gets the users input
    user = input("Enter a word: ")
    #reverses the word 
    rev_user = reversed(user)
    #Checks if the word is palindromic
    if list (user) == list(rev_user):
        print ("This is a palindromic word ")
    else:
        print ("This is not a palindromic word")
