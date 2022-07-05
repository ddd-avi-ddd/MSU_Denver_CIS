header = "David Lee \nHomework 4 \nMSU-Denver \nSummer 2022 \nCIS 2110 with Professor Joe Hasley \n \n "

print(header)
print("$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")

print("Program 1\n")
# Request User Input
num = int(input("Enter a number plz: "))
# If/else
if num > 0:
    print("This is a positive number.")
elif num == 0:
    print("The number you have selected is Zero.")
else:
    print("That is a negative integer")
print();

print("$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")
print("Program 2\n\n")
print("$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")
# Request User Input
cash = float(input("Welcome to your automated change dispense service.\n\nPlease enter a figure under 10k: "))

# Count the number of bills/coins
count = cash // 20
if count != 0:
    print(int(count), " - $20 note")
cash -= 20 * count
count = cash // 10
if count != 0:
    print(int(count), " -$10 note")
cash -= 10 * count
count = cash // 5
if count != 0:
    print(int(count), " - $5 note")
cash -= 5 * count
count = cash // 1
if count != 0:
    print(int(count), " -$1 note")
cash -= count
count = cash // .25
if count != 0:
    print(int(count), " - quarters")
cash -= count * .25
count = cash // .1
if count != 0:
    print(int(count), " - dimes")
cash -= count * .1
count = cash // .05
if count != 0:
    print(int(count), " - nickles")
cash -= count * .05
count = cash // .01
if count != 0:
    print(int(count), " - pennies")
print("\n\n$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")

print("Program 3 \n\n$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")
# Request User Input
user = input("Enter a string of your choice: ")
# Analyze string & return output
if user.isalpha():
    print("Your string contains only letters.")
if user.isupper():
    print("Your string contains only uppercase letters.")
if user.islower():
    print("Your string contains only lowercase letters.")
if user.isdigit():
    print("Your string contains only digits.")
if user.isalnum():
    print("Your string contains only letters or digits.")
if user[0].isupper():
    print("Your string starts with an uppercase letter.")
if user[len(user) - 1] == '.':
    print("Your string ends with a period.")
print("\n\n$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")

print("Program 4 \n\n$*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$  HW4  $*$*$*$*$*$\n \n")
# Request User Input
income = float(input("Input your income to see what taxman takes: "))

# Calculate tax in percentage, based on income.
tax = 0.0
if income <= 50000:
    tax += income * .01
elif income <= 75000:
    tax += 50000 * .01 + (income - 50000) * .02
elif income <= 100000:
    tax += 50000 * .01 + 25000 * .02 + (income - 75000) * .03
elif income <= 250000:
    tax += 50000 * .01 + 25000 * .02 + 25000 * .03 + (income - 100000) * .04
elif income <= 500000:
    tax += 50000 * .01 + 25000 * .02 + 25000 * .03 + 150000 * .04 + (income - 250000) * .05
else:
    tax += 50000 * .01 + 25000 * .02 + 25000 * .03 + 150000 * .04 + 250000 * .05 + (income - 500000 * .06)

print("You owe the taxman:", tax)



