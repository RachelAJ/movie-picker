import random

horror_movies = ["Halloween", "Friday the 13th", "The Shining"]
comedy_movies = ["Monty Python and the Holy Grail", "School of Rock", "The Blues Brothers"]
fantasy_movies = ["Star Wars - A New Hope", "Lord of the Rings", "Harry Potter and the Sorcerer's Stone"]

choose_genre = input("Pick one of the following genres - Horror, Comedy, or Fantasy: ")

def genre():
    if choose_genre == "Horror":
        print(choose_genre + ", " + "oooo spooky!")
        print("You should watch", random.choice(horror_movies))
    elif choose_genre == "Comedy":
        print("Ahh yes, " + choose_genre + ", " + "get ready for a laugh!")
        print("You should watch", random.choice(comedy_movies))
    elif choose_genre == "Fantasy":
        print(choose_genre + ", " + "time to travel to a galaxy far, far away, the Shire, or Hogwarts!")
        print("You should watch", random.choice(fantasy_movies))
    else:
        try:
            raise ValueError
        except ValueError:
            print("Please choose from the 3 genres listed.")
genre()

