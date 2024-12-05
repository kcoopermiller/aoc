from collections import defaultdict

part1, part2 = open('input.txt').read().split('\n\n')
part1, part2 = part1.splitlines(), part2.splitlines()

order = defaultdict(set)
for i, line in enumerate(part1):
    before, after = map(int, line.split('|'))
    order[before].add(after)

pt1_tot, pt2_tot = 0, 0
for i, line in enumerate(part2):
    pages = [int(x) for x in line.split(',')]
    bad = False
    for j in range(len(pages)):
        if bool(order[pages[j]] & set(pages[:j])):
            bad = True
            for k in range(j):
                if pages[k] in order[pages[j]]:
                    pages[j], pages[k] = pages[k], pages[j]
    if not bad: pt1_tot += pages[len(pages)//2]
    else: pt2_tot += pages[len(pages)//2]

print(f'Part 1: {pt1_tot}\nPart 2: {pt2_tot}')

