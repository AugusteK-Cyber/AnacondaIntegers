# Course: CMSC 331, Fall 2021
# File: cmsc331_hw3.py
# Homework: HW3
# Author: Auguste Kiendrebeogo
# Email: akiendr1@umbc.edu
# Date: 10/09/2021

# The program reads in a single character at a time and recognizes Anaconda integers.
# It reads a single character at a time from an input file "input.txt" which will contain
# several lines with different strings to be tested. Then, it will write to an output file
# (<YOUR_CAMPUS_ID>.txt) where each line will contain the result for each string (i.e., whether
# the strings is accepted as an Anaconda integer or not).

#!/usr/bin/env python3

# File name as a constant
FILE = "input.txt"
    
# Decimal check
def decimalcheck(*args):
    i = 1
    for line in args:
        size = len(line) # Size of the string
        # Single zero
        if line.startswith('0') and size == 1:
            return True
        # Zero and another number
        if line.startswith('0') and ord(line[i]) > ord('0'):
           return False
        # Ex: +0
        if ((line.startswith('+') or line.startswith('-')) and ord(line[i]) == ord('0') and size == 2):
            return True
        # Ex: +02
        if ((line.startswith('+') or line.startswith('-')) and ord(line[i]) == ord('0') and size > 2):
           return False
        # Everything after, starting at i = 1
        while i < size:
            if ord(line[i]) in range(ord('1'), ord('9')+1):
               i += 1
            else:
               return False

    return True

# Hexadecimal check
def hexadecimalcheck(*args):
    i = 3
    for line in args:
        size = len(line)
        # Ex: 0x or -0x
        if size < 4:
            return False
        # Ex: 0a, 0j
        if line.startswith('0') and not line.startswith('x',1,2) and not line.startswith('X',1,2):
            return False
        # Ex: -1a
        if (line.startswith('+') or line.startswith('-')) and not line.startswith('0',1,2) and not line.startswith('x',2,3) and not line.startswith('X',2,3):
            return False
        # Ex: +0x044
        if (line.startswith('+') or line.startswith('-')) and line.startswith('0',1,2) and (line.startswith('x',2,3) or line.startswith('X',2,3)) and line.startswith('0',3,4) and size > 4:
           return False
        # Ex: 0X01
        if line.startswith('0') and (line.startswith('x',1,2) or line.startswith('X',1,2)) and line.startswith('0',2,3) and size > 3:
           return False
        # Anything else after, starting at i = 3
        while i < size:
            if ord(line[i]) in range(ord('0'), ord('9')+1) or ord(line[i]) in range(ord('a'), ord('f')+1) or ord(line[i]) in range(ord('A'), ord('F')+1):
                i += 1
            else:
                return False

    return True
        
# Octal check
def octalcheck(*args):
    i = 1
    for line in args:
        size = len(line)
        # Ex: 0
        if size < 2:
           return False
        # Ex: -1
        if ((line.startswith('+') or line.startswith('-')) and (ord(line[i]) not in range(ord('0')))):
           return False
        # Ex: 142
        if ((not line.startswith('0')) and (not line.startswith('+'))) and (not line.startswith('-')):
           return False
        # Ex: 00
        if line.startswith('0',0,2) and line.startswith('0',1,2) and size == 2:
           return True
        while i < size:
            if ord(line[i]) in range(ord('1'), ord('8')):
                i += 1
            else:
               return False
            
    return True 


# Write to a file with my campus ID (QD95656@umbc.edu)
def writetofile(var):
    f = open("akiendr1.txt", "a")
    f.write(var)
    f.write('\n')
    f.close()

    
# Main function
def main():
    count = 0 # Keep track of the number of lines in the file
    arrayOfLines = [] # List of strings
    file = open(FILE) # Open the file
    lines = file.readlines() # Read lines of the file

    # Loop through the file and append data to the list
    for line in lines:
        count += 1 # Increment and get number of lines in the file
        arrayOfLines.append(line.strip('\n'))
        
    # Close file
    file.close()

    # Display results
    print("Writing to the file ...")
    p = 0
    while (p < count):
        if decimalcheck(arrayOfLines[p]) == True:
            writetofile("D")
        elif hexadecimalcheck(arrayOfLines[p]) == True:
            writetofile("H")
        elif octalcheck(arrayOfLines[p]) == True:
            writetofile("O")
        else:
            writetofile("N")
        p += 1
    
    
# Call main
main()



