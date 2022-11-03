# Asking the user for the number they want to convert.
# Plus checking if the input from the user is a valid number.
num = -1
while num < 0 or num > 255:
    num = int(input("Enter the number you want to convert to binary: "))
    if num > 0 and num < 255:
        print(" ")
    else:
        print("Not a valid number. Please enter a number between 0 and 255.")

help_list = [128, 64, 32, 16, 8, 4, 2, 1]
binary_list = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(8):
    if num >= help_list[i]:
        num = num - help_list[i]
        binary_list[i] = 1

print(binary_list)
