# The game map
# | and - (pipes and dashes) ->  Walls
# G -> Ghosts
# . -> Empty spaces where the characteres can walk
# P -> Pills
# @ -> Pacman

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

# Finding Pacman
def find_pacman(map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):   # len(map) = number of rows
        for y in range(len(map[x])):    # len(map[x]) = number of columns 
            if map[x][y] == "@":    # "@" = Pacman
                pacman_x = x
                pacman_y = y
    
    return pacman_x, pacman_y


# Moving Pacman
def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)

    # The place where the pacman was is now empty.
    new_row = map[pacman_x][0:pacman_y] + "." + map[pacman_x][pacman_y+1]
    # new_row = everything before pacman + empty space + everything after pacman
    map[pacman_x] = new_row
    
    # The new place has the pacman.
    new_row_2 = map[next_pacman_x][0:next_pacman_y] + "@" + map[next_pacman_x][next_pacman_y+1]
    # new_row = everything before empty space + pacman + everything after empty space
    map[next_pacman_x] = new_row_2
        