def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        elemento_meio = lista[meio]

        if elemento_meio == alvo:
            return meio
        elif elemento_meio < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return - 1

lista_ordenada = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
alvo = 50
resultado = busca_binaria(lista_ordenada, alvo)

if resultado != -1:
    print("O elemento {} foi encontrado no índice {}.".format(alvo, resultado))
else:
    print("O elemento {} não foi encontrado na lista.".format(alvo))