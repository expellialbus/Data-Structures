#Also known as Lineer Search Algorithm

def sequentialSearch (a_list , item) : 
	pos = int ()
	found = bool () 

	while pos < len (a_list) and not found : 
		if a_list [pos] == item : 
			found = True 

		else : 
			pos += 1 

	return found 

