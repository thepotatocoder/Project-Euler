
def fibonacci(toplimit):
    """
    Generator for fibonacci sequence
    """
    first = 0
    last = 1
    while first + last < toplimit:
        yield first + last
        temp = first
        first = last
        last += temp



print(sum(x for x in fibonacci(4000000) if x%2 == 0))
