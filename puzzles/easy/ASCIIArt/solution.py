L = int(raw_input())
H = int(raw_input())
T = raw_input().lower()
ROW = [raw_input() for i in xrange(H)]
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'.lower()

ind = [chars.find(letter) if chars.find(letter) != -1 else len(chars)-1
       for letter in T]

for j in xrange(H):
    print ''.join([ROW[j][i*L:i*L+L] for i in ind])
