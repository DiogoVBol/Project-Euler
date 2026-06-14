# 10 001st Prime

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


n_pride = 0
pride_10001 = 0

n = 1

while n_pride < 10001:

    if is_pride(n):
        pride_10001 = n
        n_pride += 1
        n += 1

    else:
        n += 1

print(pride_10001)
