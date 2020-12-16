from Stack import Stack
from binaryTree import BinaryTree
import operator

def buildParseTree (the_exp) :
    the_list = the_exp.split ()
    p_stack = Stack ()
    the_tree = BinaryTree ('')
    p_stack.push (the_tree)
    current_tree = the_tree

    for i in the_list :
        if i == '(' :
            current_tree.insertLeft ('')
            p_stack.push (current_tree)
            current_tree = current_tree.getLeftChild ()

        elif i not in ['+' , '-' , '*' , '/' , ')'] :
            current_tree.setRootValue (int (i))
            current_tree = p_stack.pop ()

        elif i in ['+' , '-' , '*' , '/'] :
            current_tree.setRootValue (i)
            current_tree.insertRight ('')
            p_stack.push (current_tree)
            current_tree = current_tree.getRightChild ()

        elif i == ')' :
            current_tree = p_stack.pop ()

        else :
            raise ValueError

    return the_tree

def evaluate (parse_tree) :
    opers = {'+' : operator.add , '-' : operator.sub , '*' : operator.mul , '/' : operator.truediv}

    left = parse_tree.getLeftChild ()
    right = parse_tree.getRightChild ()

    if left and right :
        fn = opers [parse_tree.getRootValue ()]

        return fn (evaluate (left) , evaluate (right))

    else :
        return parse_tree.getRootValue ()

def postorderEval (parse_tree) :
    opers = {'+' : operator.add , '-' : operator.sub , '*' : operator.mul , '/' : operator.truediv}

    res_one = None
    res_two = None

    if parse_tree :
        res_one = postorderEval (parse_tree.getLeftChild ())
        res_two = postorderEval (parse_tree.getRightChild ())

        if res_one and res_two :
            return opers [parse_tree.getRootValue ()] (res_one , res_two)

        else :
            return parse_tree.getRootValue ()

def inorderEval (parse_tree) :
    exp = ""

    if parse_tree :
        left = inorderEval (parse_tree.getLeftChild ())

        if  left != "" :
            exp += '( ' + str (left)

        exp += str (parse_tree.getRootValue ()) + ' '

        right = inorderEval (parse_tree.getRightChild ())

        if right != "" :
            exp += str (right) + ') '

    return exp
