def cocktailSort (the_list) :
    count = 0
    condition = True

    while condition :
        condition = False
        while count < len (the_list) - 1 :
            if the_list [count] > the_list [count + 1] :
                the_list [count] , the_list [count + 1] = the_list [count + 1] , the_list [count]
                condition = True

            count += 1

        count = len (the_list) - 1

        while count > 0 :
            if the_list [count] < the_list [count - 1] :
                the_list [count] , the_list [count - 1] = the_list [count - 1] , the_list [count]
                condition = True

            count -= 1

    return the_list
