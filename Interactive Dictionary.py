# interactive dictionary project
import json

# Opening the dictionary.json file in read mode
fin = open("C:/Users/chant/Desktop/Py4e/dictionary.json", "r")

# Reading the contenets for json file to the cont object
cont = json.load(fin)

# Define functions
# 1) dispwords function displays words that begin with a specific letter
def dispwords():
        letter = input("Enter the letter to display the words with which it begins with:")
        for i in cont:
            if i.startswith(letter): # checks the dictionary file for words that begin with the same letter
                print(i)

# 2) findword function finds a word and displays whether it is in the dictionary or not
def findword():
    word = input("Enter the word to check in the dictionary:").lower()
    found = False
    for i in cont:
        if i == word: # if the word found in the dictionary is the same as the word the user inputted, True
            found == True
    if found == False:
        print("No such word exists in the dictionary.")
    else:
        print("Word is in the dictionary.")

# 3) dispm function displays the meaning of a specific word
def dispm():
    word = input("Enter the word to check the meaning of:").lower()
    found = False
    for key, value in cont.items():
        if key == word: # if there is a key in the dictionary that is equal to the word the user entered
            found == True
            print("{} word has meaning {}".format(key,value))
    if found == False: # if user enters a word that is not in the dictionary file
        print("No such word exists.")

# 4) dispsm function displays word-meaings for the specific word that is there in the meaning.
def dispsm():
    word = input("Enter a word to be searched in the dictionary and to display the meaning of:")
    found = False
    for key, value in cont.items():
        if key == word or word in value: # Need to check the if the word is in the value as well 
            found == True
            print("Word {} - Meaning {}".format(key,value))
    if found == False:
        print("No such word is in the dictionary.")


# 5) searchno function searches words by number of letters
def searchno():
    num = int(input("Enter number of letters of length of the word:"))
    found = False
    for key in cont:
        if len(key) == num:
            print(key)
            found = True
    if found == False:
        print("No words with this specific length.")


# create menu for the main dictionary
while True:
    try: #print function displays commands the user will see when they prompt
        # User can select from six command options 
        print(""" 
        I N T E R A C T I V E  D I C T I O N A R Y
        ==========================================
        1. Display the words that begin with a specific letter.
        2. Find a specific word.
        3. Display the meaning of the specific word.
        4. Display the word-meanings for the specific word that is in the meaning.
        5. Search and display words by the number of letters.
        6. Exit 
              """)
        # Create choice variable
        choice = int(input("Enter your choice of operation (1-6):"))

        # Need to verify which command the user entered
        # Create six if-elif conditional statements for check command user selected

        if choice == 1:
            dispwords()
        elif choice == 2:
            findword()
        elif choice == 3:
            dispm()
        elif choice == 4:
            dispsm() #search the word the user inputed in the json file for that word`
        elif choice == 5:
            searchno()
        elif choice == 6:
            break
        else:
            print("Invalid command! Enter any number between 1 through 6.")
    except:
        print("Invalid input.")

