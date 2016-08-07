import sys

road = int(raw_input())        # the length of the road before the gap.
gap = int(raw_input())         # the length of the gap.
platform = int(raw_input())    # the length of the landing platform.

# game loop
while 1:
    speed = int(raw_input())   # the motorbike's speed.
    coordX = int(raw_input())  # the position on the road of the motorbike.

    print >> sys.stderr , coordX
    print >> sys.stderr, platform
    print >> sys.stderr, road
    if coordX < road-1:
        if speed < gap+1:
            print "SPEED"
        elif speed == gap+1:
            print "WAIT"
        else:
            print "SLOW"
    elif coordX == road-1:
        print "JUMP"
    else:
        print "SLOW"

