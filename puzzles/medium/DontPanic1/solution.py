import sys

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, \
    nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]
print >> sys.stderr, 'number of floors: ', nb_floors
print >> sys.stderr, 'width of the area: ', width
print >> sys.stderr, 'maximum number of rounds: ', nb_rounds
print >> sys.stderr, 'floor on which the exit is found: ', exit_floor
print >> sys.stderr, 'position of the exit on its floor: ', exit_pos
print >> sys.stderr, 'number of generated clones: ', nb_total_clones
print >> sys.stderr, 'ignore (always zero): ', nb_additional_elevators
print >> sys.stderr, 'number of elevators: ', nb_elevators
print >> sys.stderr, '\n'

if nb_elevators > 0:
    elevator_floor, elevator_pos = zip(*([int(j) for j in raw_input().split()]
                                         for i in xrange(nb_elevators)))
    print >> sys.stderr, 'floor on which this elevator is found: ', elevator_floor
    print >> sys.stderr, 'position of the elevator on its floor:', elevator_pos

# possible directions
dirs = ['LEFT','RIGHT']
# keep track of the turns
turn = 0
# define goals for each floor
goals = [elevator_pos[elevator_floor.index(f)] for f in xrange(nb_elevators)]
goals.append(exit_pos)
print >> sys.stderr, goals

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    # ignore clones
    if clone_floor == -1:
        print 'WAIT'
    else:
        goal = goals[clone_floor]

    # save start position
    if clone_floor == 0 and turn == 0:
        start = clone_pos
    elif clone_floor > 0:
        start = elevator_pos[elevator_floor.index(clone_floor-1)]
    print >> sys.stderr, 'Start: ', start
    print >> sys.stderr, 'Goal: ', goal
    print >> sys.stderr, 'Clone is on the ', clone_floor, ' floor at position ', clone_pos

    # action: WAIT or BLOCK
    # find direction of the goal
    if goal < clone_pos:
        print 'BLOCK' if clone_pos == start+1 else 'WAIT'
    else:
        print 'BLOCK' if clone_pos == start-1 else 'WAIT'
    turn += 1
