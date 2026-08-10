n = int(input())
lines = []
for i in range(n):
    lines.append(input())
query = input()

for line in lines:
    if query.lower() in line.lower():
        print(line)

