"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes
    :param number_of_layers: int - amount of layers the lasagna will have
    :return: int - total preparation time for the amount of layers the lasagna has

    Function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. 
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time baking the lasagna
    :param number_of_layers: int - amount of layers the lasagna will have
    :param elapsed_bake_time: int - time the lasagna has been baking
    :return: int - total elapsed time based on the amount of layers plus the elapsed time baking
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time