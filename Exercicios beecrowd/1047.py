h1, m1, h2, m2 = map(int, input().split())

if h1 == h2 and m1 == m2:
    duracao = 24
elif h1 < h2:
    duracao = h2 - h1
else:
    duracao = 24 - h1 + h2

if m1 < m2:
    duracao_min = m2 - m1
else:
    duracao_min = 60 - m1 + m2

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao, duracao_min))    