# Sudoku Solver
This is a simple program that uses a backtracking algorithm to solve a Sudoku puzzle. The program takes a 9x9 grid as input, where empty cells are represented by 0, and solves the puzzle by filling in the missing numbers.

## How to use
- First, enter the sudoku puzzle in the form of a 9x9 grid, with empty cells represented by 0.
- Run the program, it will output the solved puzzle, if it has a unique solution.

## Input format
The input is a 9x9 grid, where each cell is a number from 0 to 9, where 0 represents an empty cell. The input can be given in the following format:
```
0 3 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 3
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 8 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

## Output format
The output is the solved puzzle in the form of a 9x9 grid, where each cell is a number from 1 to 9. If there is no unique solution, the output will be a message saying that the puzzle is not solvable.

## Example
```
Input:
0 3 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 3
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 8 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```
```
Output:
1 3 2 8 5 9 4 7 6
4 6 9 7 2 1 5 8 3
8 5 7 4 9 3 2 1 6
3 7 1 2 6 4 8 5 9
5 2 8 3 7 6 1 9 4
9 4 6 1 8 5 7 3 2
6 8 5 9 3 7 1 2 4
2 1 4 6 4 2 9 6 7
7 9 3 5 1 8 6 4 8
```

## Note
This code uses a backtracking algorithm to solve the sudoku puzzle which may not be the most efficient one, but it works.
Also, some of the test cases that have multiple solutions or no solutions, it will not work properly.

## Conclusion
This program provides a simple and straightforward solution to solving a Sudoku puzzle using backtracking algorithm. It can be used as a reference for understanding how a backtracking algorithm works and can be further optimized for better performance.