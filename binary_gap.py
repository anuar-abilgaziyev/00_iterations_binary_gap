'''
Function takes an integer and returns longest binary gap. 
For example, given N = 1041 the function should return 5, 
because N has binary representation 10000010001 and 
so its longest binary gap is of length 5. 

Given N = 32 the function should return 0, 
because N has binary representation '100000' and thus no binary gaps.
'''
def solution(N):
    bin_num = bin(N)[2:]
    counter = 0
    long_bin_gap = 0

    for c in bin_num:
        if c == '1':
            if counter >= long_bin_gap:
                long_bin_gap = counter
            counter = 0
        elif c == '0':
            counter += 1
    return long_bin_gap
