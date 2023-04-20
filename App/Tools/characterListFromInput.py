def characterListFromInput():
    stringInput = input("Enter the characters of your list : ")
    charactersList = [letter for letter in stringInput]

    return charactersList

print(characterListFromInput())