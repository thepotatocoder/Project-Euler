
def is_palindrome(number):
    """
    Checks if a number is a palindrome
    """

    digits = []
    while number != 0:
        digits.append(number%10)
        number //= 10

    while len(digits) > 1:
        if digits[0] != digits[-1]:
            return False
        digits.pop()
        digits.pop(0)
    return True

def largest_palindrome(numdigits):
    """
    Returns the biggest palindrome product of two numbers both with 'a' digits
    """

    start = 10**(numdigits - 1)
    end = 10**numdigits - 1
    now = end

    biggest = 0

    while now > start:
        if is_palindrome(now*now) and now*now > biggest:
            biggest = now*now
        for element in range(start, end):
            if is_palindrome(now * element) and now*element > biggest:
                biggest = now * element
        now -= 1
    return biggest

print(largest_palindrome(3))
