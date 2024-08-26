
'''
planet1 = "Closest to sun"
print(planet1)

print(planet1[0])
print(planet1[3])
print(planet1[0:3]) #Slicing/ wycinanie konkretnych indekosw
print(planet1[:7]) #[ :liczba] - od poczatku do podanego indeksu ale do tego indeksu a nie wlacznie z tym ideksem
print(planet1[11:]) #tak samo do konca, od ale nie wlacznie (0 to pierwszy idneks)

print(planet1[-1]) #leci od konca
print(planet1[-2]) #itd
print(planet1[-1:-6])



print(planet1[0:3][::-1]) #odwrotna iterracja/odwortne indeksowanie
print(planet1[::-1])

palindrome = "12321"
print(palindrome)
print(palindrome[::-1])

#Slicing tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[3])
print(devops[5])
print(devops[2:4])
print(devops[2:5])

print(devops[2:5][0][5:11]) # [liczymy od 2, z tego ciagu zaczynmy od 1 i wyciagamy znaki od 5 do 11]
print(devops[3:][2][:3]) # [ od 3, drugi wyraz, znaki tego wyrwazu od 1 do 3]
print(devops[3:][2][:3][::-1]) #to samo ale odwrtacamy kolejnosc wyrazow
print(devops[3:][2][:3][-1]) #wyciagamy tylko ostatni znak


#Slciing list /te same dzialania co w tuple
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devops[3])
print(devops[5])
print(devops[2:4])
print(devops[2:5])

print(devops[2:5][0][5:11]) # [liczymy od 2, z tego ciagu zaczynmy od 1 i wyciagamy znaki od 5 do 11]
print(devops[3:][2][:3]) # [ od 3, drugi wyraz, znaki tego wyrwazu od 1 do 3]
print(devops[3:][2][:3][::-1]) #to samo ale odwrtacamy kolejnosc wyrazow
print(devops[3:][2][:3][-1]) #wyciagamy tylko ostatni znak
'''
#Dictionary

skills = {"DevOps": ("AWS", "Jenkins", "Python", "Ansible"), "Development": ["Java", "NodeJS",".net"]}
print(skills)
print(skills["DevOps"][0])
print(skills["DevOps"][0:3])
print(skills["DevOps"][1:3][1][0:4])
print(skills["DevOps"][1:3][1][0:4][::-1])
print(skills["DevOps"][1:3][1][0:4][::-1][2])
print("")
print(skills["Development"][0:2])
print(skills["Development"][0:2][1])
print(skills["Development"][0:2][1][::-1])