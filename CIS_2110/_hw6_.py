def header():
    print("David Lee\nMSU Denver\nCIS 2110 With Professor Joe Hasley\nSummer 2022\n")

header()

def line_break():
    print("\n$*$*$*$*$  _HW6_  $*$*$*$*$  _HW6_  $*$*$*$*$  _HW6_  $*$*$*$*$\n")
    
line_break()

def SumOfThree(a, b, c):
    return a + b + c
def AvgOfThree(a, b, c):
    avg = (a + b + c)/3
    return avg
def BigOfThree(a, b, c):
    return max(a, b, c)

a = float(input("Enter first floating pt number: "))
b = float(input("Enter second floating pt number: "))
c = float(input("Enter third floating pt number: "))
print("Sum= ", SumOfThree(a, b, c))
print("Average= ", AvgOfThree(a, b, c))
print("Largest= ", BigOfThree(a, b, c))

line_break()

# Program 2
def FindArea(height, width):
    return height * width

height = int(input("Enter a height: "))
width = int(input("Enter a width: "))

print(FindArea(height, width))

line_break()

# Program 3
def translate(number):
    translated_number = ""
    two = ['a','b','c','A','B','C']
    three = ['d','e','f','D','E','F']
    four = ['g','h','i','G','H','I']
    five = ['j','k','l','J','K','L']
    six = ['m','n','o','M','N','O']
    seven = ['p','q','r','s','P','Q','R','S']
    eight = ['t','u','v','T','U','V']
    nine = ['w','x','y','z','W','X','Y','Z']
    for i in number:
        if i.isdigit():
            translated_number += i
        elif i in two:
            translated_number += '2'
        elif i in three:
            translated_number += '3'
        elif i in four:
            translated_number += '4'
        elif i in five:
            translated_number += '5'
        elif i in six:
            translated_number += '6'
        elif i in seven:
            translated_number += '7'
        elif i in eight:
            translated_number += '8'
        elif i in nine:
            translated_number += '9'
        else:
            return "Invalid Number"
    return translated_number

# Reading from the user
number = input("Enter a 800 number you would like to translate. Do not include hyphens: ")
print("The number you want to call is:",translate(number))

line_break()

