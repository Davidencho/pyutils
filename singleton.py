'''
    Il Singleton è un pattern di programmazione molto usato che consente di utilizzare una singola istanza per una determinata
    classe. In Python è piuttosto macchinoso ma fattibile. Alla creazione di un nuovo oggetto, viene chiamato il metodo
    __new__ della classe invocata, dopodichè il metodo __init__. Questi due metodi sono quindi invocati a prescindere da tutto
    il resto, motivo per cui la dichiarazione/assegnazione delle variabili d'istanza non può avvenire in questi due metodi.
    Da qui la creazione del metodo __inizialize__, che può essere a piacere rinominato, e che viene invocato nel __new__
    solo in caso in cui non esiste già un'istanza di quella classe.
    Per una classe senza variabili d'istanza, si può semplicemente eliminare il metodo inizialize e la riga di codice che lo
    invoca.
    Il metodo __init__ non è a questo punto essenziale, non inserendolo verrà utilizzato quello della classe Object
'''

class Singleton():
    __instance = None

    def __new__(cls):
        """ Override the default __new__ method to implement singleton behavior. """
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
            cls.__instance.__initialize__()
        return cls.__instance

    def __initialize__(self):
        # Qui si possono settare le variabili d'istanza come se fosse un __init__
        # Qui sotto dichiaro una stringa che viene istanziata quando viene creato l'oggetto e poi la stampo.
        self.string = 'This is a string istance.'
        print(self.string)



if __name__ == '__main__':
    s = Singleton()
    s = Singleton()

# Chiamo due volte il costruttore, nonostante ciò, viene stampata una singola volta la stringa.
# Questo perchè il metodo initialize viene invocato solo ed esclusivamente la prima volta.