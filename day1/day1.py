f = open('input.txt', 'r')
glob_max = 0
for_max = 0
for x in f:
    if (x == "\n"):
        if glob_max < for_max:
            glob_max = for_max
            print(glob_max)
        for_max = 0
    else:
        for_max += int(x)

print(glob_max)