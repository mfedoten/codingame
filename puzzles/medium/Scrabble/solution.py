import sys

# read inputs
n = int(raw_input())                      # nr. of words
words = [raw_input() for i in xrange(n)]  # dictionary
letters_init = raw_input()                # letters we have

# create py dictionary with price for each letters
pts_for_letter = {'e':1, 'a':1, 'i':1, 'o':1, 'n':1,
                  'r':1, 't': 1, 'l':1, 's':1, 'u':1,
                  'd':2, 'g':2,
                  'b':3, 'c':3, 'm':3, 'p':3,
                  'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
                  'k':5,
                  'j':8, 'x':8,
                  'q':10, 'z':10}

print >> sys.stderr, 'Words in our dictionary: ',', '.join(w for w in words)
print >> sys.stderr, 'Letters we have: ', ' '.join(l for l in letters_init), '\n'

# loop over all words
max_pts = 0
for word in words:
    pts_for_word = 0
    letters = list(letters_init)
    for l in word:
        if l in letters:
            pts_for_word += pts_for_letter[l]
            letters.remove(l)
        else:
            pts_for_word = 0
            break
    if pts_for_word > max_pts:
        out_word = word
        max_pts = pts_for_word

print out_word
