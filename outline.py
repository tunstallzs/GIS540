"""
Zach Tunstall
zstunsta
outline.py
Using a nested for loop to print an arbitrary string and iterate through a list
"""

list = ['a', 'b', 'c']
for r in range(1, 5):
    print str(r) + ') ' + 'hehe'

    for thing in list:
        print '    ' + thing + ') ' + 'hoho'
