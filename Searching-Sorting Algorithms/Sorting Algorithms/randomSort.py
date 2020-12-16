from random import randint

def randomSort (the_list) :
    sort = False

    while not sort :
        from_index = randint(0, (len(the_list) - 1))
        to_index = randint(0, (len(the_list) - 1))

        if the_list [from_index] > the_list [to_index] :
            the_list [from_index] , the_list [to_index] = the_list [to_index] , the_list [from_index]

        sort = True

        for i in range (len (the_list) - 1) :
            if the_list [i] > the_list [i + 1] :
                sort = False

                break

    return the_list