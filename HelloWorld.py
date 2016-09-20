print ("My First Python Code")

#print ("commented out")


'''
commented out
'''

#assignment

a = 0
b = 3
print(a + b)

#assignmennt, strings
c = "0"
d = "3"
print(c + d)

#casting int as c
print(int(c) + b)

#conditionals

if a >= 1:
    print("if statement completes")
elif a == -1:
    print("elif statement completes")
else:
    print("else prints")

#function
def sayHello():
    print("Hello!")

sayHello()

def addition(a, b):
    print(a + b)

addition(5, 15)

#for loop

for a in range(1,14): #2nd number is not inclusive
    print(a)

#while loop

z = 0

while z <= 20:
    print("You are" + " " + str(z) + " years old.")
    z += 1

#strings

myString = "some text"

print(myString)

print(type(myString))