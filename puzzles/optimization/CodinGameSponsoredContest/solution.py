import sys
from random import randint
import numpy as np
import heapq


# functions
def update_field(field,current_pos,walls,moves,enemies):
    ''' Updateds the game field:
        1 : visisted field
        2 : walls
    '''
    field[current_pos[0]][current_pos[1]] = 1
    for wall in walls:
        if wall == 'A':
            field[current_pos[0]+1][current_pos[1]] = 2
        elif wall == 'E':
            field[current_pos[0]-1][current_pos[1]] = 2
        elif wall == 'D':
            field[current_pos[0]][current_pos[1]+1] = 2
        elif wall == 'C':
            field[current_pos[0]][current_pos[1]-1] = 2

    for move in moves:
        if move == 'A':
            field[(current_pos[0]+1)%X][current_pos[1]] = 1
        elif move == 'E':
            field[(current_pos[0]-1)%X][current_pos[1]] = 1
        elif move == 'D':
            field[current_pos[0]][(current_pos[1]+1)%Y] = 1
        elif move == 'C':
            field[current_pos[0]][(current_pos[1]-1)%Y] = 1
            
    for enemy in enemies:
        field[enemy[0]][enemy[1]] = 1
            
            
def check_enemies(coords,moves):
    coords_me = coords[-1]
    coords_en = coords[:-1]
    K = np.asarray(coords_en) - np.asarray(coords_me)
    too_close = K[np.any(abs(K) <= 2,axis=1) & np.any(abs(K) == 0,axis=1)]
    ind = np.where(np.logical_and(abs(too_close)>0, abs(too_close)<=2))
    bad_mv = np.sign(too_close[ind])+ind[1]
    return [moves[i] for i in bad_mv]

# I assume first two inputs are the size of the game field (X,Y)
Y = int(raw_input())
X = int(raw_input())
# number of players (next inputs)
nr_players = int(raw_input())
# you are the last player
print >> sys.stderr, 'The field size: ', X, Y
print >> sys.stderr, 'Number of players: ', nr_players

# initialize the game field
field = [[0 for row in range(Y)] for col in range(X)]

# Actions:
# A - go right
# B - do nothing
# C - go up
# D - go down
# E - go left

# all possible moves
arr = ['A','B','C','D','E']
# possible moves in the same order as obstacles
arr_go = ['C','A','D','E','B']
ind = 0
oppose_mv = ''

iter = 1
# game loop
while True:
    # next lines mark where the walls are in this order: CADE
    # '#' means there's an obstacle and '_' means good to go
    walls = ''.join(raw_input() for i in xrange(4))
    print >> sys.stderr, walls

    #  line = [map(int, raw_input().split()) for i in xrange(third_init_input)]
    # coordinates of the players at the current step
    coords = [[int(j) for j in raw_input().split()] for _ in xrange(nr_players)]
    coords_me = coords[-1]
    for j in xrange(nr_players):
        print >> sys.stderr, coords[j]

    # compute possible moves based on walls location
    moves = [arr_go[n] for n, elem in enumerate(walls) if elem == '_']
    no_go = [arr_go[n] for n, elem in enumerate(walls) if elem == '#']

    update_field(field,coords_me,no_go,moves,coords[:-1])
    #if iter > 300:
    #print >> sys.stderr, field

    # possible move: if you have more than one option,
    # try not to go to the opposite direction
    enemies = check_enemies(coords,arr_go[:-1])
    print >> sys.stderr, "You can go there:", moves
    print >> sys.stderr, "The enemies at: ", enemies
    if len(enemies) != 0:
        for enemy in enemies:
            if enemy in moves:
                moves.remove(enemy)

    preferred_moves = moves
    if len(preferred_moves) > 1:
        try:
            preferred_moves.remove(oppose_mv)
        except:
            pass
        
    if len(moves) == 0:
        # do nothing if you're traped
        next_mv = arr_go[-1]
        oppose_mv = ''
    elif len(preferred_moves) == 0:
        # choose next move randomly from the remaining options
        ind = randint(0,len(moves)-1)
        next_mv = moves[ind]
        # re-calculate the opposite direction
        oppose_mv = arr_go[(arr_go.index(next_mv)+2) % 4]
    else:
        # choose next move randomly from the remaining options
        ind = randint(0,len(preferred_moves)-1)
        next_mv = preferred_moves[ind]
        # re-calculate the opposite direction
        oppose_mv = arr_go[(arr_go.index(next_mv)+2) % 4]
    
    iter += 1
    print next_mv
