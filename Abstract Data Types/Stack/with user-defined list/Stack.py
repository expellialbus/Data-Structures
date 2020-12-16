from UnorderedList import UnorderedList

class Stack () :
    def __init__ (self) :
        self.items = UnorderedList ()

    def is_empty (self) :
        return self.items.isEmpty ()

    def push (self , item) :
        self.items.append (item)

    def pop (self) :
        return self.items.pop ()

    def peek (self) :
        return int (self.items.slice ()[-2])

    def size (self) :
        return self.items.size ()

