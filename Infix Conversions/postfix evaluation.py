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

def postfix_eval (postfix_expr) :
    operand_stack = Stack ()
    numbers = "0123456789"
    operator = ['+' , '-' , '*' , '/' , '^']

    expression = False

    while not expression :
        try :
            token_list = postfix_expr.split ()

            for token in token_list :
                if token not in numbers :
                    if token not in operator :
                        raise SyntaxError

            else :
                expression = True

        except SyntaxError :
            print ("You must enter the postfix expression that each item separated by space.")
            postfix_expr = str (input ("Please enter again the expression : "))

    for token in token_list :
        if token in numbers :
            operand_stack.push (int (token))

        else :
            second = operand_stack.pop ()
            first = operand_stack.pop ()

            result = do_math (first , second , token)

            operand_stack.push (result)

    return operand_stack.pop ()

print (postfix_eval ("2 3 *2^"))