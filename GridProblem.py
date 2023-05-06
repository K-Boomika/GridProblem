import sys
from itertools import product

def isValid(letter, row, col, grid):
    neighbors = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        r, c = row + dr, col + dc
        if 0 <= r < 5 and 0 <= c < 5:
            neighbor = grid[r][c]
            if neighbor != '-':
                neighbors.append(neighbor)

    if not neighbors:
        return True

    for neighbor in neighbors:
        if abs(ord(neighbor) - ord(letter)) == 1:
            return True

    return False

def SelectUnassignedVariable(grid, domain):
    # Choose the variable with the smallest domain
    smallest_domain_size = float('inf')
    smallest_domain_var = None
    for (row, col), d in domain.items():
        if grid[row][col] == '-' and len(d) < smallest_domain_size:
            smallest_domain_size = len(d)
            smallest_domain_var = (row, col)
    return smallest_domain_var

def GridProblem(grid, remaining_letters, domain, row=0, col=0):
    if not remaining_letters:
        return True

    if col == 5:
        row += 1
        col = 0

    if grid[row][col] != '-':
        return GridProblem(grid, remaining_letters, domain, row, col + 1)

    var = SelectUnassignedVariable(grid, domain)

    for letter in domain[var] & remaining_letters:
        if isValid(letter, var[0], var[1], grid):
            grid[var[0]][var[1]] = letter
            new_remaining_letters = remaining_letters - {letter}

            # Get affected cells
            affected_cells = []
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = var[0] + dr, var[1] + dc
                if 0 <= r < 5 and 0 <= c < 5 and grid[r][c] == '-':
                    affected_cells.append((r, c))

            # Update domains of affected cells
            for r, c in affected_cells:
                domain[(r, c)] -= {letter}
                if not domain[(r, c)]:
                    # Domain is empty, invalid placement
                    grid[var[0]][var[1]] = '-'
                    continue

            # Recursive GridProblem with updated domain
            if GridProblem(grid, new_remaining_letters, domain, var[0], var[1]):
                return True

            # Revert domains of affected cells
            for r, c in affected_cells:
                domain[(r, c)].add(letter)

            grid[var[0]][var[1]] = '-'

    return False

def getData(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            grid_vals = line.strip().split()
            for val in grid_vals:
                row.append(val)
            grid.append(row)
    return grid

def getRemaining(grid):
    used_letters = set()

    for row in grid:
        for cell in row:
            if cell != '-':
                used_letters.add(cell)

    remaining_letters = set(chr(ord('A') + i) for i in range(25)) - used_letters
    return remaining_letters

def getDomain(grid):
    domain = {}
    for row, col in product(range(5), range(5)):
        if grid[row][col] == '-':
            domain[(row, col)] = getRemaining(grid)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < 5 and 0 <= c < 5 and grid[r][c] != '-':
                    domain[(row, col)] -= {grid[r][c]}
            if len(domain[(row, col)]) == 0:
                return {} # Empty domain, no solution possible
    return domain

def main():
    if len(sys.argv) <= 1:
        return
    else:
        filename = sys.argv[1]
        if ".txt" in filename:
            if len(sys.argv) < 2:
                return
            else:
                grid = getData(filename)
                #print(grid)
                domain = getDomain(grid)
                #print(domain)
                remaining = getRemaining(grid)
                if GridProblem(grid, remaining, domain):
                    for row in grid:
                        print(" ".join(row))
                else:
                    print("No solution found")

if __name__ == "__main__":
    main()
