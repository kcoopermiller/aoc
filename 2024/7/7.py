import itertools

ans = 0
for line in open('input.txt'):
    tot, nums = line.split(':')
    tot = int(tot)
    nums = [int(x) for x in nums.strip().split()]
    
    for ops in itertools.product(['+', '*', '||'], repeat=len(nums)-1):
        result = nums[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += nums[i + 1]
            elif op == '*':
                result *= nums[i + 1]
            else:
                result = int(f"{result}{nums[i + 1]}")
        if result == tot:
            ans += tot
            break
print(ans)