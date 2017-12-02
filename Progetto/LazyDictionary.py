# Antonio D'Orazio - 0242178

from LazyBinaryTree import LazyBinaryTree
from LazyBinaryTree import BinaryNode


""" Classe LazyDictionary: tutti gli output sono a livello di Chiave e Valore
Livello piu visibile dei dati """

class LazyDictionary:
    def __init__(self, elems=None):
        # @param elems: lista per inizializzare con sintassi [[chiave, valore],[chiave,valore], ...]
        self.tree = LazyBinaryTree()
        self.length = 0
        if elems is not None:
            for el in elems:
                node = BinaryNode(el)
                self.add(node.info[0], node.info[1])

    def add(self, key, val):
        # @param key: numero o stringa
        # @param val: numero o stringa
        self.tree.insert(str(key), val)
        self.length += 1

    def remove(self, key):
        # @param key: numero o stringa
        self.tree.delete(str(key))

    def get(self, key):
        # @param key: numero o stringa
        # @return: valore associato a chiave
        node = self.tree.search(str(key))
        return self.tree.value(node)

    def size(self):
        # @return: numero di elementi nel dizionario
        return len(self.tree)

    def allPairs(self):
        # @return pairs: lista di tipo [chiave, valore]
        infos = self.tree.DFS()
        pairs = []
        for info in infos:
            pairs.append([info[0], info[1]])
        return pairs

    def keys(self):
        # @return keys: lista di tutte le chiavi
        infos = self.tree.DFS()
        keys = []
        for info in infos:
            keys.append(info[0])
        return keys

    def values(self):
        # @return values: lista di tutti i valori
        infos = self.tree.DFS()
        values = []
        for info in infos:
            values.append(info[1])
        return values
