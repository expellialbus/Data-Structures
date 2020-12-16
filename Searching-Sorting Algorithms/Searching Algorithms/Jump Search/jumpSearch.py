def jumpSearch (the_list , value) :
	gap = int (len (the_list) ** (1 / 2))
	i = 0
	find = False

	while i < len (the_list) and not find :
		if i + gap >= len (the_list) :
			i = len (the_list) - 1

		print ("döngü :" , the_list [i] , i )
		if the_list [i] == value :
			find = True

		else :
			if the_list [i] > value :
				j = i

				while j > i - gap :
					if the_list [j] == value :
						find = True

					j -= 1

		i += gap

	return find