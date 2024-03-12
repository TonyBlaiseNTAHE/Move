#!/usr/bin/python3


"""
movie module
"""


class Movie:
    """movie class"""
    def __init__(self, movie_id, title, description, release_year):
        self.movie_id = movie_id
        self.title = title
        self.description = description
        self.release_year = release_year
    
    def __repr__(self):
        return f'<Movie {self.title}>'
