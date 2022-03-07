"""
ClassGenerator.py
By Matthew Graber
Made to generate repettitive class text
"""

proceed = 'y'
part3 = input("What is the name of the abstract class?")
totalText = ""

while proceed == 'y':

    part1 = "class"
    part2 = input("What is the specific name of the thing?")
    part4 = "   def __init__(self):\n      self.__name = '"+part2+"'"
    newText = part1 +" "+ part2+"("+part3+"):\n"+part4

    totalText += "\n\n" + newText
    proceed = input("Continue?")

file = open("TextGenerated.txt", 'w')
file.write(totalText)
file.close()