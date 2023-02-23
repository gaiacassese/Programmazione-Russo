#versione 1.2

class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
   
    def __init__(self,name):
        self.name = name
        
    def get_data(self):
        
        import datetime

        #lista da restituire in caso di successo
        retList = []
        
        #userò questa lista per vedere se è ordinata o se ci sono duplicati
        listaMesiAnni = []
        
        #controllo se il nome è None
        if self.name is None:
            raise ExamException('Errore! nome file non inserito in input')
            
        #prova ad aprire il file
        try:
            my_file = open(self.name,"r")
            contenuto=my_file.readlines()
            #controllo comunque che il file non sia vuoto
            if len(contenuto) == 0:
              raise ExamException('Errore! Il file è vuoto')                  
            my_file.close()
            
        except Exception as e:
            raise ExamException('Errore! File non trovato o non leggibile: "{}" '.format(e))
 
        #adesso posso aprire il file 
            
        with open(self.name) as csv_file:
            for line in csv_file:
                elements = line.strip("\n").split(",")

        #se manca un parametro salto la riga e continuo senza alzare eccezioni
                if len(elements) < 2:
                    print('Manca almeno un parametro nella riga: --> "{}" - SKIP'.format(elements))
                    continue
        #non serve che controlli se ci sono più di due elementi perchè la funzione split prende i primi due in automatico
                
                if elements[0] == "date":
                    #sono sull'intestazione
                    print('Salto intestazione --> "{}" '.format(elements))
                    continue

                #per comodità assegno data e passeggeri a delle variabili locali per non lavorare con element[...]
                data = elements[0]
                
                #controllo che la data sia valida, se non lo è salto la riga senza alzare eccezioni
                try:
                    testData = data.split("-")
                    datetime.datetime(int(testData[0]),int(testData[1]),1) #metto giorno 1 per essere sicura che esista
                except:
                    print("Impossibile convertire la data --> {} - SKIP".format(data))
                    continue
                    
                #controllo che il numero di passeggeri sia valido, se non lo è salto la riga senza alzare eccezioni
                try:
                    passeggeri = int(elements[1])
                except:
                    print("Il valore del numero di passeggeri non è numerico --> {} - SKIP".format(elements[1]))
                    continue
                #controllo che il numero di passeggeri sia non negativo
                if passeggeri < 0:
                    print("Il numero di passeggeri deve essere non negativo--> {} - SKIP".format(elements[1]))
                    continue

                
                #controllo che l'anno sia compreso tra 1914, anno in cui ha volato il primo aereo di linea, e l'anno attuale
                if int(testData[0]) < 1914 or int(testData[0]) > datetime.date.today().year:
                    print("L'anno non è corretto --> {} - SKIP".format(elements[0]))
                    continue

                #creo la sottolista (rowlist) che poi andrò ad inserire nella lista generale (retlist)
                    #SONO NEL FOR 
                rowList = [data,passeggeri]
                retList.append(rowList)
                listaMesiAnni.append(data)

             #controllo se la lista è ordinata
            listaOrdinata = listaMesiAnni.copy()
            listaOrdinata.sort()
            
            if listaOrdinata ==listaMesiAnni:
                #tutto ordinato
                print("La lista è ordinata")
            else:
                #non ordinata
                raise ExamException("Errore! La lista NON è ordinata")
            
            #controllo se la lista ha duplicati
            lunghezzalista = len(listaMesiAnni)
            lunghezzalistaSet = len(set(listaMesiAnni))
            
            if lunghezzalista == lunghezzalistaSet:
                #se la lunghezza della lista è uguale alla lista senza duplicati allora non ci sono duplicati
                print("La lista non contiene duplicati")
            else:
                #altrimenti alzo un'eccezione
                raise ExamException("Errore! La lista contiene dei duplicati")

                
        return retList


#al di fuori della classe ho il metodo:
def detect_similar_monthly_variations(time_series, years):
    
#CONTROLLO I PARAMETRI
    
    #controllo time_series
    if time_series is None:
        print("La lista time_series è None")
        raise ExamException("Errore! La lista time_series è nulla")
        
    if len(time_series)==0:
        print("La lista time_series ha lunghezza 0")
        raise ExamException("Errore! La lista time_series ha lunghezza 0")
        
    #controllo years
    #se la lista è None
    if years is None:
        print("Lista anni None")
        raise ExamException("Errore! La lista degli anni è None")
    
    #che la lista abbia 2 valori
    if len(years) != 2:
        print("Gli anni devono essere 2")
        raise ExamException("Errore! Gli anni devono essere 2")
    
    # valori interi per gli anni
    if type(years[0]) is not int:
        raise ExamException("Errore! Il primo anno non è intero")
        
    if type(years[1]) is not int:
        raise ExamException("Errore! Il secondo anno non è intero")
        
    # anni ordinati consecutivi
    if years[1] != years[0] + 1:
        raise ExamException("Errore! Il secondo anno deve essere successivo al primo")
    
    #anni nella lista
    for anno in years:
        found = False #variabile temporanea per capire se l'anno è presente nella lista
        for el in time_series:
            tempAnno = int(el[0].split("-")[0])
            if  tempAnno == anno:
                found = True #se trovo l'anno nella lista allora 'trovato' diventa true ed esco dal ciclo
                break
    
        if not found:
            raise ExamException('Errore! Anno non nella lista "{}"'.format(anno))

    #fine controlli, inizia l'algoritmo

    #uso questa nomenclatura per aggiungere direttamente il valore che voglio tramite indexing
            
    anno0 = [None,None,None,None,None,None,None,None,None,None,None,None]
    anno1 = [None,None,None,None,None,None,None,None,None,None,None,None]

    #riempo gli array con delle variabili temporanee 
    for el in time_series:
        tempAnno = int(el[0].split("-")[0])
        tempMese = int(el[0].split("-")[1])
        tempPasseggeri = int(el[1])
        
        if tempAnno == years[0]:
            anno0[tempMese-1] = tempPasseggeri
            
        if tempAnno == years[1]:
            anno1[tempMese-1] = tempPasseggeri
        
    # calcolo le differenze
    #se qualcosa va storto... metto None (evidentemente manca)
    #ci saranno 11 segnaposti in quanto la lista delle differenze avrà un posto in meno rispetto alla lista in cui vado a prendere i dati (le coppie sono 11)
    
    diff0 = [None,None,None,None,None,None,None,None,None,None,None]
    diff1 = [None,None,None,None,None,None,None,None,None,None,None]
    
    for x in range(11):
        try:
            diff0[x] = anno0[x+1] - anno0[x]
        except:
            diff0[x] = None
        
        try:
            diff1[x] = anno1[x+1] - anno1[x]
        except:
            diff1[x] = None

    #finalmente calcolo il risultato della funzione
    
    retList=[False,False,False,False,False,False,False,False,False,False,False]
    
    for i in range(11):
        #caso del None, resta falso
        if diff1[i] == None or diff0[i] == None:
            retList[i] = False
            continue
        
        #calcolo differenza
        d = diff0[i] - diff1[i]
        if d >= -2 and d <= 2:
            retList[i] = True
        

    return retList

    
