def countingSort (the_list) :
    max_value = max (the_list)
    counting_list = [0 for i in range (max_value + 1)]

    for i in the_list :
        counting_list [i] += 1

    return [i for i in range (len (counting_list)) for j in range (counting_list [i])]