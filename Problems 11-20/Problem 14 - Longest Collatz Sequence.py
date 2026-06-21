
# %%


count_max = 1
number_max = 0

for i in range(1, 1000000, 2):

    number = i
    count_number = 1

    while number != 1:

        if number % 2 == 0:

            number = number/2
            count_number += 1

        else:
            number = 3*number + 1
            count_number += 1
    
    if count_number > count_max:
        number_max = i
        count_max = count_number


print("Número com maior chain", number_max)


