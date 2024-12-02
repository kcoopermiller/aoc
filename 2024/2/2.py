part_1, part_2 = 0, 0
with open('input.txt', 'r') as file:
    for line in file:
        levels = list(map(int, line.split()))
        pt1_diff, pt2_diff = [], []
        for i in range(length := len(levels)):
            if i+1 < length: pt1_diff.append(levels[i] - levels[i+1])
            damp_level = levels[:i] + levels[i+1:]
            pt2_diff.append([damp_level[j] - damp_level[j+1] for j in range(len(damp_level)-1)])
        part_1 += 1 if set(pt1_diff) <= {1, 2, 3} or set(pt1_diff) <= {-1, -2, -3} else 0 # checks for subset of {1, 2, 3} or {-1, -2, -3}
        part_2 += 1 if any([set(diff) <= {1, 2, 3} or set(diff) <= {-1, -2, -3} for diff in pt2_diff]) else 0
    print(f'Part 1: {part_1}\nPart 2: {part_2}')