import sys

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]


def midpt((a,b)):
    ''' returns midpoint of the (a,b)-interval'''
    return (a + b)/2


def get_intervals(x_interval,y_interval,x,y,loc):
    if "R" in loc:
        x_interval = (x+1,x_interval[1])
    elif "L" in loc:
        x_interval = (x_interval[0], x-1)

    if "U" in loc:
        y_interval = (y_interval[0], y-1)
    elif "D" in loc:
        y_interval = (y+1, y_interval[1])

    return x_interval, y_interval


# game loop
x_inter, y_inter = (0,w-1), (0,h-1)
x, y = x0, y0
while True:
    # the direction of the bombs from batman's current location
    # (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = raw_input()
    x_inter, y_inter = get_intervals(x_inter,y_inter,x,y,bomb_dir)
    x = midpt(x_inter)
    y = midpt(y_inter)

    # the location of the next window Batman should jump to.
    print str(x)+" "+str(y)

