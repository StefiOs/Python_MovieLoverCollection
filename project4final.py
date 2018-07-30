from pprint import pprint
from collections import defaultdict
import collections

movies = {
    'Mary': {'Big':
         {
         'Watched': 1,
         'Rating': 'G'
         },
          'Superman':
         {
         'Watched': 3,
         'Rating': 'PG'
          },
           'Forrest Gump':
          {
         'Watched': 3,
         'Rating': 'PG-13'
         }
       },
        'Frank': {'Beauty and the Beast':
       {
         'Watched': 1,
         'Rating': 'G'
       },
        'Kung Fu Panda':
       {
        'Watched': 5,
         'Rating': 'G'
       },
       'Cinderella':
      {
        'Watched': 1,
        'Rating': 'G'
        }
     }
}
print("Welcome to the Movie Lover's Club")
while True:
        print('')
        print("1. Display all members.")
        print("2. Display all movie information for a member.")
        print("3. Increment the times a specific movie was watched by a member.")
        print("4. Add a movie for a member.")
        print("5. Add a new member")
        print("Q. Quit")
        print('')

        def getUserSelection(prompt, validChoices):

                while True:
                    selection = input(prompt).strip()
                    if selection in validChoices:
                        return selection
                    else:
                        print("Invalid choice, try again.")

        userSelection = getUserSelection("Please enter a selection: ", ['1', '2', '3', '4', '5', 'Q', 'q'])


        def optionOne():
            print('Club Members')
            print('==================')
            for key in movies:
                print(key)
                
        def optiontwo():
            print(' Movie                   Rating  Watched ')
            print('=========================================')
            print(' ')
            if memberselection in movies:
                    for movie in movies[memberselection]:
                            print(movie,  movies[memberselection][movie]["Rating"], movies[memberselection][movie]["Watched"], sep="      ")




        def optionfour():

                  while True:
                        rating = input("Enter the movies rating: ")
                        watched = input("Enter amount of times watched: ")
                        movies[memberselection][movieselectiontwo] = {'Watched': watched, 'Rating': rating}
                        print("Movie has been added")
                        print(" ")
                        break

        def optionfive():
            movies.update({newmember: {'Watched': None}})


        def getMemberSelection(prompt, validChoices):
            while True:
                selection = input(prompt).strip()
                if selection in validChoices:
                    return selection
                else:
                    print("Sorry, member not found.")

        def getMovieSelection(prompt, validChoices):
                selection = input(prompt).strip()
                if selection in movies[memberselection]:
                        return selection
                else:
                        print("Sorry, movie title not found.")
                
        def getMovieSelectionTwo(prompt):
                while True:
                        selection = input(prompt).strip()
                        if selection in movies[memberselection]:
                                print("Sorry that movie already exists.")
                        else:
                                return selection
        def newMember(prompt):
                while True:
                    selection = input(prompt).strip()
                    if selection in movies:
                        print("Sorry that member already exists.")
                    else:
                        return selection

                
        if userSelection == '1':
            optionOne()

        if userSelection == '2':
            memberselection = getMemberSelection('Please enter the members name: ', movies.keys())
            print('')
            print('Movies for club member:', memberselection)
            optiontwo()

        if userSelection == '3':
            memberselection = getMemberSelection('Please enter the members name: ', movies.keys())
            movieselection = getMovieSelection('Please enter movie name: ', movies.values())
            for movie in movies[memberselection][movieselection]:
                if memberselection in movies:
                    movies[memberselection][movieselection]["Watched"] += 1
                    print("Times watched incremented.")
                
                break 

        if userSelection == '4':
            memberselection = getMemberSelection('Please enter the members name: ', movies.keys())
            movieselectiontwo = getMovieSelectionTwo('Please enter the name of the movie: ')
            optionfour()

        if userSelection == '5':
            while True:
                newmember = newMember("Enter the new member's name: ")
                print("Member added")

                break

            optionfive()


        if (userSelection == 'Q' or userSelection == 'q'):
            print("Thanks for using the Movie Lover's Club applicaiton!")
            break


            















