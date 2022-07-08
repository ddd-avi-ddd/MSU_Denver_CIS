header = "David Lee \nHomework 5 \nMSU-Denver \nSummer 2022 \nCIS 2110 with Professor Joe Hasley \n \n "

print(header)
print("$*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$\n \n")
print("Program 1\n\n")

# User input #1
num1 = int(input("Please input an integer less than 500: "))
# User input #2
num2 = int(input("Please input a second #, with which to divide by: "))
iv = 1
while iv < num1:
    if(iv % num2 == 0):
        print(iv)
    iv += 1
print("Thank you, end program 1\n\n")
print("$*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$\n \n")

print("Program 2\n\n")

# User Input
upper_limit = int(input("Please enter an integer between 0 & 100 (Upper Limit): "))
lower_limit = int(input("Enter a second integer between 0 & 100 (Lower Limit): "))
#Initial sum & count set to 0
sum = 0
count = 0
# While loop
while(lower_limit < upper_limit):
    print(lower_limit)
    sum += lower_limit
    lower_limit += 1
    count += 1
print("The numbers between upper & lower limits are: ", count)
print("The sum of the numbers: ", sum)
print("$*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$\n \n")
print("Program 2b\n\n")

# # User Input
upper_limit = int(input("Please enter an integer between 0 & 100 (Upper Limit): "))
lower_limit = int(input("Enter a second integer between 0 & 100 (Lower Limit): "))
#Initial sum & count set to 0
sum = 0
count = 0
for i in range(lower_limit, upper_limit):
    print(i)
    count += 1
    sum += i
print("The numbers between upper & lower limits are: ", count)
print("The sum of the numbers: ", sum)

print("$*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$\n \n")
print("Program 3\n\n")

# User input into variable str
str = input("Please enter a string of your choosing: ")
# Iterate over string
for i in str:
    if(i.isupper()): #check if character of a string is uppercase of not
        print(i, i.lower()) #if yes then print it's lowercase
    elif(i.islower()): #check if character of a string is lower of not
        print(i, i.upper()) #if yes then print it's uppercase
    elif(i.isdigit()): #check if character of a string is digit of not
        print("The original is ", i) #if yes then print the original digit
        print("The square of ", i," is ",int(i)**2) #print the square of the digit
    elif(i.isspace()): #if character of a string is space
        print("SPACE") #prints space
    else:
        print(i, " is a special character") #prints i is a special character

print("$*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$\n \n")
print("Program 4\n\n")

#Initial sum & count set to 0
sum = 0
count = 0
while True:
    #enter a number or a string done to exit
    num = input("Enter a floating point number or done to exit : ")
    if(num=="done"):
        break
    else:
        #convert the num to float and append it to the floating_point_list
        num=float(num)
        count+=1
        sum+=num
        
# Calculate Average
average = sum/count

# Print Output
print("The count of the numbers entered ", count)
print("The sum of the numbers entered", sum)
print("Average of the numbers entered ", average)

print("Thanks for your Data!!!\n\n")
print("$*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$  HW5  $*$*$*$*$*$\n \n")
