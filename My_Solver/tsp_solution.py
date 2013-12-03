'''
Created on Dec 2, 2013

Assume that data comes in as a txt file of the form:

 x_1 y_1
 x_2 y_2
 . . .
 x_n y_n

@author: Jonathan Simon
'''

from math import sqrt
from numpy import array
from time import time

def euc_dist(pair1,pair2):
    return sqrt((pair1[0] - pair2[0])**2 + (pair1[1] - pair2[1])**2) 

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
        
#This function alters 'ordered_index_list' and 'indices_to_visit' directly.
#Consider removing 'indices_to_visit' altogether, and instead just naively iterate over all indices.
def swap_node_pairs(ordered_index_list,indices_to_visit,dist_array):
    new_indices_to_visit = indices_to_visit.copy()
    for i in indices_to_visit:
        new_indices_to_visit.remove(i)
        i1,i2,i3,i1_minus,i2_minus = [(i+j)%len(ordered_index_list) for j in [1,2,3,-1,-2]]
        current_dist = dist_array[ordered_index_list[i],ordered_index_list[i1]] + dist_array[ordered_index_list[i1],ordered_index_list[i2]] + dist_array[ordered_index_list[i2],ordered_index_list[i3]] 
        new_dist = dist_array[ordered_index_list[i],ordered_index_list[i2]] + dist_array[ordered_index_list[i2],ordered_index_list[i1]] + dist_array[ordered_index_list[i1],ordered_index_list[i3]]
        if new_dist < current_dist:
            ordered_index_list[i1], ordered_index_list[i2] = ordered_index_list[i2], ordered_index_list[i1]
            new_indices_to_visit.add(i1); new_indices_to_visit.add(i2); new_indices_to_visit.add(i1_minus); new_indices_to_visit.add(i2_minus)
    indices_to_visit = new_indices_to_visit.copy()
        
def solution_cost(this_solution,dist_array):
    accumulated_sum = 0
    for idx,val in enumerate(this_solution):
        accumulated_sum += dist_array[val,this_solution[(idx+1)%len(this_solution)]]
    return accumulated_sum
    
if __name__ == '__main__':
    infile = open("/Users/Macbook/Documents/Git_Repos/Zillabyte-tsp-solver/Input/random_points_100.txt",'r')
    cities_list = [map(float,line[:-1].split()) for line in infile.readlines()]
    infile.close()
    
    dist_array = array([[euc_dist(city1,city2) for city1 in cities_list] for city2 in cities_list])
    #dist_array = [[euc_dist(city1,city2) for city1 in cities_list] for city2 in cities_list]
    
    your_start_time = time()
    your_solution_costs = [solution_cost(greedy_search(i,dist_array),dist_array) for i in range(len(cities_list))]
    print "Your min cost:", min(your_solution_costs)
    print "Your run time:", time()-your_start_time
    
    my_start_time = time()
    my_solution_costs = []
    for i in range(len(cities_list)):
        my_solution = greedy_search(i,dist_array)
        indices_to_visit = {i for i in range(len(cities_list))}
        max_loops = 100
        num_loops = 0
        while len(indices_to_visit) > 0 and num_loops <= max_loops:
            swap_node_pairs(my_solution,indices_to_visit,dist_array)
            num_loops += 1
        my_solution_costs.append(solution_cost(my_solution,dist_array))
    print "My min cost:", min(my_solution_costs)
    print "My run time:", time()-my_start_time
    
        
    