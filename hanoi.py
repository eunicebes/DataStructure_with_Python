def hanoi(n, from_peg, to_peg, use_peg):
    if n > 0:
        hanoi(n-1, from_peg, use_peg, to_peg)
        if from_peg:
            to_peg.append(from_peg.pop())
        hanoi(n-1, use_peg, to_peg, from_peg)

from_peg = [4, 3, 2, 1]
to_peg = []
use_peg = []
hanoi(len(from_peg), from_peg, to_peg, use_peg)
print(to_peg)