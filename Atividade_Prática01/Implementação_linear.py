def busca_linear(lista, alvo):
    for i, elemento in enumerate(lista):
        if elemento == alvo:
            return i
    return -1

minha_lista = [3, 18, 75, 30, 150, 17, 99]
valor_procurado = 75

resultado = busca_linear(minha_lista, valor_procurado)

if resultado != -1:
    print("O valor {} foi encontado na posição {}.".format(valor_procurado, resultado))
else:
        print("O alor {} não foi encontrado na lista.".format(valor_procurado))