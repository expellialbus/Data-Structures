from binaryTree import BinaryTree

def preorder (tree) :
    if tree :
        print (tree.getRootValue ())
        preorder (tree.getLeftChild ())
        preorder (tree.getRightChild ())