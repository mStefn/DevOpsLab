# Defining Function
"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total


output = add(2, 3)
print(output)
print(add(10, 20))



def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)


adder(5, 20)
print(adder(30, 40))




def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x


out = summ([20, 30, 40])
print(out)

"""


# Default

def greetings(MSG):
    print(f"Good {MSG}")
    print("Welcome to the function.")


greetings("Morning")

print("")


def greetings(MSG="Afternoon"):
    print(f"Good {MSG}")
    print("Welcome to the function.")

greetings()
print("")
greetings("Evening")


