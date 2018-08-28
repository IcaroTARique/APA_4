#!/usr/bin/python3.5

def countingSort(lista, listaOcorrencias, listaOrdenada):

    explicaCountSort1()
    for i in range(len(lista)): #Não era pra ir ate len(lista)-1 ?
        listaOcorrencias[lista[i]] = listaOcorrencias[lista[i]] + 1
    print('OCORRENCIAS :: ','\033[34m',listaOcorrencias,'\033[0;0m')


    explicaCountSort2()
    for i in range(1, len(listaOcorrencias)):
        listaOcorrencias[i] = listaOcorrencias[i]+listaOcorrencias[i-1]
    print('OCORRENCIAS SOMADAS :: ','\033[34m',listaOcorrencias,'\033[0;0m')

    explicaCountSort3()
    for i in range(0,len(lista)):
        print(i)
        print("ELEMENTO DO ARRAY PERCORRIDO ANTES DO INCREMENTO",listaOcorrencias[lista[i]])
        print("ELEMENTO INDEX DO (ELEMENTO ARRAY PERCORRIDO)", lista[i] )
        listaOrdenada[listaOcorrencias[lista[i]]-1]= lista[i]
        print("ELEMENTO ORDENADO ::::::::::::::::::::::::::::::::::::: ",listaOrdenada[listaOcorrencias[lista[i]]-1])
        #listaOrdenada[listaOcorrencias[lista[i]]]
        listaOcorrencias[lista[i]] = listaOcorrencias[lista[i]]-1

        print("ELEMENTO DO ARRAY PERCORRIDO DEPOIS DO DECREMENTO",listaOcorrencias[lista[i]])
        print('------------------------------------------------------------',listaOrdenada)

def explicaGeral():
    print('\033[33m'+"O CountSort funciona da seguinte maneira : \n"
        "A lista de entrada passa por algumas etapas até sair complentamente ordenada como esperado,\n"
        "a seguir veremos passo-a-passo as manipulações na qual a lista passará até sair completa-\n"
        "mente ordenada."'\033[0;0m')

def explicaTamanhodoMaiorElemento():
    print('\033[33m'+
        "Quando recebemos uma lista de entrada nós não temos noção de quem é o maior elemento,\n"
        "portanto percorremos toda a lista em busca dele e assim criarmos uma outra lista chamada\n"
        "de listaOcorrencias, com o tamanho igual a do maior número encontrado, onde ficarão\n"
        "armazenados a quantidade de ocorrências de um numero específico na lista."+'\033[0;0m')

def explicaCountSort1():
    print('\033[33m'+
        "Ao percorrermos a lista devemos armazenar a quantidade de ocorrencias dos números na\n"
        "lista listaOcorrencias, isso é feito incrementando o valor em cada índice correspon-\n"
        "dente ao valor encontrado na lista de nome lista"+"\033[0;0m")

def explicaCountSort2():
    print('\033[33m'+
        "Agora, manipulamos a lista de nome listaOcorrencias somando o valor do índice com o \n"
        "seu anterior"
    +"\033[0;0m")

def explicaCountSort3():
        print('\033[33m'+
        "A parte mais complicada de entender é agora, mas vamos explicar:\n"
        "Temos que a quantidade de ocorrencias de um número está expressa na listaOcorrencias\n"
        "portanto, temos apenas que, percorrendo a lista de entrada de dados, verificar que a\n"
        "listaOrdenada, que foi criada pra receber a lista já ordenada, recebe o elemento da \n"
        "lista de entrada, porém o índice da listaOrdenada é o elemento da listaOcorrencias que\n"
        "tem como índice o valor de lista naquela iteração.\n"
        "Após essa etapa, decrementamos a ocorrência da listaOcorrencias no índice referente ao\n"
        "valor atual da lista de entrada"
    +"\033[0;0m")


explicaGeral()
lista = [1,4,1,2,7,5,0,3,6,9,0]
print("lista de numeros de entrada -->"+'\033[31m',lista,'\033[0;0m')
#print("Tamanho da Lista", len(lista))
listaOcorrencias = []
listaOrdenada = []


#For to get the higher number in the sequence
explicaTamanhodoMaiorElemento()
maior = lista[0]
for i in range (1,len(lista)):
    if maior < lista[i]:
        maior = lista[i]
        print("MAIOR NUMERO --> ", maior)

#list of indexes to count the numbers ammount
for i in range(0,maior+1):
    listaOcorrencias.append(0)

print("criação da lista listaOcorrencias -->"+'\033[31m', listaOcorrencias,'\033[0;0m')

#Ordered list created to be displayed at the end
for i in range(0,len(lista)):
    listaOrdenada.append(0)

countingSort(lista,listaOcorrencias,listaOrdenada)
print('\033[31m',listaOrdenada,'\033[0;0m')
print('\033[05;31m','------------------------------FIM------------------------------','\033[00;37m')