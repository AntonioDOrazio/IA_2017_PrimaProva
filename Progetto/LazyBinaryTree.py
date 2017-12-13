# Antonio D'Orazio - 0242178

if __name__ == '__main__':
    from strutture.Stack import PilaArrayList
    from strutture.Queue import CodaArrayList_deque
else:
    from strutture.Stack import PilaArrayList
    from strutture.Queue import CodaArrayList_deque


class BinaryNode:
    """ Classe BinaryNode: definisce un singolo nodo con
    informazioni e nodi padre, figlio destro e figlio sinistro"""

    def __init__(self, info):
        """info: lista per inizializzare con sintassi [chiave, valore, attivo]
        attivo: boolean, stabilisce se elemento è presente o cancellato"""
        self.info = info
        self.father = None
        self.leftSon = None
        self.rightSon = None

    def toString(self):
        """return: stringa con i valori del nodo"""
        return "{0} {1} {2} {3} {4} {5}".format(str(self.info[0]), str(self.info[1]), str(self.info[2]),
                                                str(self.father), str(self.leftSon), str(self.rightSon))


class LazyBinaryTree:
    """ Classe LazyBinaryTree: definisce un albero binario di ricerca
    a partire dalla sua radice. Implementa la lazy deletion. """

    def __init__(self, rootNode=None):
        """param rootNode: BinaryNode, la radice dell'albero"""
        self.root = rootNode

    ### INSERIMENTO ###
    def insert(self, key, value):
        """ Inserimento principale: inserisce nodo [chiave, valore, attivo] valore nell'albero
        param key: numero o stringa
        param val: numero o stringa
        return Boolean: True se nodo inserito, False se nodo sovrascritto """
        key = str(key)
        values = [key, value, True]
        newTree = LazyBinaryTree(BinaryNode(values))

        if self.root == None:
            self.root = newTree.root
            return True
        else:
            curr = self.root
            pred = None

            # cerco posizione corretta ed inserisco
            while curr is not None:
                if not curr.info[2]: # Per sovrascrivere un elemento eliminato
                    break
                pred = curr
                if key < self.key(curr):
                    curr = curr.leftSon
                elif key > self.key(curr):
                    curr = curr.rightSon
                else: # Se chiave è già presente sovrascrivo
                    break
            if curr is None:
                if key <= self.key(pred):
                    self.insertAsLeftSubTree(pred, newTree)
                else:
                    self.insertAsRightSubTree(pred, newTree)
                return True
            else:
                curr.info = self.info(newTree.root)
                return False

    def insertAsLeftSubTree(self, father, subtree):
        """Inserisce radice di un sottoalbero come figlio sinistro del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son

    def insertAsRightSubTree(self, father, subtree):
        """Inserisce radice di un sottoalbero come figlio destro del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    ### CANCELLAZIONE ###
    def delete(self, key):
        """ Cancellazione principale: cancella dall'albero il nodo con chiave key
        param key: numero o stringa
        return Boolean: True se eliminato correttamente, False altrimenti """
        key = str(key)
        toRemove = self.search(key)
        if toRemove != None:
            if toRemove.leftSon == None or toRemove.rightSon == None:
                # rimuove nodo con 0 o 1 figli
                self.oneSonDeletion(toRemove)
            else:  # rimuove nodo con 2 figli
                # predecessore del nodo da rimuovere
                maxLeft = self.maxKeySon(toRemove.leftSon)
                # scambio il contenuto informativo dei nodi
                toRemove.info, maxLeft.info = maxLeft.info, toRemove.info
                # adesso so che maxLeft non ha figli destri e posso applicare
                # la cutOneSonNode
                self.oneSonDeletion(maxLeft)
            return True
        return False

    def oneSonDeletion(self, node):
        """Cancella nodo con 0 o 1 figli. Implementa Lazy Deletion"""
        node.info[2] = False

    ### RICERCA ###
    def search(self, key):
        """Ricerca principale: restituisce nodo corrispondente a chiave key
        return: BinaryNode, nodo corrispondente a chiave key"""
        if self.root == None:
            return None
        key = str(key)
        curr = self.root
        while curr != None:
            currKey = self.key(curr)
            if key == currKey:
                if not self.isActive(curr):
                    return None  # filtro per lazy deletion
                return curr
            # cerco usando proprietà dell'albero di ricerca
            elif key < currKey:
                curr = curr.leftSon
            else:
                curr = curr.rightSon

        return None

    ### Metodi di appoggio con controllo se nodo è none ###
    def key(self, node):
        """return: string, la chiave del nodo"""
        if node is None:
            return None
        return node.info[0]

    def value(self, node):
        """return il valore associato al nodo"""
        if node is None:
            return None
        return node.info[1]

    def isActive(self, node):
        """return: boolean, true se nodo è attivo, falso se cancellato"""
        if node is None:
            return False
        else:
            return node.info[2]

    def info(self, node):
        """return: lista [chiave, valore, attivo]"""
        if node is None:
            return False
        else:
            return node.info

    def maxKeySon(self, root):
        """return: BinaryNode: nodo con chiave piu grande (quello piu a destra)"""
        curr = root
        while curr.rightSon is not None:
            curr = curr.rightSon
        return curr

    ### VISITE E STAMPA ###
    def DFS(self):
        """Visita in profondità
        return: lista di BinaryNode.info"""
        res = []
        stack = PilaArrayList()
        if self.root is not None and self.isActive(self.root):  # TODO forse eliminare ultimo control
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            if self.isActive(current):
                res.append(current.info)
            if current.rightSon != None:
                stack.push(current.rightSon)
            if current.leftSon != None:
                stack.push(current.leftSon)
        return res

    def BFS(self):
        """Visita in ampiezza
        return: lista di BinaryNode.info"""
        res = []
        q = CodaArrayList_deque()
        if self.root != None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            if self.isActive(current):
                res.append(current.info)
            if current.leftSon != None:
                q.enqueue(current.leftSon)
            if current.rightSon != None:
                q.enqueue(current.rightSon)
        return res

    def stampa(self):
        """return: void. Stampa albero sfruttando pila di appoggio"""
        stack = PilaArrayList()
        if self.root is not None:
            # pila di liste di due elementi
            # [il nodo, il livello occupato dal nodo]
            stack.push([self.root, 0])
        else:
            print("Empty tree!")
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print("|---" * level + str(current[0].info))

            if current[0].rightSon is not None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon is not None:
                stack.push([current[0].leftSon, level + 1])
