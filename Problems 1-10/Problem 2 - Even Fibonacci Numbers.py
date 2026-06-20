# Even Fibonacci Numbers (2)

numbers = [1,2]

while numbers[-1] < 4000000:
    new_number = numbers[-1] + numbers[-2]
    numbers.append(new_number)
    

somatorio = 0

for i in numbers:
    if i % 2 == 0:
        somatorio += i

print(somatorio)
