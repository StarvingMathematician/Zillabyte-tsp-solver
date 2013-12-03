'''
Created on Dec 3, 2013

Assume that the graph is complete, and that data comes in as a txt file of the form:

 x_1 y_1
 x_2 y_2
 . . .
 x_n y_n

@author: Jonathan Simon
'''

from math import sqrt
from numpy import array
from time import time

'''
Calculates the Euclidean distance between two points in 2D.
'''
def euc_dist(pair1,pair2):
    return sqrt((pair1[0] - pair2[0])**2 + (pair1[1] - pair2[1])**2) 

'''
Uses a greedy strategy to find an approximate tsp solution.
''' 
def greedy_search(start_node,dist_array):
    ordered_index_list = [start_node]
    already_visited_set = set([start_node])
    while len(ordered_index_list) < len(dist_array):
        current_min_val = None
        for idx,val in enumerate(dist_array[ordered_index_list[-1]]):
            if idx not in already_visited_set:
                if val < current_min_val or current_min_val == None:
                    current_min_idx = idx
                    current_min_val = val
        ordered_index_list.append(current_min_idx)
        already_visited_set.add(current_min_idx)
    return ordered_index_list #don't add the return node until the very end
        
'''
Loops through all nodes in sequential order, swapping adjacent nodes when doing so will decrease the overall cost.
'''
def swap_node_pairs(ordered_index_list,dist_array):
    new_ordered_index_list = ordered_index_list[:]
    for i in range(len(new_ordered_index_list)):
        i1,i2,i3 = [(i+j)%len(new_ordered_index_list) for j in [1,2,3]]
        current_dist = dist_array[new_ordered_index_list[i],new_ordered_index_list[i1]] + dist_array[new_ordered_index_list[i1],new_ordered_index_list[i2]] + dist_array[new_ordered_index_list[i2],new_ordered_index_list[i3]] 
        new_dist = dist_array[new_ordered_index_list[i],new_ordered_index_list[i2]] + dist_array[new_ordered_index_list[i2],new_ordered_index_list[i1]] + dist_array[new_ordered_index_list[i1],new_ordered_index_list[i3]]
        if new_dist < current_dist:
            new_ordered_index_list[i1], new_ordered_index_list[i2] = new_ordered_index_list[i2], new_ordered_index_list[i1]
    return new_ordered_index_list
        
'''
Calculates the cost of 'this_solution'. 
'''
def solution_cost(this_solution,dist_array):
    accumulated_sum = 0
    for idx,val in enumerate(this_solution):
        accumulated_sum += dist_array[val,this_solution[(idx+1)%len(this_solution)]]
    return accumulated_sum
    
if __name__ == '__main__':
    #infile = open("/Users/Macbook/Documents/Git_Repos/Zillabyte-tsp-solver/Input/random_points_100.txt",'r')
    infile = open("/Users/Macbook/Documents/Git_Repos/Zillabyte-tsp-solver/Input/random_points_1000.txt",'r')
    cities_list = [map(float,line[:-1].split()) for line in infile.readlines()]
    infile.close()
    
    dist_array = array([[euc_dist(city1,city2) for city1 in cities_list] for city2 in cities_list])
    
    greedy_start_time = time()
    greedy_solution = greedy_search(0,dist_array)
    print "Greedy solution cost:", solution_cost(greedy_solution,dist_array)
    print "Greedy run time:", time()-greedy_start_time
    
    my_start_time = time()
    my_solution = greedy_search(0,dist_array)
    num_loops = 0
    while True:
        #print "Cost " + str(num_loops) + ":", solution_cost(my_solution,dist_array)
        new_solution = swap_node_pairs(my_solution,dist_array)
        if new_solution == my_solution:
            break
        else:
            my_solution = new_solution
            num_loops += 1
    print "\nMy solution cost:", solution_cost(my_solution,dist_array)
    print "My run time:", time()-my_start_time
    print "Additional loops required:", num_loops
    