
def factorize(num):
    """
    Factorizes a number, then returns the list of factor tuples
    defined by (number, times it appears)
    """
    factors = {}
    divide = 2
    while num != 1:
        while num % divide == 0:
            num //= divide
            if factors.get(divide) != None:
                factors[divide] += 1
            else:
                factors[divide] = 1
        divide += 1
    #print(factors)
    return factors

def smallest_divisible_number(num):
    """
    Returns the smallest number that can be divided by each of the numbers from
    1 to num without any remainder.
    """

    factdict = {}
    count = 2
    while count <= num:
        for number, times in factorize(count).items():
            #print('n:' + str(number) + '; t: ' + str(times))
            if number in factdict.keys():
                if factdict[number] < times:
                    factdict[number] = times
            else:
                factdict[number] = times

        count += 1

    val = 1
    for number, times in factdict.items():
        val *= number**times
    return val

print(smallest_divisible_number(20))