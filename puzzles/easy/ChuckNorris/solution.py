import sys, math, re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = raw_input()
binary = ''.join(format(ord(s),'b').rjust(7,'0') for s in MESSAGE)

gr = [m.group(0) for m in re.finditer(r'(\d)\1*', binary)]

answer = ''
for i,s in enumerate(gr):
    if '1' in s:
        answer += '0 '
    elif '0' in s:
        answer += '00 '
    answer += '0'*len(s)
    if i != len(gr)-1:
        answer += ' '

print answer
