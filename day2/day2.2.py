f = open('input.txt', 'r')

glob_points = 0
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
piedra = 1
papel = 2
tijera = 3
for x in f:
    l_f = list(x)
    if (l_f[0] == 'A'): #rock
        if (l_f[2] == 'X'):
            glob_points += 0+tijera
        if (l_f[2] == 'Y'):
            glob_points += 3+piedra
        if (l_f[2] == 'Z'):
            glob_points += 6+papel
    if (l_f[0] == 'B'): #paper
        if (l_f[2] == 'X'):
            glob_points += 0 + piedra
        if (l_f[2] == 'Y'):
            glob_points += 3 + papel
        if (l_f[2] == 'Z'):
            glob_points += 6 + tijera
    if (l_f[0] == 'C'): #scissor
        if (l_f[2] == 'X'):
            glob_points += 0 + papel
        if (l_f[2] == 'Y'):
            glob_points += 3 + tijera
        if (l_f[2] == 'Z'):
            glob_points += 6 + piedra

print(glob_points)