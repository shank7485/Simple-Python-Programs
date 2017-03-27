"""
HackerRank: Algorithms::Implementation::Cut the sticks
"""


def cutter(inp, times):
    times = len(inp)
    for i in range(0, times):
        if len(inp) > 0:
            print len(inp)
            minimum = min(inp)

            for i in range(0, len(inp)):
                inp[i] -= minimum

            output = [i for i in inp if i > 0]
            inp = output

number = int(raw_input())

inp = [int(i) for i in raw_input().split()]

cutter(inp, number)
