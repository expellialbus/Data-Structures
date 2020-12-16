def oddEvenSort (the_list) :
    i = j = 0

    while i < len (the_list) :
        if i % 2 == 0 :
            j = 0

        else :
            j = 1

        while j < len (the_list) - 1 :
            if the_list [j] > the_list [j  + 1] :
                the_list [j] , the_list [j  + 1] = the_list [j + 1] , the_list [j]

            j += 2
        i += 1

    return the_list
