def binaryTree (r) :
    return [r , [] , []]

def insertLeft (root , new_branch) :
    temp = root.pop (1)

    if len (temp) > 1 :
        root.insert (1 , [new_branch , temp , []])

    else :
        root.insert (1 , [new_branch , [] , []])

    return root

def insertRight (root , new_branch) :
    temp = root.pop (2)

    if len (temp) > 1 :
        root.insert (2 , [new_branch , [] , temp])

    else :
        root.insert (2 , [new_branch , [] , []])

    return root

def getRootValue (root) :
    return root [0]

def setRootValue (root , new_value) :
    root [0] = new_value

def getLeftChild (root) :
    return root [1]

def getRightChild (root) :
    return root [2]