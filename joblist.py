# joblist.py
# Updated.

def testPassword(x):
    print(x)

a = "String 1"
b = "String 2"

x = "String 3"
y = "String 4"
print(f"x = {x} and y = {y}")

print("c = {c} and d = {d}".format(c=1, d=2))

jobList = {'John': 'Doctor', 'Jane': 'Engineer', 'Jim': 'Teacher'}

for name, i in jobList.items():
    print(f"{name} is a {i}")

Password = 'SuperSecretAdminPassword'
testPassword(Password)