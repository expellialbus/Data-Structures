class Map () :
    def __init__ (self) :
        self.slots = []
        self.data = []

    def __setitem__ (self , key , value) :
        if key in self.slots :
            self.data [key] = value

        else :
            self.slots.append (key)
            self.data.append (value)

    def __getitem__ (self , key) :
        return self.data [key]

    def __delitem__ (self , key) :
        index = self.slots.index (key)
        
        self.slots.pop (index)
        self.data.pop (index)

    def __str__ (self) :
        if self.slots == [] :
            return "{}"

        else :
            item_list = '{'

            for i in range (len (self.slots)) :
                item_list += str(self.slots[i]) + ": " + str(self.data[i])

                if i != len (self.slots) - 1 :
                    item_list += ", "

                else :
                    item_list += '}'

        return item_list

    def __len__ (self) :
        return len (self.slots)

    def __contains__ (self , key) :
        return key in self.slots