# Variable Lenght Arguments (non key word)

def order_food(min_order, *args):
    global delivery_time
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have oredered: {item}")

        extra_time = max(0, (len(args) - 1) * 5)  # 5 minut za każdy dodatkowy element powyżej 1
        delivery_time = 30 + extra_time
    print(f"Your food will be delivered in {delivery_time} minutes:")
    print("Enjoy the food!")


order_food("Salad", "Pizza", "Carry", "Burger", "Hot Dog", "Soup", "Panini")
