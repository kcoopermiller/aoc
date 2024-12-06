# https://docs.python.org/3/library/functions.html#complex
grid = {}
start = None
for i, line in enumerate(open('input.txt')):
    for j, char in enumerate(line):
        grid[i+j*1j] = char
        if char == '^': start = i+j*1j

# Part 1
pos, dir = start, -1
visited = set()
while pos in grid:
    visited |= {(pos,dir)}
    if grid.get(pos+dir) == "#":
        dir *= -1j
    else: 
        pos += dir
path = {pos for pos, _ in visited}

# Part 2
loops = 0
for obs in path:
    if obs == start:
        continue
        
    # Add an obstacle
    test_grid = grid | {obs: '#'}
    
    # Check if this creates a loop
    pos, dir = start, -1
    visited = set()
    while pos in test_grid:
        visited |= {(pos,dir)}
        if test_grid.get(pos+dir) == "#":
            dir *= -1j
        else:
            pos += dir
        if (pos,dir) in visited:
            loops += 1
            break

print(f'Part 1: {len(path)}\nPart 2: {loops}')