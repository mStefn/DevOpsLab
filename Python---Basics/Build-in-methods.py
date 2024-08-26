# String Build in Methods/Functions
"""
print("")
message = "corona vaccine is ready to use, most of them are more than 90% effective."
print("")
print(message)
print(message.capitalize())
Message = message.capitalize()
print(Message)


# dir() function / Podaje liste funckji pythona ktore mozna uzyc
print(dir([]))
print(dir(()))
print(dir(""))
print(dir({}))


message = "Corona Vaccine is ready to Use, most of them are more than 90% effective."
print(message)
print(message.upper())
print(message.lower())
print(message.islower())



message = "Corona Vaccine is ready to Use, most of them are more than 90% effective."
print(message.find("ready"))
print(message[18:24])
print("")
print(message.find("Maja"))



seq1 = ("192", "162", "40", "90")
print(seq1)
print("")
print(".".join(seq1))
print("")
print("/".join(seq1))
print("")
seq2 = ("13", "28", "16", "8", "55")
print("-".join(seq2))
print("")
print(":".join(seq2))


import random

mountains = ["Everest", "K2", "Giewont", "Sniezka", "Kotex"]
print(mountains)
mountains.append("Maja") # rozszerza liste o podana wartosc na koncu
print("")
print(mountains)
mountains.extend(["Gora1", "Gora2", "Gora3"]) # powieksza ( scala ) liste o podnaa liste
print("")
print(mountains)
lucky = random.choices(mountains)
print("")
print(lucky)

print("")
mountains.insert(2, "Gora4") # dodaje podana wartosc na podanym miejscu ( indexie)
print(mountains)

print("")
mountains.pop() # usuwa ostania pozyce z listy

print(mountains)
print("")
mountains.pop(5) # usuwa pozycje z podanego indexu
print(mountains)

"""

first_dictionary = {"Name":"Maciej", "Surname":"Stefanowicz", "Age":33, "Family":["Maja", "Kot"]}
print(first_dictionary)
print(first_dictionary.keys())
print(first_dictionary.values())
print(first_dictionary)
