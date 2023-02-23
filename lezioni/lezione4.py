#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste

class CSVFile():

    def __init__(self, name): #ovvero nella riga 21 'shampoo_sales.csv'
        self.name = name

    def get_data(self):

        values = []
        my_file = open(self.name, 'r')

        if my_file == []:
            return None

        for line in my_file:
            elements = line.strip('\n').split(',') #strip toglie \n alla fine e all'inizio della linea
            if elements[0] != 'Date':
                values.append(elements)

        return values

vendite=CSVFile('shampoo_sales.csv') #inizializzo una variabile che richiama la classe CSVFile, che prende in input il file 'shampoo_sales.csv'
print(vendite.name) #stampa il nome
print(vendite.get_data())