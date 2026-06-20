# Sum Square Difference

quadrado_valores = 0

for i in range(1,101):
    quadrado_valores += i ** 2

valores_quadrado = 0

for i in range(1,101):
    valores_quadrado += i

diff = (valores_quadrado ** 2) - quadrado_valores

print("A diferença é de", diff)