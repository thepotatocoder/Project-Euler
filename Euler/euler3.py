
def biggest_prime_number(num):
    """
    Return list of prime numbers that factorize num
    """
    biggest = 0

    while num != 1:
        i = 2
        while num % i != 0:
            i += 1
        if i > biggest:
            biggest = i
        num //= 1

    return biggest

print(biggest_prime_number(600851475143))
