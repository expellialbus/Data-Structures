class Node () :
    def __init__ (self , init_data) :
        self.data = init_data
        self.next = None
        self.back = None

    def getData (self) :
        return self.data

    def getNext (self) :
        return self.next

    def getBack (self) :
        return self.back

    def setData (self , new_data) :
        self.data = new_data

    def setNext (self , new_next) :
        self.next = new_next

    def setBack (self , new_back) :
        self.back = new_back

