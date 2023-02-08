#stampa, una funzione che stampa il contenuto di una lista passata come argomento

def stampa(my_list):
    for item in my_list:
        print (item)

my_list=[1,2,3]
stampa(my_list)
print('----------')

#statistiche, una funzione che riceve una lista e, se `e una lista di interi, ne determina la somma, la media, il minimo ed il massimo degli elementi

def statistiche(my_list):
    sum=0
    for item in my_list:
        if type(item) is not int:
            print('la lista non è formata solo da interi')
            break
        sum += item
        
    n=len(my_list)
    mean=(sum)/n

    print (sum, mean)

    valore_minimo = min(my_list) #built in
    print(valore_minimo)

    valore_massimo = max(my_list) #built in
    print(valore_massimo)
       
my_list=[1,2,3]
statistiche(my_list)
print('----------')

#somma vettoriale, una funzione che riceve in ingresso due liste, determina se sono due liste di interi, se hanno la stessa dimensione e ne calcola la somma vettoriale, poi ritornata come lista, altrimenti ritorna una lista vuota

def somma_vettoriale(my_list, my_list2):
    lista_risultante=[]
    for item in my_list:
        if type(item) is not int:
            print('la lista non è formata solo da interi')
            break
    for item in my_list2:
        if type(item) is not int:
            print('la lista non è formata solo da interi')
            break

    if len(my_list) == len (my_list2):
        print ('le liste hanno la stessa lunghezza')
    else:
        print ('le liste hanno lunghezze diverse, cambiale')
        print (lista_risultante)
        return lista_risultante

         
    for i in range(len(my_list)):
        lista_risultante.append(my_list[i]+my_list2[i])
    
    stampa(lista_risultante)


my_list=[1,2,3]
my_list2=[4,5,7]
somma_vettoriale(my_list, my_list2)

        