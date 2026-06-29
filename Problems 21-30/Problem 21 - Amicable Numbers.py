

# %%

# A primeira ideia era verificar todos os números menores que n.
# Para cada i de 1 até n-1, verificava se i era divisor.
# Essa abordagem funciona, mas faz muitas verificações desnecessárias (O(n)).

# Na verdade quando faço, por exemplo 36/2 o resultado 18 é um par pois 36/18 é igual a 2
# Basta guardar os dois resultados.
# E não preciso calcular os divisores até o n-1, posso fazer até raiz(n)
# Números antes da raiz sempre tem pares...

# Exemplo pares:
# sqrt(36) = 6
# 1 -------- 36
# 2 -------- 18
# 3 -------- 12
# 4 -------- 9
# 6 -------- 6

def find_divisors(number):

    divisors = []

    sqrt_number = int(round(number ** (1/2),0)) 

    for i in range(1,sqrt_number+1): # Procura até sqrt(number)

        if number % i == 0:

            divisors.append(i)

            par_divisor = number // i # o par do i

            if par_divisor != i and par_divisor != number: # O par não pode ser o próprio i (6-6) - número perfeito e nem pode ser o número final.
                divisors.append(par_divisor)

    return divisors

sum_amicable = 0

for i in range(1,10001):

    all_divisors = sum(find_divisors(i))


    new_divisor = sum(find_divisors(all_divisors))

    if all_divisors != i and i == new_divisor:
        sum_amicable += i

sum_amicable