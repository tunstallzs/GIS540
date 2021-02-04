# Zach Tunstall
# zstunstall
# treeAnalysis.py
# Purpose: Define and use a Tree class to support tree data analysis
# Input: No arguments needed.

class Tree:
    def __init__(self, block, plot, species, dbh):
        '''Initialize tree object properties.'''
        self.block = block
        self.plot = plot
        self. species = species
        self.dbh = dbh
    
    def calculateDIB(self):
        '''Calculate DIB, assuming DIB is diameter breast height times 0.917.'''
        DIB = self.dbh * 0.917
        return DIB
    
    def calculateHeight(self):
        '''Calculate height, assuming that height is 86.6 plus 0.025 times the
        diameter breast height for loblolly pines (LP)
        and height is 98.8 plus 0.15 times the diameter breast height for all
        other species.'''
        if self.species == 'LP':
            tallness = 86.6 + ( 0.025 * self.dbh) 
        else:
            tallness = 98.8 + (0.15 * self.dbh)
        return tallness

    def report(self, num):
        '''Print tree properties.'''
        print '\nReport Tree', num
        print '-------------'
        print 'Block: {0}'.format(self.block)
        print 'Plot: {0}'.format(self.plot)
        print 'Species: {0}'.format(self.species)
        print 'DBH: {0}'.format(self.dbh)
        print 'DIB: {0}'.format(self.calculateDIB())
        print "Height: {0}".format(self.calculateHeight())
        print '\n'


if __name__ == '__main__':
    t1 = Tree(5, 91, 'SG', 14)  # Create a tree object t1 from record 1 of rdu_forest.txt
    print 'Tree 1 Species:', t1.species  # Print t1's species.
    dib = t1.calculateDIB()  # Calculate t1's DIB.
    print 'Tree 1 DIB:', dib  # Print t1's DIB.
    t1.report(1)  # Report t1 information.

    t2 = Tree(5, 91, 'LP', 23)  # Create a tree object t2 from record 2 of rdu_forest.txt
    print "Tree 2 DBH:", t2.dbh
    print "Tree 2 Height:", t2.calculateHeight()

    t3 = Tree(5, 91, 'LP', 18)
    print "Tree 3 block:", t3.block
    print "Tree 3 plot:", t3.plot

    t4 = Tree(5, 91, 'LP', 18)
    t4.calculateDIB()
    t4.calculateHeight()
    t4.calculateHeight()
    t4.report(4)
