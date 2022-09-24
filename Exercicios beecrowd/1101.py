x, y = map(int, input().split())

while True:
    if x == y:
        break

    if x > y:
        print("Decrescente")
    else:
        print("Crescente")

    x, y = map(int, input().split())