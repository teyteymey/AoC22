f = open('input.txt', 'r')

glob_points = 0
lines = f.readlines()

for line in lines:
    line_list = list(line)
    val = []
    acu = ''
    for i in range(0, len(line_list), 1):
        if line_list[i] == '-' or line_list[i] == ',' or line_list[i] == '\n':
            val.append(acu)
            acu = ''
        else:
            acu += line_list[i]

    val = [int(i) for i in val]

    if val[0] in range(val[2], val[3]+1) or val[1] in range(val[2], val[3]+1):
        glob_points += 1
    elif val[2] in range(val[0], val[1]+1) or val[3] in range(val[0], val[1]+1):
        glob_points += 1

print(glob_points)
