#Implementare una funzione (simile a quella creata le lezioni precedenti) che ritorni una lista i cui elementi saranno le date delle vendite del file shampoo sales.csv.

from datetime import datetime

def fun_csv(my_file):
    lista_date=[]
    my_file = open("shampoo_sales.csv", 'r') #apro il file, aggiungo 'r' perchè mi serve in modalità lettura
 
    if my_file==[]:
        return None
    
    for line in my_file:
        element=line.split(',')
        if element[0] == 'Date':
            try:
                my_date = datetime.strptime (element[0],'%d-%m-%Y')
                lista_date.append(my_date)

            except:
                my_date is None
    print(my_file)

my_file = fun_csv('shampoo_sales.csv') 



        



