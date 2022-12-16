f = open('input.txt', 'r')
commands = f.readlines()
dir_sizes = {}
ndir = '/'
accu_size = 0
path_dir = []

dir_sizes['/'] = 0

for command in commands:

    if command.startswith('$ cd ..'):
        path_dir.pop()
        #ndir = "/".join(path_dir)
    elif command.startswith('$ cd '):
        size = len(command)
        nomdir = command[5:size-1]    #nombre dir actual
        path_dir.append(nomdir)       #lo pongo en el path
        ndir = "/".join(path_dir)
        dir_sizes[ndir] = 0 #ini del directorio a 0
    elif command.startswith('$ ls'):
        continue
    elif command.startswith('dir '):
        continue
    else:   #size of file
        line = command.split(' ')
        #dir_sizes[ndir] += int(line[0])  # se guarda el tamaño que tenia
        for i in range(1, len(path_dir)+1):
            parent_path = path_dir[0:i]
            parent_path = "/".join(parent_path)
            print(parent_path)
            dir_sizes[parent_path] += int(line[0])

    #print(command, ndir, accu_size, dir_sizes, path_dir)

#at the end to calculate the correct sizes
for dir in path_dir:
    ndir = "/".join(path_dir)
    dir_sizes[ndir] += accu_size  # añado al dir donde estaba el tamaño
    path_dir.pop()

response = 0
for dir in dir_sizes:
    if dir_sizes[dir] <= 100000:
        response += dir_sizes[dir]

print(dir_sizes)
print(response)

#1068023 -> too low
#1567808 -> too high