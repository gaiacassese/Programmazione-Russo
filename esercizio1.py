def sum_list(my_list):
    risultato = 0 #inizializzare dentro la funzione ma fuori dal for, metto 0 perchè None e intero non sono omogenei
    if (len(my_list)==0):
        return None

    for item in my_list:
        risultato = risultato + item
    return risultato

    
    
my_list=[1,2,3]
somma= sum_list(my_list)
print (somma)
