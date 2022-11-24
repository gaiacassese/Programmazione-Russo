class CSVfile():
    def __init__(self, name):
        self.name= name #è una variabile dell'oggetto
        
#init è funzione standard che serve ad inizializzare l'oggetto
    def get_data(self):

        values=[]
        my_file=open(self.name, 'r')

        if my_file == []:
            return None

        for line in my_file:
            elements=line.split(',')
            if elements[0]!= 'Date':
                values.append(elements)
        return values

my_file = CSVfile('shampoo_sales.csv') #trasformo la classe in un oggetto, non posso usare le classi nel codice in quanto sono astratte
#my_file=self.name
my_file.get_data()#esegue le istruzioni di get_data
print(my_file.get_data())