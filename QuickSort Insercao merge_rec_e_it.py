import random
import time
import copy

intervalo = 0
print 'Programa iniciado, favor aguardar..'


def lista(intervalo):
    return [random.randint(-0, 10000) for i in xrange(intervalo)]


def bubbleSort(listab):
    for bolhinha in range(len(listab)-1,0,-1):
        for i in range(bolhinha):
            if listab[i]>listab[i+1]:
                #No Python, nao precisa fazer com variavel temp
                #Pode ser feita atribuicao simultanea. Ex.: a, b = b, a
                #Mas fiz dessa forma para facilitar fazer o codigo
                #em outra linguagem, se for o caso.
                temp = listab[i]
                listab[i] = listab[i+1]
                listab[i+1] = temp

    

def insertionSort(lista1):
    for index in range(1,len(lista1)):
        valor_atual= lista1[index]
        posicao = index
        while posicao > 0 and lista1[posicao-1] > valor_atual:
            lista1[posicao] = lista1[posicao-1]
            posicao = posicao-1

        lista1[posicao] = valor_atual
    return lista1


    
def mergeSort(lista):
#    print("Divisao ",lista)
    if len(lista)>1:
        meio = len(lista)//2
        ladoesquerdo = lista[:meio]
        ladodireito = lista[meio:]
        
        mergeSort(ladoesquerdo)
        mergeSort(ladodireito)

        i=0
        j=0
        k=0
        while i < len(ladoesquerdo) and j < len(ladodireito):
            if ladoesquerdo[i] < ladodireito[j]:
                lista[k]=ladoesquerdo[i]
                i=i+1
            else:
                lista[k]=ladodireito[j]
                j=j+1
            k=k+1

        while i < len(ladoesquerdo):
            lista[k]=ladoesquerdo[i]
            i=i+1
            k=k+1

        while j < len(ladodireito):
            lista[k]=ladodireito[j]
            j=j+1
            k=k+1
#    print("Juntando ",lista)
    return lista



#Versao iterativa do Mergesort / etapa da ordenacao
def merge(a, left, mid, right):
    copy_list = []
    i, j = left, mid + 1
    ind = left
    
    while ind < right+1:
#se o vetor da esquerda terminar o merge, copiar do lado direito
        if i > mid:
            copy_list.append(a[j])
            j +=1
#copiar o do lado esquerdo, se o direito terminar o merge
        elif j > right:
            copy_list.append(a[i])
            i +=1
#Verifica se o vetor da direita eh menor que o da esquerda
        elif a[j] < a[i]:
            copy_list.append(a[j])
            j +=1
        else:
            copy_list.append(a[i])
            i +=1
        ind +=1
        
    ind=0
    for x in (xrange(left,right+1)):
        a[x] = copy_list[ind]
        ind += 1


#Versao Iterativa do Algorithm Merge Sort (cont)        
def merge_sort_iterative(list_):
    fator = 2
    temp_mid = 0
    while 1:
        index = 0
        left = 0
        right = len(list_) - (len(list_) % fator) - 1
        mid = (fator / 2) - 1
        
        #Vetor auxiliar para subdivisoes do merge
        while index < right:
            temp_left = index
            temp_right = temp_left + fator -1
            mid2 = (temp_right +temp_left) / 2
            merge (list_, temp_left, mid2, temp_right)
            index = (index + fator)
        

        if len(list_) % fator and temp_mid !=0:
#faz o merge do subvetor para depois fazer o merge com o vetor final
            merge(list_, right +1, temp_mid, len(list_)-1)
            #Update the pivot
            mid = right
        #Aumenta o fator
        fator = fator * 2
        temp_mid = right
       
#Faz o merge final, unindo subvetores criados pela subdivisao
#do fator do vetor principal
        if fator > len(list_) :
            mid = right
            right = len(list_)-1
            merge(list_, 0, mid, right)
            break



#Ordena por Quicksort  
def quickSort(lista):
   ajudaquickSort(lista,0,len(lista)-1)

def ajudaquickSort(lista,primeiro,ultimo):
   if primeiro<ultimo:

       pontodivisao = particao(lista,primeiro,ultimo)

       ajudaquickSort(lista,primeiro,pontodivisao-1)
       ajudaquickSort(lista,pontodivisao+1,ultimo)

#O Quick Sort primeiro seleciona um valor, chamado de valorpivo 
#Selecionamos o primeiro valor como pivo
def particao(lista,primeiro,ultimo):
   valorpivo = lista[primeiro]

#Seleciona-se os marcadores para depois dividir
   marcaesquerda = primeiro+1
   marcadireita = ultimo

#Vai deslocando ate achar um valor maior que o pivo
   feito = False
   while not feito:

       while marcaesquerda <= marcadireita and lista[marcaesquerda] <= valorpivo:
           marcaesquerda = marcaesquerda + 1

# Rearranja marcas (chaves) de modo que as "menores" precedam "maiores"
# Depois ordena as duas sublistas de chaves menores e maiores recursivamente
# ate que a lista completa se encontre ordenada.
       while lista[marcadireita] >= valorpivo and marcadireita >= marcaesquerda:
           marcadireita = marcadireita -1

       if marcadireita < marcaesquerda:
           feito = True
       else:
           temp = lista[marcaesquerda]
           lista[marcaesquerda] = lista[marcadireita]
           lista[marcadireita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[marcadireita]
   lista[marcadireita] = temp


   return marcadireita



#print "Lista original:"
#print (lista_aleatoria)
print "Tamanho do intervalo ; Tempo: BubbleSort ; InsertSort ; MergeSort (iterativo) ; MergeSort (recursivo); QuickSort"
vc = [100,400,1000,4000,10000]

for i in range(0, (len (vc))):

    intervalo = vc[i]

    lista_aleatoria = lista(intervalo)
# Queremos trabalhar na copia da lista e nao na lista original, por isso "copy"/"deepcopy"
    lms = copy.deepcopy(lista_aleatoria) #lms - Lista ordenada por MergeSort (vai ser)
    inicio3 = time.time()
    mergeSort(lms)
    fim3 = time.time()
    tempoms = (fim3 - inicio3) #Tempo que demora para executar o IS


    lis = copy.deepcopy(lista_aleatoria)  #lis - Lista ordenada por Insertionsort (vai ser)
    inicio2 = time.time()
    insertionSort(lis)
    fim2 = time.time()
    tempois = (fim2 - inicio2) #Tempo que demora para executar o IS

    lbs = copy.deepcopy(lista_aleatoria)   #lbs - Lista ordenada por Bubblesort (vai ser)
    inicio = time.time()
    bubbleSort(lbs)
    fim = time.time()
    tempobs = (fim - inicio) #Tempo que demora para executar o BS

    lqs = copy.deepcopy(lista_aleatoria)   #lqs - Lista ordenada por Quicksort (vai ser)
    inicio = time.time()
    quickSort(lqs)
    fim = time.time()
    tempoqs = (fim - inicio) #Tempo que demora para executar o QS

    lmsi = copy.deepcopy(lista_aleatoria) #lms - Lista ordenada por MergeSort iterativo(vai ser)
    inicio4 = time.time()
    merge_sort_iterative(lmsi) #Ordena Items
    fim4 = time.time()
    tempomsi = (fim4 - inicio4) #Tempo que demora para executar o IS

    print str(intervalo) + " ; " + str(tempobs) + " ; " + str(tempois) + " ; " + str(tempomsi) + " ; " + str(tempoms) + " ; " + str(tempoqs)
