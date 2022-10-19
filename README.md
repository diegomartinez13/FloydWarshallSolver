# FloydWarshallSolver
Floyd Warshall Algorithm Solver using the terminal.

## Command
`python FloyWarshall.py [Const Adjacency Matrix] [k value]`

### Format of the arguments
- Const Adjacency Matrix shoud be in the form `[[...],[...],...]` with the infinite values (no connection between nodes) as `inf`
- k value should be an integer

### Result
The pregramm returns the k matrix in the same format as the Const Adjacency Matrix. If no k value was provided the programm will sove the matrix completely.

### Example
1. `python3 FloydWarshall.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 4` 
  - returns `[[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]`
2. `python3 FloydWarshall.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 1` 
  - returns `[[0, 3, inf, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, inf, 0]]`
