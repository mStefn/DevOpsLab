"""
This script will implement our knowledge on conditions and different datatypes.
"""
print("")
print("This IT organization has various skill sets.")
print("Find out your match.")
print("")
print("Enter Capitalised Values:")

Devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Docker", "Ansible", "Kubernetes", "Terraform"]
Development = ("NodeJS", "AngularJS", "Java", ".net", "Python")
cntr_emp1 = {"Name": "Kotex", "Skills": "Blockchain", "Code": 1024}
cntr_emp2 = {"Name": "Maja", "Skills": "GoLang", "Code": 666}

usr_skill = input("Enter your desired skill:")
#print(usr_skill)

# Check in the database if we have this skill

if usr_skill in Devops:
    print(f"We have {usr_skill} in DevOps Team")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print("We have contract employee with this skill.")
else:
    print(f"SKill: {usr_skill} not found")
