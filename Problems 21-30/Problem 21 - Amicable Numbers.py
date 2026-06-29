

# %%

def find_divisors(number):

    divisors = []

    for i in range(1,number):

        if number % i == 0:

            divisors.append(i)

    return divisors


sum_amicable = 0

for i in range(1,10000):

    all_divisors = sum(find_divisors(i))


    new_divisor = sum(find_divisors(all_divisors))

    if all_divisors != i and i == new_divisor:
        sum_amicable += i

sum_amicable
