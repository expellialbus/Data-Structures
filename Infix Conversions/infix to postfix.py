from Stack import Stack

def infix_to_postfix (infix_expr) :
    infix_expr = infix_expr.upper ()

    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1}
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


    op_stack = Stack ()
    postfix_list = list ()

    for token in token_list :
        if token in operands or token in numbers :
            postfix_list.append (token)

        elif token == '(' :
            op_stack.push (token)

        elif token == ')' :
            top_token = op_stack.pop ()

            while top_token != '(' :
                postfix_list.append (top_token)
                top_token = op_stack.pop ()

        else :
            while (not op_stack.is_empty ()) and (prec [op_stack.peek ()] >= prec [token]) :
                postfix_list.append (op_stack.pop ())

            else :
                op_stack.push (token)

    while not op_stack.is_empty () :
        postfix_list.append (op_stack.pop ())

    return " ".join (postfix_list)