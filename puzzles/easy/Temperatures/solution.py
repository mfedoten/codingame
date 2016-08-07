import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())  # the number of temperatures to analyse
TEMPS = raw_input()   # the N temperatures expressed as integers ranging from -273 to 5526

minTEMP = 5527
try:
    T = [int(t) for t in TEMPS.split(' ')]
    for t in T:
        print >> sys.stderr, t
        if abs(t) < minTEMP:
            minTEMP = abs(t)
            result = t
            # print >> sys.stderr, "min for now {0}".format(minTEMP)
        elif abs(t) == minTEMP:
            result = max(result,t)
            # print >> sys.stderr, "Here"
        # print >> sys.stderr, "res: {0}".format(result)
except:
    result = 0
print result
