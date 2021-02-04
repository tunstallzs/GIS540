"""
Zach Tunstall
zstunsta
"""

# enumList.py
# Purpose: Use the enumerate function in a FOR-loop (instead of the WHILE-loop)
# Usage: No arguments needed.

soulBand = ['earth', 'wind', 'fire']

for num, element in enumerate(soulBand):
    print 'Field {0} is {1}.'.format( num, element)

