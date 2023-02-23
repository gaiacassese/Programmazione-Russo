#Scrivete una funzione sum_csv(file_name) che sommi tutti i valori delle vendite degli shampoo del file “shampoo_sales.csv” passato come argomento

def sum_csv(file_name):
    res = 0
    my_file = open(file_name, 'r') #apro il file, aggiungo 'r' perchè mi serve in modalità lettura

    if my_file==[]:
        return None
    
    for line in my_file:

        elements = line.split(',') #splitta gli elementi della lista
        if elements[0] != 'Date': #se l'elemento è diverso dalla colonna Date
 
            try: 
                value=float(elements[1])
                res=res+value
            
            except:
                value=None
            
    if res==0:
        return None
               
    return res 

