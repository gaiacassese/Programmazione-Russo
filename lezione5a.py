#Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a schermo un messaggio di errore se si cerca di aprire un file non esistente.
class CSVFile():

    def __init__(self, name):
        self.name = name
    
    def get_data(self):

        values = []
        try:
            my_file = open(self.name, 'r')
            
        except Exception as e: #e è la variabile in  cui inserisco l'eccezione
            print('Errore: non esiste il file digitato "{}"'.format(e))
            
        if my_file == []:
            return None

        for line in my_file:
            elements = line.strip('\n').split(',')
            if elements[0] != 'Date':
                values.append(elements)

        return values