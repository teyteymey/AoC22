f = open('input.txt', 'r')

lines = f.readlines()
crates = [[] for i in range(9)]  # ini de la lista

for line in range(0, 8, 1):  # para cada linea de los crates
    line_list = list(lines[line])
    n_crate = 0
    for i in range(1, len(line_list), 4):  # del 1 al final de tres en tres: 1,4,7...
        if line_list[i] != ' ':
            crates[n_crate].insert(0, line_list[i])
        n_crate += 1

for line in range(10, len(lines), 1):  # para cada linea de los crates
    line_list = list(lines[line])

    if line_list[6] != ' ':  # if we move more than 9 items, then the index are moved
        n_items = int(line_list[5] + line_list[6])
        orig_crate = int(line_list[13]) - 1
        dest_crate = int(line_list[18]) - 1
    else:
        n_items = int(line_list[5])
        orig_crate = int(line_list[12]) - 1
        dest_crate = int(line_list[17]) - 1

    crates_moved = crates[orig_crate][len(crates[orig_crate]) - n_items:]  # sublist of nelements to move
    del crates[orig_crate][len(crates[orig_crate]) - n_items:]  # deletes them from the original list
    crates[dest_crate] += crates_moved  # add the stack of elements to the dest crate

crates_top = ''
for i in range(0, 9, 1): # read the tops of the crates
    crates_top += crates[i][-1]

print(crates)
print(crates_top)
