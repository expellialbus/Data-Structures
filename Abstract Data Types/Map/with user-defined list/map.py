from UnorderedList import UnorderedList

class Map () :
    def __init__ (self) :
        self.slots = UnorderedList ()
        self.data = UnorderedList ()

    def __setitem__ (self , key , value) :
        if self.slots.search (key) :
            index = self.slots.index (key)
            self.data.insert (index , value)
            self.data.pop (index + 1)

        else :
            self.slots.append (key)
            self.data.append (value)

    def __getitem__ (self , key) :
        index = self.slots.index (key)

        if (index == int ()) :
            return "{} doesn't exist.".format (key)

        values = self.data.head

        for i in range (index) :
            values = values.getNext ()

        return values.getData ()

    def __delitem__ (self , key) :
        index = self.slots.index (key)

        self.slots.pop (index)
        self.data.pop (index)

    def __str__ (self) :
        if self.slots.isEmpty () :
            return "{}"

        else :
            keys = self.slots.head
            values = self.data.head
            item_list = '{'

            while keys != None :
                item_list += str (keys.getData ()) + ": " + str (values.getData ())
                if keys.getNext () != None :
                    item_list += ", "

                else :
                    item_list += '}'

                keys = keys.getNext ()
                values = values.getNext ()

        return item_list

    def __len__ (self) :
        return len (self.slots)

    def __contains__ (self , key) :
        return self.slots.search (key)