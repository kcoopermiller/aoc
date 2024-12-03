import re
import math

data = open('input.txt').read()

matches = re.findall(r'mul\(\d+,\d+\)', data)
print(sum([math.prod(list(map(int, re.findall(r'\d+', match)))) for match in matches]))

dos = re.split(r'do\(\)', data)
dos = [re.split(r'don\'t\(\)', dont)[0] for dont in dos]
matches = re.findall(r'mul\(\d+,\d+\)', ' '.join(dos))
print(sum([math.prod(list(map(int, re.findall(r'\d+', match)))) for match in matches]))
