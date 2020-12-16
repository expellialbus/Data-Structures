def binarySearch (a_list , item) : 
	first = 0
	last = len (a_list) - 1
	found = False

	while first <= last and not found : 
		midpoint = (first + last) // 2 

		if a_list [midpoint] == item : 
			found = True 

		else : 
			if a_list [midpoint] > item : 
				last = midpoint - 1

			else : 
				first = midpoint + 1 

	return found 