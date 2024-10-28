#######################################
#                                     #
#  Script created by Mark L. Jensen   #
#  marklustyjensen@gmail.com          #
#  www.marklustyjensen.com            #
#                                     #
#######################################

# setting a non-valid number as the default value.
num = -1

# Using a while loop to aske the user for the number they want to convert.
# This while loop will keep asking the userfor a number until the user enter a valid number.
while num < 0 or num > 255:
    # Asking the user for the number they want to convert.
    num = int(input("Enter a number between 0 and 255 to convert to binary: "))
    # Checking if the input from the user is a valid number.
    if num > 0 and num < 255:
        print(" ")
    else:
        print("Not a valid number. Please enter a number between 0 and 255.")

# Creating the standard binary list used to convert the users number.
help_list = [128, 64, 32, 16, 8, 4, 2, 1]

# Creating an empty list to be filled in, creating the binary number
binary_list = [0, 0, 0, 0, 0, 0, 0, 0]

# Creating a for loop the will convert the numeric number into a binary represented by a list.
for i in range(8):
    if num >= help_list[i]:
        num = num - help_list[i]
        binary_list[i] = 1

# Printing the result.
print(binary_list)
