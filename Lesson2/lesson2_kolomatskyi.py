
#TASK_1

print("enter your name: ")
name = input()
print("enter your last name: ")
last_name = input()


print("My name is " + name + " last name is " + last_name )
print("My name is {} last name is {} ".format(name, last_name))
print(f"My name is {name} last name is {last_name}")
full_name = name + ' ' + last_name
print(full_name.title())
print(full_name.upper())
print((full_name.lower()))
print("My name is " + (name.strip()) + " last name is " + last_name )
full_name = (name.strip() + ' ' + last_name)
print(full_name)

#TASK_2

print (" Enter the value of the radius: ")
radius = input()
import math

square = (math.pi * (float (radius) ** 2))
length = (math.pi * (float(radius) * 2))
print (" The square of the circle is: ", math.pi * (float (radius) ** 2))
print (" The length of the circle is: ", math.pi * (float(radius) * 2))
print("The square is {} length {} ".format(square, length))
print(f"The square is {square} length {length} ")

#TASK_3

print (" Введіть значення поточного курсу USD до гривні: ")
usd = input()

uah = (1 / float (usd))
print(f"Поточний курс складає: {round (uah, 2)}" )

