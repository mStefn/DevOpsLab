## Variable Lenght Arguments with key words
import random


def time_activity(*args, **kwargs):
    """
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random spect on a random activity
    """
    min = sum(args) + random.randint(0, 60)
    #print(min)
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spend {min} minutes for {kwargs[choice]} activity.")

time_activity(10, 20, 30, hobby="Gaming", game="WoW", fun="Gym", work="DevOps")
