def pesquisa_binaria(lista, item):
    baixo = 0                           #baixo é o menor index
    alto = len(lista) - 1               #alto é o maior index

    while baixo <= alto:
        meio = (baixo + alto) // 2      #para encontrar o meio precisa dividir a soma do index maior e menor por 2
        chute = lista[meio]             #aqui checa se o item é igual ao item desejado
        if chute == item:
            return meio                 #se for o item desejado retorna o index dele
        if chute > item:                #senão continua a procura
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = ['diego', 'gabi', 'isabelle', 'christianne', 'junior']
minha_lista.sort()                      #para a pesquisa binária funcionar a lista precisa estar ordenada
print(minha_lista)
print(pesquisa_binaria(minha_lista, 'isabelle'))

print(pesquisa_binaria(minha_lista, 'Diego'))