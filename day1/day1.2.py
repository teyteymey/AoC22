f = open('input.txt', 'r')
glob_max = 0
for_max = 0
list = [0, 0, 0]
for x in f:
    if (x == "\n"):
        if (min(list) < for_max):
            list[list.index(min(list))]= for_max
        for_max = 0
    else:
        for_max += int(x)

print(sum(list))