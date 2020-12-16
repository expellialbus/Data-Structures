def gnomeSort (the_list) :
    j = int ()

    for i in range (len (the_list)) :
        while j < len (the_list) - 1 :
            if the_list [j] > the_list [j + 1] :
                the_list [j] , the_list [j + 1] = the_list [j + 1] , the_list [j]

                break

            j += 1

        while j > 0 :
            if the_list [j] < the_list [j - 1] :
                the_list [j] , the_list [j - 1] = the_list [j - 1] , the_list [j]

            j -= 1

    return the_list