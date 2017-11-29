class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        # Não existe filho na esquerda
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        # Caso já tenha um filho, insere o novo filho e coloca
        # o existe no próximo nível 
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key

    def getRootVal(self):
        return self.key

    # def __str__(self):
    #     return self.key

    
# r = BinaryTree('a')
# print(r)