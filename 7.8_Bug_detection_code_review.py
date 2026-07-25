s = input()

while len(s) <= 10:
    if len(s) % 4 == 0:
        s = 'x' + s
        print(s)
    elif len(s) % 5 == 0:
        s = 'y' + s
        print(s)
    else:
        s = 'zzz' + s
        print(s)

    s = '@' + s
