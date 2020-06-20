# Jerry Garretson
# June 19 2020


# Clear terminal screen
import os
#os.system('clear')

greetings = 'My Boss yelled "GET BACK TO WORK!"'

""" The back slash tells the compiler to escape out the very next character.
	It says to ignor the very next character and go on to the next
"""
greetings2 = "My Boss yelled \"GET BACK TO WORK!\""

print(greetings)
print(greetings2)

name1 = "Jerry"
name2 = "jerry"

print("Hello, my name is " + name1)

print(name1.upper())
print(name2.title())
print(name2.capitalize())
print(name1.lower())
print(name1.swapcase())
print(len(greetings))
print(greetings.split(" "))