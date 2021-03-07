from random import choice

answers = ["Yes!", "No."]


def give():
    """Return random advice"""
    return choice(answers)
