import numpy as np

f = open('input.txt', 'r')
tree_line = f.readlines()
lines_list = []

# convert the input in a matrix
for line in tree_line:
    list_current_line = list(line)  # convert line into list
    list_current_line = list_current_line[:len(list_current_line) - 1]  # get rid of the \n at the end of each line
    lines_list.append(list_current_line)  # add new line to the list of lists

matrix = np.array(lines_list)  # convert the list of lists into a matrix array

#print(matrix)
n_row = len(matrix)
n_col = len(matrix[1, :])

visible_r, visible_u, visible_d, visible_l = 0,0,0,0
scenic_score_temp: int = 0
scenic_score_final: int = 0
for i in range(1, n_row-1):
    for j in range(1, n_col-1):
        row = matrix[i, :]  #all the line
        col = matrix[:, j]
        height_tree = matrix[i, j]
        right = row[j+1:]
        left = row[:j]
        up = col[:i]
        down = col[i+1:]
        left = np.flip(left)    #bc we have to read from the index to the edge
        up = np.flip(up)
        #print(height_tree, right, left, up, down)
        #print(row, col)
        if max(right) >= height_tree:
            visible_r = np.argmax(right >= height_tree)+1     #get the index of the first tree that blocks the view
        else:
            visible_r = len(right)

        if max(left) >= height_tree:
            visible_l = np.argmax(left >= height_tree)+1     #get the index of the first tree that blocks the view
        else:
            visible_l = len(left)

        if max(up) >= height_tree:
            visible_u = np.argmax(up >= height_tree)+1     #get the index of the first tree that blocks the view
        else:
            visible_u = len(up)

        if max(down) >= height_tree:
            visible_d = np.argmax(down >= height_tree)+1     #get the index of the first tree that blocks the view
        else:
            visible_d = len(down)

        #print(visible_r, visible_u, visible_d, visible_l)
        scenic_score_temp = visible_d * visible_u * visible_l * visible_r

        if scenic_score_temp > scenic_score_final:
            scenic_score_final = scenic_score_temp
            #print(scenic_score_final)

print(scenic_score_final)
#8400 too low