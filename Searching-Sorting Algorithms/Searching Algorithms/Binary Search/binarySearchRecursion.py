def binarySearch (a_list , item) : 
	if len (a_list) == 0 : 
		return False

	else : 
		midpoint = len (a_list) // 2 

		if a_list [midpoint] == item : 
			return True 

		else : 
			if a_list [midpoint] > item : 
				return binarySearch (a_list [: midpoint] , item) 

			else : 
				return binarySearch (a_list [(midpoint + 1) : ] , item) 