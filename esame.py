#Create quindi la classe MovingAverage, che venga inizializzata con la lunghezza delle finestra, e che abbia un metodo compute che prenda in input la lista di valori della serie e che ritorni la lista di valori corrispondente alla media mobile.

class ExamException(Exception):
        pass

class MovingAverage:

    def __init__(self, finestra):
        self.finestra=finestra
        #verifico che finestra non sia None
        if self.finestra is None:
            raise ExamException('Errore, la finestra non può avere lunghezza None')
        #verifico se la finestra è positiva
        if int(self.finestra)<1:
            raise ExamException('Errore, la finestra non può avere lunghezza negativa')

    #funzione che mi calcola la media
    def mean(self, list):
        sum=0
        for elem in list:
            sum += elem
        return sum/len(list)
        
    
    def compute(self, mylist):
        res=[]
        #verifico che la lista non sia None
        if mylist is None:
            raise ExamException('Errore, la lista non può essere None')
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
            try:
                res.append(self.mean(tmp)) #scrivo self.mean perchè sto richiamando una funzione definita sempre nella stessa classe
                i += 1
            except:
                raise ExamException('Errore, la lista non è composta solo da interi') 
            
        return res    

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result) # Deve stampare a schermo [3.0,6.0,12.0]
