import sys

# Don't let the machines win. You are humanity's last hope...
# Read the input
width  = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
lines  = [raw_input() for i in xrange(height)]  # width characters, each either 0 or .

# initialize empty string and counters
str_node = ''
y = 0
x = 0

# scan all the rows
while y < height:
    # scan all the columns incide the row
    while x < width:
        if lines[y][x] == '0':
            # if there is a node put its coordinates and check for neighbours
            str_node = str(x) + ' ' + str(y)
            # neighbour on the right
            x2 = lines[y][x+1:].find('0')
            if x2 != -1:
                x2 += x + 1
                str_node += ' ' + str(x2) + ' ' + str(y) + ' '
            else:
                str_node += ' -1 -1'
            # neighbour below
            y3 = "".join(lines[i][x] for i in xrange(y+1,height)).find('0')
            if y3 != -1:
                y3 += y + 1
                str_node += ' ' + str(x) + ' ' + str(y3) + ' '
            else:
                str_node += ' -1 -1'
            # print results for the current node
            print str_node
        x += 1
    y += 1
    x = 0

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
