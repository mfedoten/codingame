import sys
from collections import deque

# read inputs
n = int(raw_input())  # the number of cards for player 1
cardp_1 = deque([raw_input() for i in xrange(n)])  # the n cards of player 1
m = int(raw_input())  # the number of cards for player 2
cardp_2 = deque([raw_input() for i in xrange(m)])  # the m cards of player 2

# map card names to values
cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
cards.update({str(k):k for k in range(1,11)})


# WAR
def war(cardp_1, cardp_2, add1, add2):
    print >> sys.stderr, 'War'
    # if player one has less than 3 cards: pat
    # otherwise put three first cards and play with the 4th
    try:
        for i in xrange(4):
            add1.append(cardp_1.popleft())
        ind_1 = add1[-1]
        print >> sys.stderr, '\t Player 1: ' + ind_1
    except:
        return True
    # Same for player 2
    try:
        for i in xrange(4):
            add2.append(cardp_2.popleft())
        ind_2 = add2[-1]
        print >> sys.stderr, '\t Player 2: ' + ind_2
    except:
        return True

    if ind_1[:-1] > ind_2[:-1]:
        print >> sys.stderr, '\t Player 1 wins'
        cardp_1.extend(add1)
        cardp_1.extend(add2)
    elif ind_2[:-1] > ind_1[:-1]:
        print >> sys.stderr, '\t Player 2 wins'
        cardp_2.extend(add1)
        cardp_2.extend(add2)
    else:
        war(cardp_1, cardp_2, add1, add2)
    return False

# ---------------------------------------------
print >> sys.stderr, 'Cards in the beginning:'
print >> sys.stderr, ' '.join(cardp_1)
print >> sys.stderr, ' '.join(cardp_2)

rounds = 0  # count number of rounds
pat = False
while True:
    # increase rounds
    rounds += 1
    print >> sys.stderr, '\nRound %r' % rounds
    # easch player pulls out the top card
    ind1 = cardp_1.popleft()
    ind2 = cardp_2.popleft()
    print >> sys.stderr, 'Fighting cards: %r vs %r' % (ind1,ind2)
    # Determine the outcome: P1 wins, P2 wins or war
    if cards[ind1[:-1]] > cards[ind2[:-1]]:
        print >> sys.stderr, 'Player 1 wins'
        cardp_1.extend([ind1,ind2])
    elif cards[ind1[:-1]] < cards[ind2[:-1]]:
        print >> sys.stderr, 'Player 2 wins'
        cardp_2.extend([ind1,ind2])
    else:
        # pass the decks of both players and two played cards
        # check if a player ran out of cards during war -> pat
        pat = war(cardp_1,cardp_2,[ind1],[ind2])

    # print players' cards after each round
    print >> sys.stderr, "1st player's cards: " + " ".join(cardp_1)
    print >> sys.stderr, "2nd player's cards: " + " ".join(cardp_2)

    # output result of the game
    if pat:
        res_str = 'PAT'
        break
    elif len(cardp_1) == 0:
        res_str = '2 ' + str(rounds)
        break
    elif len(cardp_2) == 0:
        res_str = '1 ' + str(rounds)
        break

print res_str

