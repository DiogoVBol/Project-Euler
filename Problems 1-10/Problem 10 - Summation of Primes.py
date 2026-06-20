# Summation of Primes

def is_pride(number):

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    i = 3

    while i * i <= number:

        if number % i == 0:
            return False

        i += 2

    return True

max_prime = 0
soma_prime = 0
n = 1

while max_prime < 2000000:

    if n <= 2000000:

        if is_pride(n):
            max_prime = n
            soma_prime += n
            n += 1
        else:
            n += 1

    else:
        break


print(max_prime)
print(soma_prime)