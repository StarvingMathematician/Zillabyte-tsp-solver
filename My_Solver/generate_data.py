'''
Created on Dec 2, 2013

@author: Jonathan Simon
'''

from random import random

if __name__ == '__main__':
    random_points_100 = [str(random())+' '+str(random())+'\n' for _ in range(100)]
    random_points_1000 = [str(random())+' '+str(random())+'\n' for _ in range(1000)]
    
    outfile1 = open("/Users/Macbook/Documents/Git_Repos/Zillabyte-tsp-solver/Input/random_points_100.txt",'w')
    outfile1.writelines(random_points_100)
    outfile1.close()
    
    outfile2 = open("/Users/Macbook/Documents/Git_Repos/Zillabyte-tsp-solver/Input/random_points_1000.txt",'w')
    outfile2.writelines(random_points_1000)
    outfile2.close()