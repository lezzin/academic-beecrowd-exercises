A, B = map(int, input().split())

if A == B:
    duracao = 24
elif A < B:
    duracao = B - A
else:
    duracao = 24 - A + B

print("O JOGO DUROU {} HORA(S)".format(duracao))