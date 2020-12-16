def quickSort (a_list) : 
	quickSortHelper (a_list , 0 , (len (a_list) - 1)) 

def quickSortHelper (a_list , first , last) : 
	if first < last : 

		split_point = partition (a_list  , first , last)

		quickSortHelper (a_list , first , (split_point - 1)) 
		quickSortHelper (a_list , (split_point + 1) , last)

def partition (a_list , first , last) : 
	pivot_value = a_list [first] 

	left_mark = first + 1 
	right_mark = last

	done = False 

	while not done :
		while a_list [left_mark] <= pivot_value and left_mark <= right_mark :
			left_mark += 1 

		while a_list [right_mark] >= pivot_value and right_mark >= left_mark : 
			right_mark -= 1

		if right_mark < left_mark : 
			done = True 

		else : 
			a_list [right_mark] , a_list [left_mark] = a_list [left_mark] , a_list [right_mark]

	a_list [first] , a_list [right_mark] = a_list [right_mark] , a_list [first] 

	return right_mark
