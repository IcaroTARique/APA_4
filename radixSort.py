#!/usr/bin/python3.5

def maximo(listaEntrada):
    global indiceDoMaior
    maior = listaEntrada[0]
    for i in range (1,len(listaEntrada)-1):
        if maior < listaEntrada[i]:
            maior = listaEntrada[i]
            indiceDoMaior = i
            print("INDICE DO MAIOR",indiceDoMaior)
            print("MAIOR",maior)

    return maior

def countingSort(listaEntrada,listaOcorrencias,listaOrdenada,exp):

    listaOrdenada = [0] * (len(listaEntrada))
    listaOcorrencias = [0] * (10)

    for i in range(0, len(listaEntrada)):
        index = (int(listaEntrada[i]/exp))
        print("EXP\t",exp)
        print("ARRAY\t",listaEntrada)
        print("INDICE\t", index)
        listaOcorrencias[ int((index)%10) ] += 1

    for i in range(1,10):
        listaOcorrencias[i] += listaOcorrencias[i-1]
        print("CHEGUEEEI AQUI, BILOOORA, ", i ," VEZES")

    print("SAÍ, FRESCO!!")

    i = len(listaEntrada)-1
    while i>=0:
        index = (listaEntrada[i]/exp)
        print("RAMO RÊ: ",int(index)%10)
        listaOrdenada[ listaOcorrencias[int((index)%10) ] -1] = listaEntrada[i]
        print("AQUI É BOM DEMAIS, CUMPADI")
        listaOcorrencias[ int((index)%10) ] -= 1
        i -= 1


    i = 0
    for i in range(0,len(listaEntrada)):
        listaEntrada[i] = listaOrdenada[i]
    print('\033[05;31m',"SAINDO DO countingSort",'\033[00;37m')

def radixSort(listaEntrada,listaOcorrencias,listaOrdenada):
    #Função que procura, acha e retorna o maior numero, para sabermos
    #a quantidade de digitos
    Maior = maximo(listaEntrada)

    #Faz o conunting Sort para cada digito, vale notar que no lugar de passar
    #o digito, a variavel que é passada, e essa variável é 10^i onde i é o numero atual
    exp = 1
    while Maior/exp > 1:
        print("\t=====> \tMAIOR\t ::\t",Maior)
        print("\t=====> \tEXP\t ::\t",exp)
        print("\t=====> \tMaior/exp ::\t",Maior/exp)
        countingSort(listaEntrada, listaOcorrencias, listaOrdenada,exp)
        exp *= 10

# __MAIN__
listaEntrada = [0,211,144,754,125,678]
print(len(listaEntrada))
listaOcorrencias = [0] * (10)
listaOrdenada = []
listaString = []

maior = maximo(listaEntrada)
print("MAIOR ELEMENTO",maior)
print("INDICE DO MAIOR",indiceDoMaior)

for i in range ( len(listaEntrada)):
    listaOrdenada.append(0)

print(listaOrdenada)
radixSort(listaEntrada,listaOcorrencias,listaOrdenada)

print(listaOrdenada)
print(listaEntrada)