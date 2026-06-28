# %%


def calcula_fatorial(number):

    fatorial = 1

    for i in range(1,number+1):
        fatorial = fatorial * i

    return fatorial


def comb(n,k):

    fat_n = calcula_fatorial(n)

    fat_k = calcula_fatorial(k)

    diff = n-k

    fat_diff = calcula_fatorial(diff)

    total = fat_n / (fat_k*(fat_diff))

    return total


# Em um grid 20x20 temos 40 movimentos
# nesses 40 movimento obrigatóriamente terá 20 direitas e 20 para baixo

print(comb(40,20)) 




