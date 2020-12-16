class BinaryTree () :
    def __init__ (self , root) :
        self.key = root
        self.left_child = None
        self.right_child = None

    def insertLeft (self , new_node) :
        if self.left_child == None :
            self.left_child = BinaryTree (new_node)

        else :
            temp = BinaryTree (new_node)
            temp.left_child = self.left_child
            self.left_child = temp

    def insertRight (self , new_node) :
        if self.right_child == None :
            self.right_child = BinaryTree (new_node)

        else :
            temp = BinaryTree (new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def getLeftChild (self) :
        return self.left_child

    def getRightChild (self) :
        return self.right_child

    def setRootValue (self , value) :
        self.key = value

    def getRootValue (self) :
        return self.key