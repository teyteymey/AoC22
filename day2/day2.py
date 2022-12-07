f = open('input.txt', 'r')

glob_points = 0

for x in f:
    l_f = list(x)
    if (l_f[0] == 'A'): #rock
        if (l_f[2] == 'X'):
            glob_points += 1+3
        if (l_f[2] == 'Y'):
            glob_points += 2+6
        if (l_f[2] == 'Z'):
            glob_points += 3+0
    if (l_f[0] == 'B'): #paper
        if (l_f[2] == 'X'):
            glob_points += 1+0
        if (l_f[2] == 'Y'):
            glob_points += 2+3
        if (l_f[2] == 'Z'):
            glob_points += 3+6
    if (l_f[0] == 'C'): #scissor
        if (l_f[2] == 'X'):
            glob_points += 1+6
        if (l_f[2] == 'Y'):
            glob_points += 2+0
        if (l_f[2] == 'Z'):
            glob_points += 3+3

print(glob_points)