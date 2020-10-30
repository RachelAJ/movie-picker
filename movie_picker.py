import imdb
import random
from bs4 import BeautifulSoup

moviesDB = imdb.IMDb()

# print(dir(moviesDB))

movies = moviesDB.search_movie("Halloween")

genres = ["Horror", "Comedy", "Drama"]

choose_genre = input("Pick one of the following genres - Horror, Comedy, or Drama: ")

for horror in genres:
    if choose_genre == "Horror":
        print(choose_genre + ", " + "oooo spooky!")
        break

for comedy in genres:
    if choose_genre == "Comedy":
        print("Ahh yes, " + choose_genre + ", " + "get ready for a laugh!")
        break

for drama in genres:    
    if choose_genre == "Drama":
        print(choose_genre + ", " + "great choice! Get the tissues ready!")
        break

# if choose_genre == "Horror":
#     print(choose_genre + ", " + "oooo spooky!")
# elif choose_genre == "Comedy":
#     print("Ahh yes, " + choose_genre + ", " + "get ready for a laugh!")
# elif choose_genre == "Drama":
#     print(choose_genre + ", " + "great choice! Get the tissues ready!")
# else:
#     print("Please choose from the 3 genres listed.")


id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
genre = movie['genre']
directors = movie['directors']
cast = movie['cast']

print('Movie Info:')
print(f'{title} - {year}')
print(f'Rating: {rating}')

genre = ', '.join(map(str, genre))
print(f'Genre: {genre}')

direcStr = ''.join(map(str, directors))
print(f'Directors: {direcStr}')

actors = ', '.join(map(str, cast))
print(f'Cast: {actors}')
