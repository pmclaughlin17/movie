# entertainment_center.py
# Fresh Tomatoes project
# Paul McLaughlin
# Feb 21, 2015
# Populates movie data for movies in movie_list.  Accesses data from IMDb

import media
import fresh_tomatoes
from imdb import IMDb  #internet movie database

#
# Initialize an IMDb object
#
movie_db = IMDb()

#
# Initialize array where movie objects will be stored
#
all_movies = []

#
# Create array of movies
# Official trailer is not available in imdb so had to manually enter this.
# Eventually should allow user to input this array
#
movie_list = [
              {'name': 'Lawrence of Arabia', 'trailer': 'https://www.youtube.com/watch?v=zmr1iSG3RTA'},
              {'name': 'Star Wars', 'trailer': 'https://www.youtube.com/watch?v=CcfZk8H7aQo'},
#               {'name': 'Amelie', 'trailer': 'https://www.youtube.com/watch?v=HEFrLnS5sQY'},
#               {'name': 'Patton', 'trailer': 'https://www.youtube.com/watch?v=g-0dTpzNzwo'},
#               {'name': 'Bananas', 'trailer': 'https://www.youtube.com/watch?v=Xyqm-wWnX0A'},
#               {'name': 'Zelig', 'trailer': 'https://www.youtube.com/watch?v=agkCEOHQVgg'},
#               {'name': 'Strange Brew', 'trailer': 'https://www.youtube.com/watch?v=yZCI39NWZ5g'},
#               {'name': 'The Good, the Bad and the Ugly', 'trailer': 'https://www.youtube.com/watch?v=WCN5JJY_wiA'},
#               {'name': 'Monty Python and the Holy Grail', 'trailer': 'https://www.youtube.com/watch?v=urRkGvhXc8w'},
#               {'name': 'Terminator 2', 'trailer': 'https://www.youtube.com/watch?v=eajuMYNYtuY'},
#               {'name': 'Casablanca', 'trailer': 'https://www.youtube.com/watch?v=EJvlGh_FgcI'},
#               {'name': 'Rocky', 'trailer': 'https://www.youtube.com/watch?v=3VUblDwa648'},
#               {'name': 'Ben Hur', 'trailer': 'https://www.youtube.com/watch?v=NR1ZHKw09n8'},
#               {'name': 'Citizen Kane', 'trailer': 'https://www.youtube.com/watch?v=_1A_WUNQlKY'},
              {'name': 'The Razor''s Edge', 'trailer': 'https://www.youtube.com/watch?v=mlbbzB2hgss'}
              ]
            
for movie_item in movie_list:
    print(movie_item['name'])
    #
    # Search imdb for the movie and return a list movie objects that match the movie name
    # The first item in the list is assumed to be the best match which is consistent with testing
    #    
    for media_item in movie_db.search_movie(movie_item['name']):
        #this returns an array of all matching items including movies and tv shows - best match is first
        try:
            if media_item['kind'] == "movie":  #find first movie in the list that matches
                this_movie = movie_db.get_movie((media_item.movieID))
                print(media_item.movieID)
                #create movie object and assign attributes
                all_movies.append(media.Movie(IMDB_id = media_item.movieID,
                                              movie_title = this_movie['title'].encode('utf-8').strip(),  #Need to be able to properly handle unicode characters in title
                                              movie_storyline = this_movie['plot'],
                                              poster_image = this_movie['full-size cover url'],
                                              trailer_youtube = movie_item['trailer']))
                break #leave loop once returns the first movie 
            break #skip back to outside loop
        except:
            pass

# open webpage and populate page with movies
fresh_tomatoes.open_movies_page(all_movies)


