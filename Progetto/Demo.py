from LazyDictionary import LazyDictionary
import cProfile
import pstats

def main():
    """Demo sull'esecuzione del dizionario"""
    print("registro = LazyDictionary()")
    registro = LazyDictionary()

    print('registro.add("Matematica", 8)')
    registro.add("Matematica", 8)

    print('registro.add("Storia", 6.5)')
    registro.add("Storia", 6.5)

    print('registro.add("Ed. Fisica", "Distinto")')
    registro.add("Ed. Fisica", "Distinto")

    print("Materie, registro.keys() ==> ", registro.keys())
    print("Voti, registro.values() ==> ", registro.values())

    print("Elimino Storia")
    registro.remove("Storia")

    print("Struttura con elemento eliminato")
    print(registro.tree.stampa())

    print("Sovrascrivo con nuovo elemento")
    registro.add("Scienze", 9)

    print("Struttura con elemento sovrascritto")
    print(registro.tree.stampa())

    print("Inizializzo dizionario da struttura esistente")


    codiciLibri = [[13, "1984"], [9, "Harry Potter"], ["N.A.", "Il signore degli Anelli"]]

    libri = LazyDictionary(codiciLibri)
    print(libri.get(13))
    print(libri.get("N.A."))
    print(libri.allPairs())

    # TODO eliminare
    print("Inserisco chiave 2")
    ciao = LazyDictionary()
    ciao.add(2, 45)
    print("size ", ciao.length)
    print("omg", ciao.size())
    ciao.tree.stampa()
    ciao.add(2, 56)
    print("size ", ciao.length)
    ciao.values()
    ciao.tree.stampa()




### CODE PROFILING ###

'''Variabile globale per il dizionario, a scopo di profiling'''
registro = LazyDictionary()

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

def stampaChiavi():
    chiavi = registro.keys()
    print ("LE CHIAVI SONO ", chiavi)
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
    print(registro.tree.stampa())

def elemento():
    # Stampo un preciso elemento
    print(registro.get("Arte"))


if __name__ == '__main__':
    main()

    popolaDizionario()
    cProfile.run('stampaChiavi()', "output.txt")
    p = pstats.Stats("output.txt")
    p.strip_dirs().sort_stats("time").print_stats()

