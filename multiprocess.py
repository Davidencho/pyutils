'''
    Sfruttare il multiprocessing su Python è molto molto semplice, soprattutto perchè quasi tutto automatizzato.
    Si può usare la classe Process o Pool (una piscina di processi). Io personalmente mi trovo meglio con Process,
    si possono passare argomenti a piacere alla funzione target senza dover usare funzioni parziali o altre
    cose becere.
    Essenzialmente occorre prevedere una funzione, che sarà quella chiamata dai vari processi invocati, e
    chiamarla come parametro di Process come in basso.
    I processi sono di per sè delle entità che hanno ognuno un proprio spazio di memoria associato e gestito dal sistema
    operativo, ma non condiviso tra loro. Ecco perchè, per salvare i risultati occorre utilizzare delle strutture
    dati speciali, qui sotto una lista e una particolare coda del modulo "multiprocessing".

    IMPORTANTE

    Il multiprocessing si può usare anche all'interno delle classi. Personalmente, ho avuto moltissimi problemi
    nell'utilizzo del multiprocessing nelle classi su Windows, in particolar modo quando si chiamano funzioni
    che hanno come parametro "self". Funzioni "statiche" (@staticmethod) invece non hanno problemi.
    Questo è dovuto alla "serializzazione" o in inglese "pickle" di queste funzioni di classi.
    Su Linux invece non ho riscontrato alcun problema.

    Ho fatto anche un esempio con i semafori, essenzialmente delle variabili binarie che vengono "acquisite" da un processo
    per indicare che è il suo turno. Quando il processo finisce rilascia il semaforo che può essere acquisito da un
    altro processo.
    Questo meccanismo è utilizzato qui sotto banalmente per l'esecuzione in contemporeanea di un certo numero di processi
    ma nella realtà viene utilizzato per la sincronizzazione tra processi.
'''

from multiprocessing import Manager, Process, Semaphore

def power_2(number, shared_list):
    shared_list.append(number*number)

def power_2_queue(number, shared_queue):
    shared_queue.put(number*number)

def power_2_semaphore(number, shared_list, semaphore):
    # Al posto di with è possibile usare in ugual modo semaphore.acquire() all'inizio e semaphore.release() alla fine!
    with semaphore:
        print(f"Process {number}: Acquired semaphore.")
        shared_list.append(number * number)
    print(f"Process {number}: Released semaphore.")


if __name__ == '__main__':
    processes = []
    shared_list = Manager().list()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for n in numbers:
        process = Process(target=power_2, args=(n, shared_list))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
        # Con il join si fa in modo che il main thread (quello del programma principale) possa andare avanti solo quando
        # tutti i processi nella lista sono terminati.

    print(f'Risults with shared_list: {shared_list}')


    processes.clear()
    shared_queue = Manager().Queue()
    for n in numbers:
        process = Process(target=power_2_queue, args=(n, shared_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Risults with shared_queue: ')
    while not shared_queue.empty():
        print(shared_queue.get())


    # Esempio utilizzo dei semafori
    print('\n\n\nSEMAFORI \n')
    processes.clear()
    shared_list = Manager().list()
    max_processes = 2
    semaphore = Semaphore(max_processes) # Istanzio un semaforo che permette massimo 2 processi in contemporanea.
    for n in numbers:
        process = Process(target=power_2_semaphore, args=(n, shared_list, semaphore))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


