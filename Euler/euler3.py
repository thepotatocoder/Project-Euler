from __future__ import print_function

def biggest_prime_number(num):
    """
    Return list of prime numbers that factorize num
    """
    biggest = 0
    i = 2
    while True:
        i = 2
        while num % i != 0:
            i += 1
        print(i)
        if i > biggest:
            biggest = i
        num = num // i
        if num == 1:
            break
    return biggest

print(biggest_prime_number(600851475143))
