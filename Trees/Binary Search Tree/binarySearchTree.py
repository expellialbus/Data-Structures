from TreeNode import TreeNode

class BinarySearchTree () :
    def __init__ (self) :
        self.root = None
        self.size = 0

    def lenght (self) :
        return self.size

    def __len__ (self) :
        return self.size

    def put (self , key , value) :
        if self.root :
            node = self.__get (key , self.root)

            if node :
                node.payload = value

            else :
                self.__put (key , value , self.root)

        else :
            self.root = TreeNode (key , value)

        self.size += 1

    def __put (self , key , value , current_node) :
        if key < current_node.key :
            if current_node.hasLeftChild () :
                self.__put (key , value , current_node.left_child)

            else :
                current_node.left_child = TreeNode (key , value , parent = current_node)

        else :
            if current_node.hasRightChild () :
                self.__put (key , value , current_node.right_child)

            else :
                current_node.right_child = TreeNode (key , value , parent = current_node)

    def __setitem__ (self , key , value) :
        self.put (key , value)

    def get (self , key) :
        if self.root :
            res = self.__get (key , self.root)

            if res :
                return res.payload

            else :
                return None

        else :
            return None

    def __get (self , key , current_node) :
        if not current_node :
            return None

        elif current_node.key == key :
            return current_node

        elif current_node.key < key :
            return self.__get (key , current_node.right_child)

        else :
            return self.__get (key , current_node.left_child)

    def __getitem__ (self , key) :
        return self.get (key)

    def __contains__ (self , key) :
        if self.get (key) :
            return True

        else :
            return False

    def delete (self , key) :
        if self.size > 1 :
            node_to_remove = self.__get (key , self.root)

            if node_to_remove :
                self.remove (node_to_remove)
                self.size -= 1

            else :
                raise KeyError ("Error, key not in tree.")

        elif self.size == 1 and self.root.key == key :
            self.root = None
            self.size -= 1

        else :
            raise KeyError ("Error, key not in tree.")

    def __delitem__ (self , key) :
        self.delete (key)

    def remove (self , current_node) :
        if current_node.isLeaf () :
            if current_node.isLeftChild () :
                current_node.parent.left_child = None

            else :
                current_node.parent.right_child = None

        elif current_node.hasBothChild () :
            succ = current_node.findSuccessor ()
            succ.spliceOut ()
            current_node.key = succ.key
            current_node.payload = succ.payload

        else :
            if current_node.hasLeftChild () :
                if current_node.isLeftChild () :
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child

                elif current_node.isRightChild () :
                    current_node.parent.right_child = current_node.left_child
                    current_node.left_child.parent = current_node.parent

                else :
                    current_node.replaceNodeData (current_node.left_child.key ,
                                                    current_node.left_child.payload ,
                                                    current_node.left_child.left_child ,
                                                    current_node.left_child.right_child)

            else :
                if current_node.isLeftChild () :
                    current_node.parent.left_child = current_node.right_child
                    current_node.right_child.parent = current_node.parent

                elif current_node.isRightChild () :
                    current_node.parent.right_child = current_node.right_child
                    current_node.right_child.parent = current_node.parent

                else :
                    current_node.replaceNodeData (current_node.right_child.key ,
                                                  current_node.right_child.payload ,
                                                  current_node.right_child.left_child ,
                                                  current_node.right_child.right_child)

    def __iter__ (self) :
        return self.root.__iter__ ()



