from binaryTree import BinaryTree

def postorder (tree) :
    if tree :
        postorder (tree.getLeftChild ())
        postorder (tree.getRightChild ())
        print (tree.getRootValue ())