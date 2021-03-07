from random import choice

places = ["McDonalds", "KFC", "Burger King"]


def pick():
    """Return random fast food place"""
    return choice(places)
