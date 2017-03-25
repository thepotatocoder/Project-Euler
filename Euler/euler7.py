
def nthprime(nth):
    """
    Returns the nth prime in a very, very 
    """

    #number 1 counts as prime
    nums = [1]
    i = 2

    while len(nums) <= nth:
        prime = True
        for num in nums:
            if i % num == 0 and num is not 1:
                prime = False
        if prime:
            nums.append(i)
            print(i)
        i += 1
    return nums[-1]
