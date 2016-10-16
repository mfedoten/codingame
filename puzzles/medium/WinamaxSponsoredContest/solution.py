import sys
from collections import deque

# ---------- read inputs ----------
# cards of player 1
n = int(raw_input())
cards1 = deque([raw_input()[:-1] for i in xrange(n)])
pile1 = []
# cards of player 2
m = int(raw_input())
cards2 = deque([raw_input()[:-1] for i in xrange(m)])
pile2 = []

# map card names to values
cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
cards.update({str(k):k for k in range(1,11)})

# print >> sys.stderr, 'Cards in the beginning:'
# print >> sys.stderr, ' '.join(cards1)
# print >> sys.stderr, ' '.join(cards2)

# ---------- main part ----------
rounds = 0  # count number of rounds
while True:
    # print >> sys.stderr, '\nRound %r' % rounds

    # battle: each player pulls out the top card
    try:
        pile1 = [cards1.popleft()]
        pile2 = [cards2.popleft()]
        #  print>>sys.stderr, 'Fighting cards: %r vs %r' % (pile1[-1],pile2[-1])
    except IndexError:
        # if one of the players ran out of cards,
        # stopr the battle and find the winner
        win = 1 if len(cards1) > 0 else 2
        print win, rounds
        break

    # increase rounds
    rounds += 1

    # war
    try:
        while cards[pile1[-1]] == cards[pile2[-1]]:
            for i in xrange(4):
                pile1.append(cards1.popleft())
                pile2.append(cards2.popleft())
    except IndexError:
        print "PAT"
        break

    # determine the outcome: P1 wins or P2 wins
    if cards[pile1[-1]] > cards[pile2[-1]]:
        #  print >> sys.stderr, 'Player 1 wins'
        cards1 += pile1 + pile2
    elif cards[pile1[-1]] < cards[pile2[-1]]:
        #  print >> sys.stderr, 'Player 2 wins'
        cards2 += pile1 + pile2

    # print players' cards after each round
    # print >> sys.stderr, "1st player's cards: " + " ".join(cards_p1)
    # print >> sys.stderr, "2nd player's cards: " + " ".join(cards_p2)
