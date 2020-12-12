'''
Takes an integer and returns longest binary gap
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