from UnorderedList import UnorderedList

class Deque () :
    def __init__ (self) :
        self.items = UnorderedList ()

    def add_front (self , item) :
        self.items.append (item)

    def remove_front (self) :
        return self.items.pop ()

    def add_rear (self , item) :
        self.items.insert (0 , item)

    def remove_rear (self) :
        return self.items.pop (0)

    def size (self) :
        return self.items.size ()

    def is_empty (self) :
        return self.items.isEmpty ()