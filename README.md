Python README.md

This movie picker will randomly choose a movie suggestion from a pre-defined list as well as give a snack and drink suggestion to go along with the movie! 

Directions:
Run in Python3 console
The program will give you three genres to choose from. Type in one of the genres you would like a movie selection from or choose 'E' to exit.

Project requirements met:
1. Created lists, populated them with several values, retrieved at least one value, and used it in the program.
2. Implemented a Master Loop where the user can repeatedly enter commands including choosing to exit the program.
3. Created and calls at least 3 functions within the program: help() snack_ideas() drink_ideas()

Breakdown of code:
Imported random module so when the user chooses a genre, a random movie suggestion from that genre will be chosen for user to watch.

Created lists pre-populated with movie choices broken down by genre, a snack list and a drink list to give suggestions after the movie is suggested. 

Implemented a Master Loop where a user can type input or choose to exit program.

Inside the Master Loop: 
Used a While Loop and created input variable for user to choose which type of genre they would like to watch. Genre choices include Horror, Comedy, or Drama.

Added "if" statements to print out a saying corresponding with the genre the user chose, as well a randomly generate the movie suggestion. If user does not enter one of the movie genre choices, they will be asked to choose from one of the defined genre choices.

Called the two functions for the snack and drink suggestions to populate.