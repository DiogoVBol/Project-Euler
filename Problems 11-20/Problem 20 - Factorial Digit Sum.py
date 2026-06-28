# %%

factorial_num = 100

value = 1

for i in range(factorial_num,1,-1):
    value = value * i


str_value = str(value)

soma = 0

for i in str_value:
    soma += int(i)

print(soma)