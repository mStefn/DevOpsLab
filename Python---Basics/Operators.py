#Aritmitic operators
x = 5
y = 3
z = 9

total = x + y
print(total)
print(total * x)
print(total / z)

total = z - y
print(total)

total = x % y
print(total)

total = x ** y
print(total)

# Comparason operators

a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)  # != is not equal
print(out)

# Assignment Operators

c = 0
d = 1
c += d  # c=c+d (same like c++)
print(c)

c -= d
print(c)

#Logical operators
# and  - wszytkie warunki musza byc prawdziwe wtedy zwraca ture, jesli chociaz jeden jest nieprawdziy zwraca false
# or   - prznajmnije jeden warunek musi byc prwadziwy

a = 40
b = 60

x = 2
y = 3

out = (a > b) or (x < y)
print(out)

out = (a > b) and (x < y)
print(out)

out = (a < b) and (x < y)
print(out)

out = not x < y  # neguje warunke, powinno zwroci true, ale przez "not" zwraca false
print(out)

#Membership operators

devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")

ans = "Linux" in devops  # sprawdza czy wyrazenie w "" znajduje sie w liscie albo tuple o podanej nazwie
print(ans)

ans = "Python" in devops
print(ans)

ans = "Kotex" in devops
print(ans)

ans = "Python" not in devops  # odwrotnosc in, sprwadza czy wyrazenie sie nie znajduje
print(ans)

ans = "Kotex" not in devops
print(ans)

#Identity Operators

a = 12
b = 15

result = a is b
print(result)

a = 12
b = 12

result = a is b
print(result)

a = 12
b = 15

result = a is not b
print(result)

a = 12
b = 12

result = a is not b
print(result)
