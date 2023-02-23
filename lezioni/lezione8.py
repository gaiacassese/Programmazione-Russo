#Creiamo un oggetto IncrementModel che estenda Model e che implementi il metodo predict() come spiegato nelle slides precedenti. L’input del metodo predict() e’ una lista di valori per gli n mesi passati

class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        
        # Valore precedente
        prev_value = None
        
        # Numero elementi
        if data != []:
            n = len(data)
        else:
            raise Exception('La lista di input è vuota')

        # Se il numero di elementi non è superiore a 1, ritorno 0 come predizione perché non ho informazioni sufficienti
        if n <= 1:
            return 
        
        # Media dell'incremento 
        avg_increase = 0

        # Incremento totale
        increase = 0

        for item in data:
            try:
                value = float(item)
                if value >= 0:
                    if prev_value == None:
                        prev_value = value
                    else:
                        increase += value - prev_value
                        prev_value = value
                else:
                    raise Exception('Item è negativo: "{}"'.format(item))
            except TypeError:
               print('Errore di TIPO! Non posso convertire "item" a float, vale: "{}"'.format(item))
            except ValueError:
                print('Errore di VALORE! Non posso convertire "item" a float, vale: "{}"'.format(item))
            
        # Divido l'incremento totale per il numero di incrementi effettuati, ovvero n-1
        
        avg_increase = increase / (n-1) 
        
        prediction = prev_value + avg_increase 
        return prediction