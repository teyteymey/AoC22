f = open('input.txt', 'r')

line = f.readline()
line_list = list(line)
index = -1

for i in range(0, len(line_list), 1):
    explored_list = line_list[i:i+14]
    set_list = set(explored_list)
    if len(set_list) == 14:
        index = i
        break


print(index+14)
print(explored_list)