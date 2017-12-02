from BinaryTree import BinaryTree
from BinaryTree import BinaryNode


class LazyBst:
    def __init__(self):
        self.tree = BinaryTree()

    def key(self, node):
        if node is None:
            return None
        return node.info[0]

    def value(self, node):
        if node is None:
            return None
        return node.info[1]

    def isActive(self, node):
        if node is None:
            return False
        else:
            return node.info[2]

    def maxKeySon(self, root):
        """Ottengo il nodo con chiave piu grande.
        Si trova piu a destra possibile"""
        curr = root
        while curr.rightSon is not None:
            curr = curr.rightSon
        return curr

    def isLeftSon(self, node):
        """Ritorna vero se è figlio sinistro del proprio padre"""
        if node == node.father.leftSon:
            return True
        return False

    def search(self, key):
        """Ritorna value associato alla chiave key"""
        node = self.searchNode(key)
        return self.value(node)

    def searchNode(self, key):
        """Ricerca il nodo con chiave key e restituisce il nodo (o None)"""
        if self.tree.root == None:
            return None

        curr = self.tree.root
        while curr != None:
            currKey = self.key(curr)
            if key == currKey:
                if not self.isActive(curr):
                    return None # filtro lazy applicato qui
                return curr
            # cerco usando proprietà dell'albero di ricerca
            if key < currKey:
                curr = curr.leftSon
            else:
                curr = curr.rightSon

        return None


    def insert(self, key, value):
        """Inserisce valore nel dizionario"""
        values = [key, value, True]
        newTree = BinaryTree(BinaryNode(values))

        if self.tree.root == None:
            self.tree.root = newTree.root
        else:
            curr = self.tree.root
            pred = None

            #cerco posizione corretta e libera
            while curr != None: #TODO se mark as deleted
                pred = curr
                if key <= self.key(curr):
                    curr = curr.leftSon
                else:
                    curr = curr.rightSon

            if key <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newTree)
            else:
                self.tree.insertAsRightSubTree(pred, newTree)


    def oneSonDeletion(self, node):
        """Cancella nodo con singolo figlio"""
        son = None
        #cerco figlio del nodo
        if node.leftSon != None:
            son = node.leftSon
        elif node.rightSon != None:
            son = node.rightSon

        son.info[2] = False


    def delete(self, key):
        """Permette di cancellare il nodo appartenente all'albero con
        chiave key"""
        toRemove = self.searchNode(key)
        if toRemove != None:
            if toRemove.leftSon == None or toRemove.rightSon == None: #sto rimuovendo un nodo che ha 0 o 1 figlio
                self.oneSonDeletion(toRemove)
            else: # sto rimuovendo un nodo che ha due nodi figli
                maxLeft = self.maxKeySon(toRemove.leftSon) #predecessore del nodo da rimuovere
                toRemove.info, maxLeft.info = maxLeft.info, toRemove.info # scambio il contenuto informativo dei nodi
                self.oneSonDeletion(maxLeft) #adesso so che maxLeft non ha figli destri e posso applicare la cutOneSonNode
