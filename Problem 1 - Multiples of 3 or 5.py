# Find the sum of all the multiples of 3 or 5 below 1000 (1)

number = 1000

somador = 0

for i in range(0,number):

    if (i % 3 == 0) | (i % 5 == 0):
        print("i",i)
        somador = somador + i
        print("somador", somador)

print(somador)