#Break statement
"""
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data")
        break
print("Out of loop")

#Continue statement
for i in "DevOps":
    if i == "O":
        print('Found my data')
        continue
    print(f'value of i is {i}')
print("Out of loop")

print("")
import random
skills = ["AWS", "Jenkkins", "Unity", "Linux", "Ansilbe"]

random.shuffle(skills)
print(skills)

print("")

LUCKY = random.choice(skills)
print(LUCKY)

for skill in skills :
    print(f"****** TESTING skill {skill}")
    if skill == LUCKY:
        print("###############")
        print(f"{LUCKY} Skill test is succesfull")
        print("###############")
        print("")
        break
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("test failed")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("")

"""

#Break statement
"""
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data")
        break
print("Out of loop")

#Continue statement
for i in "DevOps":
    if i == "O":
        print('Found my data')
        continue
    print(f'value of i is {i}')
print("Out of loop")
"""
print("")
import random
skills = ["AWS", "Jenkkins", "Unity", "Linux", "Ansilbe"]

random.shuffle(skills)
print(skills)

print("")

LUCKY = random.choice(skills)
print(LUCKY)

for skill in skills :
    print(f"****** TESTING skill {skill}")
    if skill == LUCKY:
        print("")
        print("###############")
        print(f"{LUCKY} Skill test is succesfull")
        print("###############")
        print("")
        continue
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("test failed")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("")

