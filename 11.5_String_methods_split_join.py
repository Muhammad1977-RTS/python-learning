numbers = input().split()

count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

pairs = 0
for num in count:
    k = count[num]
    pairs += k * (k - 1) // 2

print(pairs)






