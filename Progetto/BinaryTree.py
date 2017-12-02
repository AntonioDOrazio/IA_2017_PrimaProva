if __name__ == '__main__':
    from strutture.Stack import PilaArrayList
    from strutture.Queue import CodaArrayList_deque
else:
    from strutture.Stack import PilaArrayList
    from strutture.Queue import CodaArrayList_deque

class BinaryNode:
    def __init__(self, info):
        self.info = info # lista [chiave, valore, attivo (se implemento Lazy)]

        self.father = None
        self.leftSon = None
        self.rightSon = None

class BinaryTree:
    def __init__(self, rootNode = None):
        self.root = rootNode

    def insertAsLeftSubTree(self, father, subtree):
        """Inserisco radice di un sottoalbero come figlio
        sinistro del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son

    def insertAsRightSubTree(self, father, subtree):
        """Inserisco radice di un sottoalbero come figlio
        destro del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    def cutLeft(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte
        dal figlio sinistro del nodo father"""
        son = father.leftSon
        newTree = BinaryTree(son)
        newTree.leftSon = None
        return newTree

    def cutRight(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte
        dal figlio sinistro del nodo father"""
        son = father.rightSon
        newTree = BinaryTree(son)
        newTree.rightSon = None
        return newTree

    def DFS(self):
        """Ottiene lista elementi da visita
        in profondita"""
        res = []
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            if current.rightSon != None:
                stack.push(current.rightSon)
            if current.leftSon != None:
                stack.push(current.leftSon)
        return res

    def BFS(self):
        """Ottiene lista elementi da visita in ampiezza"""
        res = []
        q = CodaArrayList_deque()
        if self.root != None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.info)
            if current.leftSon != None:
                q.enqueue(current.leftSon)
            if current.rightSon != None:
                q.enqueue(current.rightSon)
        return res


    def cut(self, node):
        """Stacca e restituisce l'intero sottoalbero radicato in node. L'operazione
        cancella dall'albero il nodo node e tutti i suoi discendenti."""
        if node == None:
            return BinaryTree(None)
        if node.father == None:  # se il nodo è la radice
            self.root = None
            return BinaryTree(node)
        f = node.father # prendo padre nodo
        if node.leftSon == None and node.rightSon == None:  # se nodo è foglia
            #cerco la foglia e la elimino
            if f.leftSon == node:
                f.leftSon = None
            else:
                f.rightSon = None
            return BinaryTree(node)
        # taglio il sottoalbero dal padre
        elif f.leftSon == node:
            nt = self.cutLeft(f)
            # f.leftSon = None  --> Questa operazione viene fatta in cutLeft
            return nt
        else:
            nt = self.cutRight(f)
            # f.rightSon = None  --> Questa operazione viene fatta in cutRight
            return nt

    def stampa(self):
        """Permette di stampare l'albero. Per farlo si usa una pila di appoggio"""
        stack = PilaArrayList()
        if self.root is not None:
            stack.push([self.root, 0])  # pila di liste di due elementi [il nodo, il livello occupato dal nodo]
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
