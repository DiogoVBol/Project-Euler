# %%

import inflect

p = inflect.engine()

soma = 0

for i in range(1,1000+1):

    word = p.number_to_words(i)
    word = word.replace(" ", "").replace("-", "")
    soma += int(len(word))

print(soma)

