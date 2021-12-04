import math as m
from os import pardir, replace
class board:
    def __init__(self,numbers):
        self.numbers = numbers
        self.scores = [0]*10
    def update(self,n):
        for i, num in enumerate(self.numbers):
            if num == n:
                self.numbers[i] += 100
                self.scores[i%5] += 1
                self.scores[m.floor(i/5) + 5 ] += 1
    def check(self):
        for s in self.scores:
            if s == 5 :
                return True
        return False


def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]

with open("input.txt") as f:
    nums = [4,77,78,12,91,82,48,59,28,26,34,10,71,89,54,63,66,75,15,22,39,55,83,47,81,74,2,46,25,98,29,21,85,96,3,16,60,31,99,86,52,17,69,27,73,49,95,35,9,53,64,88,37,72,92,70,5,65,79,61,38,14,7,44,43,8,42,45,23,41,57,80,51,90,84,11,93,40,50,33,56,67,68,32,6,94,97,13,87,30,18,76,36,24,19,20,1,0,58,62]
    #nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    r = f.read().split()
    r = [int(n) for n in r]
    boards = chunks(r,25)
    l = len(boards)
    boar_objs= []
    for i in range(l):
        b = board(boards[i])
        boar_objs.append(b)

    k = 0
    win = False
    win_board = []
    final = 0
    while win is False:
        for n in nums:
            if win is True:
                break
            for b in boar_objs:
                b.update(n)
                if b.check() == True:
                    final = n
                    print(b.numbers)
                    print(b.scores)
                    win_board = b.numbers
                    win = True
                    break
    x = 0
    print(final)
    for i , n in enumerate(win_board):
        if n - 100 < 0:
            x += n
    print(x*final)



