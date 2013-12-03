Zillabyte-tsp-solver
====================

Design an algorithm to approximately solve the travelling salesman problem (tsp). This algorithm must perform better (in terms of cost) than Zillabyte's current greedy algorithm, and also be reasonably efficient. Note that the graph is *not* assumed to be fully connected.

* Input:
  * "random_points_100.txt" - 100 randomly generated points in the unit square
  * "random_points_1000.txt" - 1000 randomly generated points in the unit square
* Output:
  * "tsp_solution2_output1000.txt" - the output displayed by 'tsp_solution2.py' when given 'random_points_1000.txt' as input
* My_Solver:
  * "generate_data.py" - generates both the 100-point and 1000-point data files
  * "tsp_solution.py" - my first tsp algorithm (assumes that the input graph is complete)
  * "tsp_solution2.py" - my second tsp algorithm (also assumes that the input graph is complete); the primary changes are in the 'swap_node_pairs' function, and in the actual solution generation
