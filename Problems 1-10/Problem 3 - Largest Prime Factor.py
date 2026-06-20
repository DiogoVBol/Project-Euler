# Largest Prime Factor (3)

def is_prime(number):

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


number = 600851475143

number_raiz = int(number ** 0.5)

if number_raiz % 2 == 0:
    number_raiz -= 1

for i in range(number_raiz, 1, -2):

    print(i)

    if number % i == 0:

        if is_prime(i):

            print("Maior fator primo:", i)

            break

# Segunda opção mais eficiênte

number = 600851475143

number_raiz = int(number ** 0.5)

for i in range(number_raiz, 1, -1):

    if number % i == 0:

        other = number // i

        if is_prime(other):
            print("Maior fator primo:", other)
            break

        if is_prime(i):
            print("Maior fator primo:", i)
            break

