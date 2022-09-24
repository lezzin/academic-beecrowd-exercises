valores = []

for i in range(100):
    valores.append(int(input()))

maior_numero = max(valores)
posicao_numero = valores.index(maior_numero)

print(maior_numero)
print(posicao_numero + 1)