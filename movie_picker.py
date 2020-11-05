import random

horror_movies = ["Halloween", "Friday the 13th", "The Shining", "Trick 'r Treat", "Nightmare on Elm Street"]
comedy_movies = ["Monty Python and the Holy Grail", "School of Rock", "The Blues Brothers", "Mean Girls", "Mrs. Doubtfire"]
fantasy_movies = ["Star Wars", "Lord of the Rings", "Harry Potter", "The Chronicles of Narnia", "The Hobbit"]

choose_genre = input("Pick one of the following genres - Horror, Comedy, or Fantasy: ")

def genre():
    if choose_genre == "Horror":
        print(choose_genre + ", " + "oooo spooky!")
        print("You should watch", random.choice(horror_movies) + "!")
    elif choose_genre == "Comedy":
        print("Ahh yes, " + choose_genre + ", " + "get ready for a laugh!")
        print("You should watch", random.choice(comedy_movies) + "!")
    elif choose_genre == "Fantasy":
        print(choose_genre + ". " + "Great choice, time to escape reality!")
        print("You should watch", random.choice(fantasy_movies) + "!")
    else:
        try:
            raise ValueError
        except ValueError:
            print("Please choose from the 3 genres listed.")
genre()

