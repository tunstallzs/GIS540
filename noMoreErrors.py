# Name: Zachary Tunstall
# ID: zstunsta

# Script Name: NoMoreErrors.py

dataName = 'Lucca.gdb'
county = 'Dyer'
ID = 20

# 1. Print the name of the script.
print 'NoMoreErrors.py'

# 2. Print the last chararcter in dataName
print dataName[-1]

# 3. Use a string method to change the first letter
#    of dataName to M ('Mucca.gdb' not 'Lucca.gdb')
#    and print the results
a = dataName.replace('L', 'M')
print a

# 4. Concatenate county and ID and print the results
fullName = county + str(ID)
print fullName

# 5. Print the county in all caps.
allCaps = county.upper()
print allCaps

# 6. Print the feedback message or the last line of the traceback resulting
# from each erroroneous line in #1-5 before each was repaired. #1 and 2 are
# done for you.
print '#1. FEEDBACK BAR: Failed to check - syntax error - EOL while scanning string literal'
print '#2. TRACEBACK: IndexError: string index out of range'
print "#3. TRACEBACK: TypeError: 'str' object does not support item assignment"
print "#4. TRACEBACK: TypeError: cannot concatenate 'str' and 'int' objects"
print '#5. TRACEBACK: TypeError: upper() takes no arguments (1 given)'
