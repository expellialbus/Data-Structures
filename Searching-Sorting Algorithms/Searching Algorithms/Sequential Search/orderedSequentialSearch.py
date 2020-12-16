#Also known as Lineer Search Algorithm 

def orderedSequentialSearch (a_list , item) : 
    pos = int ()
    found = bool ()
    stop = bool ()

    while pos < len (a_list) and not found and not stop : 
        if a_list [pos] == item : 
            found = True 

        else : 
            if a_list [pos] > item : 
                stop = True 

            else : 
                pos += 1 

    return found 
