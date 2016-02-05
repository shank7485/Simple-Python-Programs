"""
HackerRank Interview
"""


def fibo1(n):
    a = []
    a.append(0)
    a.append(1)
    if n == 0:
        return 0
    else:
        for i in range(2, n+1):
            a.append(a[i-1] + a[i-2])
        return a[len(a) - 1]

lst = []
flag = True
while flag == True:
    try:
        value = raw_input()
        if value != "":
            lst.append(int(value))
    except (EOFError):
        flag = False

for i in lst:
    print fibo1(i)
