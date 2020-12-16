from Stack import Stack

def do_math (first_operand , second_operand , operator) :
    if operator == '+' :
        return first_operand + second_operand

    elif operator == '-' :
        return first_operand - second_operand

    elif operator == '*' :
        return first_operand * second_operand

    elif operator == '/' :
        return first_operand / second_operand

    else :
        return pow (first_operand , second_operand)

def prefix_eval (prefix_expr) :
    operand_stack = Stack ()
    numbers = "0123456789"
    operators = ['^' , '+' , '-' , '*' , '/']

    expression = False

    while not expression :
        try :
            token_list = prefix_expr.split ()
            token_list.reverse ()

            for token in token_list :
                if token not in numbers :
                    if token not in operators :
                        raise SyntaxError

            else :
                expression = True

        except SyntaxError :
            print ("You must enter the prefix expression that each item separeted by space.")
            prefix_expr = str (input ("Please enter the expression again : "))

    for token in token_list :
        if token in numbers :
            operand_stack.push (int (token))

        else :
            first = operand_stack.pop ()
            second = operand_stack.pop ()

            result = do_math (first , second , token)

            operand_stack.push (result)

    return operand_stack.pop ()
