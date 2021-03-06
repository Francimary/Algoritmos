import random
import time
import copy


#Criacao da lista
lista_aleatoria = [random.randint(-0, 11000) for c in range(1000)]

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



"""
MergeSort Implementations Recursive & Iterative
Name: Jorge Valdivia
"""
 
def merge(a, left, mid, right):
    """
    Funcao Merge
    """
    #Copy array
    copy_list = []
    i, j = left, mid + 1
    ind = left
    
    while ind < right+1:
        
        #if left array finish merging, copy from right side
        if i > mid:
            copy_list.append(a[j])
            j +=1
        #if right array finish merging, copy from left side
        elif j > right:
            copy_list.append(a[i])
            i +=1
        #Check if right array value is less than left one
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

def merge_sort_iterative(list_):
    """
    Versao Iterativa do Algorithm Merge Sort 
    """
    factor = 2
    temp_mid = 0
    #Main loop to iterate over the array by 2^n.
    while 1:
        index = 0
        left = 0
        right = len(list_) - (len(list_) % factor) - 1
        mid = (factor / 2) - 1
        
        #Auxiliary array to merge subdivisions
        while index < right:
            temp_left = index
            temp_right = temp_left + factor -1
            mid2 = (temp_right +temp_left) / 2
            merge (list_, temp_left, mid2, temp_right)
            index = (index + factor)
        
        #Chek if there is something to merge from the remaining
        #Sub-array created by the factor
        if len(list_) % factor and temp_mid !=0:
            #merge sub array to later be merged to the final array
            merge(list_, right +1, temp_mid, len(list_)-1)
            #Update the pivot
            mid = right
        #Increase the factor
        factor = factor * 2
        temp_mid = right
       
        #Final merge, merge subarrays created by the subdivision
        #of the factor to the main array.
        if factor > len(list_) :
            mid = right
            right = len(list_)-1
            merge(list_, 0, mid, right)
            break




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

lbs = copy.deepcopy(lista_aleatoria)   #lbs - Lista ordenada por Bubblesort (vai ser)
inicio = time.time()
bubbleSort(lbs)
fim = time.time()
tempobs = (fim - inicio) #Tempo que demora para executar o BS
print "Tempo de ordenacao por Bubble Sort : " + str(tempobs)

lis = copy.deepcopy(lista_aleatoria)  #lis - Lista ordenada por Insertionsort (vai ser)
inicio2 = time.time()
insertionSort(lis)
fim2 = time.time()
tempois = (fim2 - inicio2) #Tempo que demora para executar o IS
print "Tempo de ordenacao por Insert Sort : " + str(tempois)

# Queremos trabalhar na copia da lista e nao na lista original, por isso "copy"/"deepcopy"
lms = copy.deepcopy(lista_aleatoria) #lms - Lista ordenada por MergeSort (vai ser)
inicio3 = time.time()
mergeSort(lms)
fim3 = time.time()
tempoms = (fim3 - inicio3) #Tempo que demora para executar o IS
print "Tempo de ordenacao por Merge Sort : " + str(tempoms)

lqs = copy.deepcopy(lista_aleatoria)   #lqs - Lista ordenada por Quicksort (vai ser)
inicio = time.time()
quickSort(lqs)
fim = time.time()
tempobs = (fim - inicio) #Tempo que demora para executar o BS
print "Tempo de ordenacao por QuickSort : " + str(tempobs)
