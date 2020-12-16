class TreeNode () :
    def __init__ (self , key , value , left = None , right = None , parent = None) :
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def hasLeftChild (self) :
        return self.left_child

    def hasRightChild (self) :
        return self.right_child

    def isLeftChild (self) :
        return self.parent and self.parent.left_child == self

    def isRightChild (self) :
        return self.parent and self.parent.right_child == self

    def isRoot (self) :
        return not self.parent

    def isLeaf (self) :
        return not (self.right_child or self.left_child)

    def hasAnyChild (self) :
        return self.right_child or self.left_child

    def hasBothChild (self) :
        return self.right_child and self.left_child

    def replaceNodeData (self , key , val , lc , rc) :
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc

        if self.hasRightChild () :
            self.leftChild.parent = self

        if self.hasRightChild () :
            self.right_child.parent = self

    def spliceOut (self) :
        if self.isLeaf () :
            if self.isLeftChild () :
                self.parent.left_child = None

            else :
                self.parent.right_child = None

        elif self.hasAnyChild () :
            if self.hasLeftChild () :
                if self.isLeftChild () :
                    self.parent.left_child = self.left_child

                else :
                    self.parent.right_child = self.left_child

                self.left_child.parent = self.parent

            else :
                if self.isLeftChild () :
                    self.parent.left_child = self.right_child

                else :
                    self.parent.right_child = self.right_child

                self.right_child.parent = self.parent

    def findSuccessor (self) :
        succ = None

        if self.hasRightChild () :
            succ = self.right_child.findMin ()

        else :
            if self.parent :
                if self.isLeftChild () :
                    succ = self.parent

                else :
                    self.parent.right_child = None
                    succ = self.parent.findSuccessor ()
                    self.parent.right_child = self

        return succ

    def findMin (self) :
        current = self

        while current.hasLeftChild () :
            current = current.left_child

        return current

    def __iter__ (self) :
        if self :
            if self.hasLeftChild () :
                for i in self.left_child :
                    yield i

            yield self.key

            if self.hasRightChild () :
                for i in self.right_child :
                    yield i