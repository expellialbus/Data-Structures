def combSort (the_list) :
    gap = len (the_list)
    condition = True

    while gap != 1 or condition :
        gap = int (gap / 1.3)              # ideal reduction factor

        if gap < 1 :
            gap = 1

        condition = False

        for i in range (len (the_list) - gap) :
            if the_list [i] > the_list [i + gap] :
                the_list [i] , the_list [i + gap] = the_list [i + gap] , the_list [i]
                condition = True

    return the_list

