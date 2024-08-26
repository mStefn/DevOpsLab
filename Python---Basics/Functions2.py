def vac_feedback(vac, effectiveness):
    print(f"{vac} Vaccine is having {effectiveness} % effectiveness.")
    if (effectiveness > 50) and (effectiveness <= 75):
        print(f"{vac} Seems not so effective, needs more trial.")
    elif (effectiveness > 75) and (effectiveness < 90):
        print(f"{vac}Seems to be effective")
    elif effectiveness > 90:
        print(f"{vac} is very effective.")


vac = input("Give name of vaccine: ")
effectiveness = float(input("Insert vaccine effectiveness (in percent): "))

print("")

vac_feedback(vac, effectiveness)
