# Antonio D'Orazio - 0242178
""" Alcuni esempi sull'esecuzione del dizionario """
from LazyDictionary import LazyDictionary
import cProfile
import pstats


def main():
    print("registro = LazyDictionary()")
    registro = LazyDictionary()

    print('registro.add("Matematica", 8)')
    registro.add("Matematica", 8)

    print('registro.add("Storia", 6.5)')
    registro.add("Storia", 6.5)

    print('registro.add("Ed. Fisica", "Distinto")')
    registro.add("Ed. Fisica", "Distinto")

    print("\nMaterie, registro.keys() ==> ", registro.keys())
    print("Voti, registro.values() ==> ", registro.values())

    print("Dimensione dizionario: ", registro.size());

    print('\nElimino Storia: registro.remove("Storia")')
    registro.remove("Storia")

    print("Struttura con elemento eliminato")
    registro.tree.stampa()
    print("Dimensione dizionario: ", registro.size());

    print('\nSovrascrivo con nuovo elemento ==> registro.add("Scienze", 9)')
    registro.add("Scienze", 9)

    print("Struttura con elemento sovrascritto")
    registro.tree.stampa()
    print("Dimensione dizionario: ", registro.size());

    print('\nSovrascrivo un elemento attivo ==> registro.add("Scienze", 8)')
    registro.add("Scienze", 8)

    print("Struttura con elemento sovrascritto")
    registro.tree.stampa()
    print("Dimensione dizionario: ", registro.size());

    print("\nInizializzo dizionario da struttura esistente")
    print('codiciLibri = [[13, "1984"], [9, "Harry Potter"], ["N.A.", "Il signore degli Anelli"]]')
    codiciLibri = [[13, "1984"], [9, "Harry Potter"], ["N.A.", "Il signore degli Anelli"]]
    print('libri = LazyDictionary(codiciLibri)')
    libri = LazyDictionary(codiciLibri)
    print("Stampo struttura albero")
    registro.tree.stampa()

    print("\nlibri.get(13) ==> ", libri.get(13))
    print('libri.get("N.A.") ==> ', libri.get("N.A."))
    print("libri.allPairs() ==> ", libri.allPairs())


'''Code profiling'''
#Variabile globale per il dizionario, a scopo di profiling
registro = LazyDictionary()

def codeProfiling():
    popolaDizionario()
    cProfile.run('funzioneDaProfilare()', "output.txt")
    p = pstats.Stats("output.txt")
    p.strip_dirs().sort_stats("time").print_stats()

def creaDizionario():
    registro = LazyDictionary()

def popolaDizionario():
    # Popolo dizionario
    registro.add("Matematica", 8)
    registro.add("Storia", 6.5)
    registro.add("Scienze", 6.5)
    registro.add("Fisica", 6.5)
    registro.add("Geografia", 6.5)
    registro.add("Informatica", 6.5)
    registro.add("Arte", 6.5)
    registro.add("Italiano", 6.5)
    registro.add("Ed. Fisica", "Distinto")

def chiavi():
    #Chiavi del dizionario
    chiavi = registro.keys()

def valori():
    #Valori del dizionario
    valori = registro.values()

def coppie():
    #Coppie [chiave, valore]
    coppie = registro.allPairs()

def rimuovi():
    #Elimino un elemento
    registro.remove("Storia")

def albero():
    # Stampo l'intero albero
    registro.tree.stampa()

def elemento():
    # Eseguo una ricerca
    result = registro.get("Arte")


if __name__ == '__main__':
    main()

    # Decommentare per eseguire code profiling
    # codeProfiling()
