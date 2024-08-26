import random

def vac_feedback(vac, effectiveness):
    print(f"{vac} Vaccine is having {effectiveness} % effectiveness.")
    if (effectiveness > 50) and (effectiveness <= 75):
        print(f"{vac} Seems not so effective, needs more trial.")
    elif (effectiveness > 75) and (effectiveness < 90):
        print(f"{vac}Seems to be effective")
    elif effectiveness > 90:
        print(f"{vac} is very effective.")



def order_food(min_order, *args):
    global delivery_time
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have oredered: {item}")

        extra_time = max(0, (len(args) - 1) * 5)  # 5 minut za każdy dodatkowy element powyżej 1
        delivery_time = 30 + extra_time
    print(f"Your food will be delivered in {delivery_time} minutes:")
    print("Enjoy the food!")

def time_activity(*args, **kwargs):
    """
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random spect on a random activity
    """
    min = sum(args) + random.randint(0, 60)
    #print(min)
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spend {min} minutes for {kwargs[choice]} activity.")

