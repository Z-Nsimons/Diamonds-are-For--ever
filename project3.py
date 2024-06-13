# Project 3
# CMSC 254
# <Zerlyne>

# include the sys module in this program
import sys
numRows = int(sys.argv[1])
count = 0

# top triangle
# use % to calculate remainder for even numbers
if numRows % 2 == 0 and numRows < 21:
# divide rows by 2 for top half of diamond
    for i in range(int(numRows/2)):
        print(" " * (int(numRows/2) - i) + "* " * (i + 1))
# add 1 to i since the count starts at 0 and is off by 1
        count = count + (i + 1)
    for z in range(int(numRows/2)):
        print(" " * (z + 1) + "* " * (int(numRows/2) - z))
        count = count + (z + 1)

# bottom triangle
# use % to calculate remainder for odd numbers
elif numRows % 2 != 0 and numRows < 21:
# divide rows by 2 for bottom half of diamond
    for i in range(int(numRows/2) + 1):
        print(" " * (int(numRows/2) - i) + "* " * (i + 1))
# add 1 to i since the count starts at 0 and is off by 1
        count = count + (i + 1)
    for z in range(int(numRows/2)):
        print(" " * (z + 1) + "* " * (int(numRows/2) - z))
        count = count + (z + 1)
    
# parameters for program arguments   
if numRows < 1:
    print("Invalid input value. The number of rows cannot be less than 1.")
    
elif numRows > 20:
    print("Invalid input value. The number of rows cannot be more than 20.")

if numRows > 0 and numRows < 21:
    print(count)
else:
    print(" ")