from Stack import Stack

def infix_to_prefix (infix_expr) :
    infix_expr = infix_expr.upper()

    prefix_list = list ()
    temp_list = list ()
    remain_op = list ()
    op_stack = Stack ()

    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1 , ')' : 1}

    operands = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    numbers = "0123456789"

    expression = False

    while not expression :
        try :
            token_list = infix_expr.split()

            for token in token_list :
                if token not in operands :
                    if token not in numbers :
                        if token not in prec :
                            raise SyntaxError

            else :
                expression = True

        except SyntaxError :
            print ("You must entered the infix expression that each item separated by a space.")
            infix_expr = str (input ("Please enter again the expression : ")).upper ()

    for token in token_list :
        if token in operands or token in numbers :
            prefix_list.append (token)

        elif token == '(' :
            while len (prefix_list) != 0 :
                temp_list.insert (0 , prefix_list.pop ())

            while not op_stack.is_empty () :
                remain_op.insert (0 , op_stack.pop ())

            op_stack.push (token)

        elif token == ')' :
            top_token = op_stack.pop ()

            while top_token != '(' :
                prefix_list.insert (0 , top_token)
                top_token = op_stack.pop ()

        else :
            while (not op_stack.is_empty ()) and (prec [op_stack.peek ()] > prec [token]) :
                prefix_list.insert (-2 , op_stack.pop ())

            else :
                op_stack.push (token)

    while not op_stack.is_empty () :
        prefix_list.insert (0 , op_stack.pop ())

    while len (temp_list) != 0 :
        prefix_list.insert (0 , temp_list.pop ())

    while len (remain_op) != 0 :
        prefix_list.insert (0 , remain_op.pop ())

    return " ".join (prefix_list)
