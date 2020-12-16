def selectionSort (a_list) : 
    for i in range ((len (a_list) -1 ) , 0 , -1) : 
        pos_of_max = int () 

        for j in range (1 , (i + 1)) : 
            if a_list [j] > a_list [pos_of_max] : 
                pos_of_max = j 

        a_list [pos_of_max] , a_list [i] = a_list [i] , a_list [pos_of_max] 

    return a_list 
