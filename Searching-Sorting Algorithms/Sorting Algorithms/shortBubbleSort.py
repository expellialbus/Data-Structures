def shortBubbleSort (a_list) : 
    exchange = True
    pass_num = 0 

    while pass_num < len (a_list) - 1 and exchange : 
        exchange = False
        
        for i in range (len (a_list) - pass_num - 1) : 
            if a_list [i] > a_list [i + 1] : 
                exchange = True

                a_list [i] , a_list [i + 1] = a_list [i + 1] , a_list [i]

        pass_num += 1 

    return a_list
