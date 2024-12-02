from collections import Counter

list_1 = []
list_2 = []

with open('input.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        list_1.append(a)
        list_2.append(b)

diff = sum(abs(i - j) for i, j in zip(sorted(list_1), sorted(list_2)))

counts = Counter(list_2)
count = sum(i * counts[i] for i in list_1)

print(diff)
print(count)
