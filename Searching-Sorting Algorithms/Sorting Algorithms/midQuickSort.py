def quickSort (a_list) :
	if len (a_list) <= 1 :
		return a_list

	else :
		pivot_value = a_list [(len (a_list) // 2)]
		left = list ()
		right = list ()

		for i in range (len (a_list)) :
			if i != (len (a_list) // 2) :
				if a_list [i] < pivot_value :
					left.append (a_list [i])

				else :
					right.append (a_list [i])

	return quickSort (left) + [pivot_value] + quickSort (right)