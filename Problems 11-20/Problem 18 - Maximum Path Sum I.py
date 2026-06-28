# %%

# A ideia é resolver o problema de baixo para cima, transformando cada número na maior soma possível a partir dele até a base.
# 1. Começar na penúltima linha, pois a última já representa a base do triângulo
# 2. Para cada número da linha atual:
#   Olhar os dois filhos na linha de baixo.
#   Escolher o maior deles.
#   Somar esse maior valor ao número atual.
# 3. Armazenar essas somas em uma nova lista.
# 4. Substituir a linha original por essa nova lista.
# 5. Repetir o processo até chegar ao topo.

lista = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

tamanho_total = len(lista)

for linha in range(tamanho_total-2, 0, -1): # 1.

    lista_nova = []

    for posicao, numero in enumerate(lista[linha]): # 2.

        soma = 0

        if lista[linha+1][posicao] >= lista[linha+1][posicao + 1]:

            soma += numero + lista[linha+1][posicao]

        else:
            
            soma += numero + lista[linha+1][posicao + 1]

        lista_nova.append(soma) # 3.

    lista[linha] = lista_nova # 4.

if lista[1][0] >= lista[1][1]:
    print("Maior soma:", lista[1][0] + 75)

else:
    print("Maior soma:", lista[1][1] + 75)

