while True:
    try:
        notas = []
        while len(notas) < 2:
            nota = float(input())
            if nota < 0 or nota > 10:
                print('nota invalida')
            else:
                notas.append(nota)
        print('media = {:.2f}'.format(sum(notas) / len(notas)))
        while True:
            print('novo calculo (1-sim 2-nao)')
            x = int(input())
            if x == 1 or x == 2:
                break
        if x == 2:
            break
    except EOFError:
        break
