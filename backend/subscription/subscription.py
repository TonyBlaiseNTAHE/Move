#!/usr/bin/python3


"""
subscription module 
"""


class Subscription:
    """subscription class"""
    def __init__(self, subscription_id, user_id, movie_id, start_date, end_date):
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.movie_id = movie_id
        self.start_date = start_date
        self.end_date = end_date