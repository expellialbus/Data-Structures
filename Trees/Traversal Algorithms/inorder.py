from binaryTree import BinaryTree

def inorder (tree) :
    if tree :
        inorder (tree.getLeftChild ())
        print (tree.getRootValue ())
        inorder (tree.getRightChild ())