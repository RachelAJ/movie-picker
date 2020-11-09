# Imported random module to populate a random movie from the lists when program runs and genre is chosen.

import random

# Added help function for instructions on how to retrieve a movie suggestion

def help():
    print("Hey there, looking for a movie to watch? Follow these instructions to get some great suggestions!:")
    print("""
Enter one of the following genres you would like a movie suggestion from: 'Horror', 'Comedy', or 'Fantasy'.
Enter 'E' to exit program.
""")

# Added snack suggestion when movie is picked and is called in Master Loop

def snack_ideas():
    print("Snack suggestion:", random.choice(snacks))

# Created pre-populated lists with movies separated into genres to be retrieved when program runs.

horror_movies = ["Halloween", "Friday the 13th", "The Shining", "Trick 'r Treat", "Nightmare on Elm Street"]
comedy_movies = ["Monty Python and the Holy Grail", "School of Rock", "The Blues Brothers", "Mean Girls", "Mrs. Doubtfire"]
fantasy_movies = ["Star Wars", "Lord of the Rings", "Harry Potter", "The Chronicles of Narnia", "The Hobbit"]
snacks = ["Popcorn", "Nachos", "Cookie Dough Bites", "Snowcaps", "a Hot Dog"]

# Beginning of Master Loop

help()
while True:

    choose_genre = input("Enter a genre or exit program: ")
    choose_genre = choose_genre.lower().replace(" ", "")

    if choose_genre == "E".lower().replace(" ", ""):
        break
    elif choose_genre == "Horror".lower().replace(" ", ""):
        print(choose_genre + ", " + "oooo spooky!")
        print("You should watch", random.choice(horror_movies) + "!")
    elif choose_genre == "Comedy".lower().replace(" ", ""):
        print("Ahh yes, " + choose_genre + ", " + "get ready for a laugh!")
        print("You should watch", random.choice(comedy_movies) + "!")
    elif choose_genre == "Fantasy".lower().replace(" ", ""):
        print(choose_genre + ". " + "Great choice, time to escape reality!")
        print("You should watch", random.choice(fantasy_movies) + "!")
    else:
        try:
            raise ValueError
        except ValueError:
            print("Please choose from the 3 genres listed.")

    snack_ideas()
