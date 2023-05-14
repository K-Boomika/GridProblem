# Grid Problem Solver

This Python program solves a grid problem by assigning letters to empty cells based on certain constraints.

## Problem Description

The grid problem involves filling a 5x5 grid with letters such that each letter satisfies the following conditions:
- The letter should be adjacent (horizontally or vertically) to another letter.
- The absolute difference between the ASCII values of adjacent letters should be 1 for atleast one neighbouring letter.

## Implementation Details

The program uses a backtracking algorithm to solve the grid problem. It iterates over each empty cell in the grid and assigns a letter that satisfies the adjacency and difference conditions. If a letter violates the conditions, it backtracks and tries a different letter until a valid solution is found or all possibilities are exhausted.

The program also employs various helper functions to check letter validity, select unassigned variables, retrieve grid data, determine remaining letters, and generate the domain of possible letters for each empty cell.

The heuristic being used is the Minimum Remaining Values (MRV) heuristic. The SelectUnassignedVariable function selects the unassigned variable (empty cell) with the smallest domain (fewest possible values) from the domain dictionary.

## How to run the program
> python GridProblem.py GridLayout1.txt
