N = int(raw_input())
Pi = [int(raw_input()) for i in xrange(N)]

Pi.sort()
diff = [abs(Pi[i+1] - Pi[i]) for i in xrange(N-1)]
answer = min(diff)

print answer
