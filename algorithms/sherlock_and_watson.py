# Sherlock and watson

from collections import deque 
line = raw_input()
line_list = line.split()
N = int(line_list[0])
K = int(line_list[1])
Q = int(line_list[2])

line = raw_input()
line_list = line.split()
line_array = map(int,line_list)

deque_list = deque(line_array)
deque_list.rotate(K)
for i in range(0,Q):
    q = input()
    print deque_list[q]