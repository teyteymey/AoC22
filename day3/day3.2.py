f = open('input.txt', 'r')

glob_points = 0
lines = f.readlines()

for i in range(0, len(lines), 3) :

    for letter in lines[i]:
        if (letter in lines[i+1]) and (letter in lines[i+2]):
            if ord(letter) > 96:
                glob_points += ord(letter)-ord('a')+1
            else:
                glob_points += ord(letter)-ord('A')+1+26
            break

print(glob_points)

