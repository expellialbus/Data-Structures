from Node import Node

class UnorderedList () :
    def __init__ (self) :
        self.head = None

    def isEmpty (self) :
        return self.head == None

    def add (self , item) :
        temp = Node (item)

        if self.head == None :
            self.head = temp
            temp.setNext (temp)
            temp.setBack (temp)

        else :
            temp.setNext (self.head)
            temp.setBack (self.head.getBack ())
            self.head.getBack ().setNext (temp)
            self.head.setBack (temp)
            self.head = temp

    def size (self) :
        current = self.head
        count = 1

        while current.getNext () != self.head :
            count += 1
            current = current.getNext ()

        return count

    def search (self , item) :
        current = self.head
        found = False

        while current.getNext () != self.head and not found :
            if current.getData () == item :
                found = True

            else :
                current = current.getNext ()

        if current.getData () == item :
            found = True

        return found

    def remove (self , item) :
        current = self.head
        found = False

        while current.getNext () != self.head and not found :
            if current.getData () == item :
                found = True

            else :
                current = current.getNext ()

        if current.getNext () == self.head :
            if current.getData () != item :
                print ("{} is not exist in the list.".format (item))

            else :
                current.getBack ().setNext (current.getNext ())
                current.getNext ().setBack (current.getBack ())

        else :
            current.getBack ().setNext (current.getNext ())
            current.getNext ().setBack (current.getBack ())

            if self.head.getData () == item :
                self.head = current.getNext ()


    def append (self , item) :
        temp = Node(item)

        if self.head == None:
            self.head = temp
            temp.setNext(temp)
            temp.setBack(temp)

        else:
            temp.setNext(self.head)
            temp.setBack(self.head.getBack())
            self.head.getBack().setNext(temp)
            self.head.setBack(temp)

    def index(self, item):
        current = self.head
        found = False
        count = 0

        while current.getNext() != self.head and not found:
            if current.getData() == item:
                found = True

            else:
                count += 1
                current = current.getNext()

        if not found:
            if current.getData() != item:
                return "{} is not exist in the list.".format(item)

        return count

    def pop(self, item=None):
        current = self.head
        data = None
        found = False
        count = 0

        if item == None:
            while current.getNext() != self.head:
                current = current.getNext()

            data = current.getData()

            if current.getBack() == current:
                self.head = None

            else:
                current.getBack().setNext(current.getNext())
                current.getNext().setBack(current.getBack())

        else:
            if item < 0:
                count = -1
                while current.getNext() != self.head:
                    count -= 1
                    current = current.getNext()

                current = self.head

            while current.getNext() != self.head and not found:
                if count == item:
                    found = True

                else:
                    count += 1
                    current = current.getNext()

            else:

                if count == item:
                    found = True

            if found:
                data = current.getData()

                if current.getBack() == self.head.getBack():
                    current.getNext().setBack(self.head.getBack())
                    self.head.getBack().setNext(current.getNext())
                    self.head = current.getNext()

                else:
                    current.getBack().setNext(current.getNext())
                    current.getNext().setBack(current.getBack())

            else:
                data = "The list doesn't have {}. index.".format(item)

        return data

    def insert (self , index , item) :
        temp = Node (item)

        current = self.head
        found = False
        count = 0

        if current == None :
            self.head = temp
            self.head.setNext (temp)
            self.head.setBack (temp)

        else :
            if index < 0 :
                while current.getNext () != self.head :
                    count -= 1
                    current = current.getNext ()

                count -= 1
                current = self.head

            while current.getNext () != self.head and not found :
                if count == index :
                    found = True

                else :
                    count += 1
                    current = current.getNext ()

            if count == index :
                found = True

            if found :
                if current.getBack () == self.head.getBack () :
                    temp.setNext (current)
                    temp.setBack (current.getBack ())
                    current.getBack ().setNext (temp)
                    current.setBack (temp)
                    self.head = temp

                else :
                    temp.setNext (current)
                    temp.setBack (current.getBack ())
                    current.getBack ().setNext (temp)
                    current.setBack (temp)

            else :
                print ("The list doesn't have {}. index.".format (index))

    def slice(self, begin=0, end=None, leap=1):
        try:
            if begin < 0 or leap < 0:
                raise TypeError

            else:
                if end != None and end < 0:
                    raise TypeError

        except TypeError:
            return "The method can execute just with unsigned integers."

        current = self.head
        count = 0
        size = 1
        item_list = '['

        while current.getNext() != self.head:
            size += 1
            current = current.getNext()

        current = self.head

        if end == None:
            end = size

        elif end > size:
            return "The list doesn't have {}. index.".format(end)

        if begin > size:
            return "The list doesn't have {}. index.".format(begin)

        while count < end:
            if count == begin:
                if (count + 1) == end:
                    item_list += str(current.getData()) + ']'

                else:
                    item_list += str(current.getData()) + ", "

                begin += leap

            count += 1
            current = current.getNext()

        return item_list

    def __len__ (self) :                # this len method is count the number of items in the list
        current = self.head             # and then adds the count value to the head of the list as a node
        count = 1

        if current == None :
            return 0

        while current.getNext () != self.head :
            count += 1
            current = current.getNext ()

        temp = Node (count)

        temp.setNext (self.head)
        temp.setBack (self.head.getBack ())
        self.head.getBack ().setNext (temp)
        self.head.setBack (temp)
        self.head = temp

        return self.head.getData ()

    def __str__ (self) :
        if self.head == None :
            return "[]"

        else :
            current = self.head
            item_list = '['

            while current != self.head.getBack () :
                if current.getNext () != self.head :
                    item_list += str (current.getData ()) + ", "

                current = current.getNext ()

            else :
                item_list += str (current.getData ()) + ']'

        return item_list

