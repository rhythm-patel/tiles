# Algorithm Idea 1

1. Generate a graph with stolen tiles (1's) as nodes and other connected (Up, Down, Left, Right) tiles as edges.
2. The graph will always be bipartite. 
3. Find Maximum Bipartite Matching by Ford Fulkerson
4. 2 checks:
	1. Return 0 if odd number of 1's (since new tiles are 2x1) 
	2. Return 0 if left set and right set of bipartite graph not equal
	
# Algorithm Idea 2

1. Generate a graph with stolen tiles (1's) as nodes and other connected (Up, Down, Left, Right) tiles as edges.
2. The graph will always be bipartite. 
3. Check for:
	1. Return 0 if odd number of 1's (since new tiles are 2x1) 
	2. Return 0 if left set and right set of bipartite graph not equal
4. Start combining outermost edges i.e. vertics with min number of edges (vertices with min degree)
