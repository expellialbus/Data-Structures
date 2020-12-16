from UnorderedList import UnorderedList

class Queue () :
    def __init__ (self):
        self.items = UnorderedList ()

    def is_empty (self) :
        return self.items.isEmpty ()

    def enqueue (self , item) :
        self.items.insert (0 , item)

    def dequeue (self) :
        return self.items.pop ()

    def size (self) :
        return self.items.size ()
