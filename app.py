import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves = json.load(open("./moves.json", encoding="utf8"))
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
while language.lower() != "english" and language.lower() != "japanese" and language.lower() != "chinese" and language.lower() != "french":
    print("Language not found") 
    language = input("Choose a language: ")

"printNames(language.lower())"

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

typeOption = input("Search for type: ")
def typesearch(typeoption):
    typeCount = 0
    print("Types: ")
    for i in range(len(data)):
        if typeoption.capitalize() in data[i]["type"]:
            print(data[i]["name"]["english"])
            typeCount += 1
    if typeCount > 0:
        print(f"Found: {typeCount}")
    elif typeCount == 0:
        print("None found")
typesearch(typeOption)

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
search = input("Search for a pokemon: ")
searchedList = []
def name_search(search):
    foundCount = 0
    for i in range(len(data)):
        if search in data[i]["name"]["english"]:
            print(data[i]["name"]["english"])
            searchedList.append(data[i]["id"])
            foundCount += 1
    if foundCount > 0:
        print(f"Pokemon Found: {foundCount}")
    elif foundCount == 0:
        print("No pokemon found")
        
name_search(search)
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

print("Moves: ")
for i in range(len(searchedList)):
    select = searchedList[i]
    print(f"- Name: {data[select]["name"]["english"]}")
    if data[select]["id"] == moves[select]["id"]:
        print(f"- - {moves[select]["ename"]}")
# use the search to list the moves
