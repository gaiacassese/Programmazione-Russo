#Create quindi la classe MovingAverage, che venga inizializzata con la lunghezza delle finestra, e che abbia un metodo compute che prenda in input la lista di valori della serie e che ritorni la lista di valori corrispondente alla media mobile.

class ExamException(Exception):
        pass

class MovingAverage:

    def __init__(self, finestra):
        self.finestra=finestra
        #verifico se la finestra è positiva
        if int(self.finestra)<1:
            raise ExamException('Errore, la finestra non può avere lunghezza negativa')

    #funzione che mi calcola la media
    def mean(self, list):
        sum=0
        for elem in list:
            sum+=elem
        return sum/len(list)
        
    
    def compute(self, mylist):
        res=[]
        #verifico se la lista è vuota
        if len(mylist)==0:
            raise ExamException('Errore, lista valori vuota')
        #verifico che la lista sia maggiore della finestra
        if (self.finestra>len(mylist)):
            raise ExamException('Errore, la finestra è maggiore della lista')

        #sfrutto l'indexing facendo un ciclo while che itera fino a quando l'indice arriva al limite della lista
        i=0
        
        while i+self.finestra<=len(mylist):
            tmp= mylist[i:i+self.finestra]
            #print(tmp)
            res.append(self.mean(tmp)) #scrivo self.mean perchè sto richiamando una funzione definita sempre nella stessa classe
            i += 1
            
        return res    


