
# %%

triangle_number = 1
divisores = 1

while divisores < 500:

    number_sum = 0
    
    for i in range(0, triangle_number+1):

        number_sum += i

    print("Triangulo number", triangle_number)

    print("Number Sum",number_sum)

    i = 1
    divisores = 0

    # não preciso testar todos os dividores, ex: 36 testar 1,2,3,4,5,6... pois se 36 é divisível por 2 então é por 18 tbm
    # number_sum = 36, i = 2: 2 * 2 = 4 -> 36 % 2 == 0 TRUE -> 2 * 2 == 36 FALSE então incrementa 2 e testa o próximo i que é 3

    while i * i <= number_sum:

        if number_sum % i == 0:

            if i * i == number_sum:
                divisores += 1
            else:
                divisores += 2
        
        i += 1

    print("Total divisors:", divisores)
        
    triangle_number += 1