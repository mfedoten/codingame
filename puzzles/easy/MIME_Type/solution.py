N = int(raw_input())  # Number of elements which make up the association table.
Q = int(raw_input())  # Number Q of file names to be analyzed.

EXT, MT = zip(*[raw_input().split() for i in xrange(N)])
EXT = [EXT[i].lower() for i in xrange(N)]

# One file name per line.
FNAME = [raw_input().lower() for i in xrange(Q)]

# Check file extensions
for i in xrange(Q):
    if FNAME[i].rpartition('.')[1]:
        try:
            ind = EXT.index(FNAME[i].rpartition('.')[2])
            print MT[ind]
        except ValueError:
            print "UNKNOWN"
    else:
        print "UNKNOWN"
