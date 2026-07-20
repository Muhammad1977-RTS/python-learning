import sys
sys.stdout.reconfigure(encoding='utf-8')

flag = False
for _ in range(5):
    word = input()
    
    if len(word) < 5:
        flag = True

print(flag)

