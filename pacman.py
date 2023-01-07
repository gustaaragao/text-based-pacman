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
