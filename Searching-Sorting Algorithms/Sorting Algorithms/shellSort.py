def shellSort (a_list) : 
    sublist_count = len (a_list) // 2 

    while sublist_count > 0 : 
        for start_pos in range (sublist_count) : 
            gapInsertionSort (a_list , start_pos , sublist_count) 

        sublist_count //= 2 
    
    return a_list 

def gapInsertionSort (a_list , start , gap) : 
    for i in range ((start + gap) , len (a_list) , gap) : 
        current_value = a_list [i]
        position = i

        while position >= gap and a_list [position - gap] > current_value : 
            a_list [position] = a_list [position - gap]
            position -= gap

        a_list [position] = current_value 
