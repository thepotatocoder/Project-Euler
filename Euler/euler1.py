
def multiples_of_3_and_5(maximum):
    """
    Generator for the all multiples of 3 and 5
    """
    num = 0
    while num < maximum:
        if num%3 == 0 or num%5 == 0:
            yield num
        num += 1

print(sum(multiples_of_3_and_5(1000)))

