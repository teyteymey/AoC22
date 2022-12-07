f = open('input.txt', 'r')

glob_points = 0

for x in f:
    print(x)
    l_f = list(x)
    l_f = l_f[:-1]
    size = len(l_f)
    l_f1 = l_f[:(size//2)]
    l_f2 = l_f[size//2:]

    for letter in l_f1:
        if letter in l_f2:
            print(letter)
            if ord(letter) > 96:
                glob_points += ord(letter)-ord('a')+1
            else:
                glob_points += ord(letter)-ord('A')+1+26
            break

print(glob_points)

