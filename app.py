import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def printNames(lang):
    print("Names: ")
    for i in range(len(data)):
        print(" ", data[i]["name"][lang])

# Add a language choice feature and print the pokemons name based on the user input

print("Languages: ")
print(" - English")
print(" - Japanese")
print(" - Chinese")
print(" - French")
language = input("Choose a language: ")
while language.lower() != "english" or "japanese" or "chinese" or "french":
    print("Language not found") 
    language = input("Choose a language: ")


printNames(language.lower())

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

