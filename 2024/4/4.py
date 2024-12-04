data = open('input.txt').read().splitlines()
rows, cols = len(data), len(data[0])

directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
]

def check_part1(i, j, dx, dy):
    word = ''
    for k in range(4):
        new_i, new_j = i + k*dx, j + k*dy
        if not (0 <= new_i < rows and 0 <= new_j < cols):
            return False
        word += data[new_i][new_j]
    return word == 'XMAS' or word == 'XMAS'[::-1]

def check_part2(i, j):
    if not (0 < i < rows - 1 and 0 < j < cols - 1):
        return 0
    if data[i][j] != 'A':
        return 0
        
    diagonals = (
        data[i-1][j-1],
        data[i-1][j+1],
        data[i+1][j-1],
        data[i+1][j+1]
    )
    
    cross = {
        ('M', 'M', 'S', 'S'),
        ('S', 'S', 'M', 'M'),
        ('M', 'S', 'M', 'S'),
        ('S', 'M', 'S', 'M'),
    }
    
    return 1 if diagonals in cross else 0

part1, part2 = 0, 0
for i in range(rows):
    for j in range(cols):
        part1 += sum(check_part1(i, j, dx, dy) for dx, dy in directions)
        part2 += check_part2(i, j)

print(f'Part 1: {part1}\nPart 2: {part2}')