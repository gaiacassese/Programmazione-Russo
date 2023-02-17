#Create quindi la classe Diff, che: quando viene inizializzata accetti anche un parametro opzionale di nome ratio il cui valore di default sia 1, e che abbia un metodo compute che prenda in input una lista di valori numerici e che ritorni in output la lista corrispondente alle loro differenze.

class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        self.ratio=ratio
        #sratio deve essere positivo
        if ratio<1:
            raise ExamException('Errore, ratio deve avere valore positivo')
        if ratio is None:
            raise ExamException('Errore, ratio deve avere un valore diverso da None')

    def compute(self, mylist):
        res=[]
        #verifico che la lista non sia None
        if mylist is None:
            raise ExamException('Errore, la lista non può essere None')
        #verifico che l'input sia una lista
        if type(mylist) is not list:
            raise ExamException('Errore, non è stata data una lista in input')
        #verifico che la lista abbia almeno due elementi
        if len(mylist)<1:
            raise ExamException('Errore, la lista deve avere almeno due elementi')
        #verifico che la lista sia composta da numeri con la somma: se non posso sommare l'elemento di una lista lancio un'eccezione 
        sum=0
        try:
            for i in range(len(mylist)):
                sum += mylist[i]
        except:
            raise ExamException('Errore, la lista non è composta solo da interi') 
            
        #inizio esecuzione
        for i in range (len(mylist)-1):
            valueA= mylist[i]
            valueB= mylist[i+1]
            result= valueB-valueA
            
            print (valueB, '-', valueA, '=', result)
            res.append(result/self.ratio)
        #fine esecuzione
        return res


diff=Diff()
result=diff.compute([2,4,8,16])
print(result)