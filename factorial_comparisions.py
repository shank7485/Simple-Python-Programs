def fact_DPish(n):
    if n == 0:
        print "1"
    else:
        temp = 1
        for i in range(1, n+1):
            temp = temp * i
        print temp


def fact_recursion(n):
    """
    Causes RuntimeError: maximum recursion depth exceeded 
    For higher 'n'
    """
    if n == 0:
        return 1
    else:
        return n * fact_recursion(n-1)

def fact_tailrecursion(n, feeder_value = 1):
    """
    Causes RuntimeError: maximum recursion depth exceeded
    For higher 'n'
    """
    if n == 0:
        return feeder_value
    else:
        return fact_tailrecursion(n - 1, feeder_value * n)

input = int(raw_input())
fact_DPish(input)
print fact_tailrecursion(input)
print fact_recursion(input)


