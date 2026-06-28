# %%

number = 2**1000

number_str = str(number)

soma = 0

for i in number_str:
    soma += int(i)

print(soma)