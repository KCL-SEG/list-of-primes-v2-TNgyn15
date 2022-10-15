"List of prime numbers generator."

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Invalid input please enter a number greater than 0")
    list = []
    i = 2
    while len(list) < number_of_primes:
        if isPrime(i):
            list.append(i)
        i += 1
    return list
