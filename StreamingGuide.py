# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 8/15/2023
# Description: Creates three classes representing a system of streaming services and their movies and a service guide
# StreamingGuide has a list of StreamingService objects, and a Streaming Service has a dictionary of Movie objects.

class Movie:
    """
    A Movie class for representing a movie that has a title, genre, director, and year
    """

    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """
        Returns the title of the Movie object
        """
        return self._title

    def get_genre(self):
        """
        Returns the genre of the Movie object
        """
        return self._genre

    def get_director(self):
        """
        Returns the director of the Movie object
        """
        return self._director

    def get_year(self):
        """
        Returns the release year of the Movie object
        """
        return self._year


class StreamingService:
    """
    A Streaming Service class that represents a service provider and the catalog of movies they provide
    """

    def __init__(self, name):
        self._name = name
        # catalog will be the data member which is a dictionary of movie objects
        self._catalog = {}  # This would look like movie_title : movie_object

    def get_name(self):
        """
        returns the name of the Streaming Service object
        """
        return self._name

    def get_catalog(self):
        """
        Returns the catalog of available movies as a dictionary of Movie objects
        """
        return self._catalog

    def add_movie(self, movie_object):
        """
        Takes a Movie object as an argument and adds it to the catalog of the Streaming Service
        """
        # add movie to the collection of movies with the title as the key and object as the value
        self._catalog[movie_object.get_title()] = movie_object
        return  # get out once complete

    def delete_movie(self, movie_title):
        """
        takes a movie title as an argument and if that Movie is in the catalog, removes it.
        """
        # to remove the movie using it's title, we will need to go through the catalog dictionary
        # compare each movie title with the movie title we want to remove
        if movie_title in self._catalog:
            del self._catalog[movie_title]  # if found, removes the movie_object from catalog
            return  # get out once complete


class StreamingGuide:
    """
    A Streaming Guide class that represents a guide for Streaming Service objects
    """

    def __init__(self):
        self._service_list = []

    def add_streaming_service(self, streaming_service_object):
        """
        takes a StreamingService object as an argument and adds it to the Streaming Guide
        """
        self._service_list.append(streaming_service_object)

    def delete_streaming_service(self, streaming_service_name):
        """
        takes the name of a streaming service as an argument and if it's in the list, removes it.
        """
        # to remove the streaming service using name we will need to go through the list of streaming service objects
        for streaming_service_object in self._service_list:
            # compare the name of each streaming service object with the name we want to remove
            if streaming_service_object.get_name() == streaming_service_name:
                # if found, removes the streaming_service_obect from the streaming guide list
                self._service_list.remove(streaming_service_object)
                return  # get out of the method once complete

    def who_streams_this_movie(self, search_title):
        """
        takes a movie title as a parameter and returns either a dictionary showing the title, year, and
        streaming services with the title or the value None (if no services in the streaming guide have the title)
        """
        # Initializes the dictionary for the title, year, and services
        available_services = {'title': search_title, 'year': 0000, 'services': []}
        # Iterates through the streaming services in the service_list
        for streaming_service_object in self._service_list:
            # creates a variable to access the catalog for each streaming service object
            catalog = streaming_service_object.get_catalog()

            for movie_title in catalog:  # Iterates through each key in the streaming service catalog dictionary
                if movie_title == search_title:  # finds keys (movie titles) that match the search title
                    # adds streaming service as the value for the service key
                    available_services['services'].append(streaming_service_object.get_name())
                    # creates a variable to access movie objects (values) in the catalog dictionary
                    movie_object = catalog[search_title]
                    # calls the movie's year and updates the value of the year key
                    available_services['year'] = int(movie_object.get_year())

        if available_services['services'] == []:  # checks if any services had the searched title, returns None if none
            return None
        return available_services
