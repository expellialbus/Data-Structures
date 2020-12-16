from Node import Node

class OrderedList () :
    def __init__ (self) :
        self.head = None

    def isEmpty (self) :
        return self.head == None

    def add (self , item) :
        temp = Node (item)

        current = self.head
        stop = False

        if self.head == None :
            temp.setNext (temp)
            temp.setBack (temp)
            self.head = temp

        else :
            while current.getNext () != self.head.getBack () and not stop :
                if current.getData () > item :
                    stop = True

                else :
                    current = current.getNext ()

            if current.getNext () == self.head.getBack () and current.getData () < temp.getData () :
                temp.setNext (self.head)
                temp.setBack (current.getNext ())
                current.getNext ().setNext (temp)
                self.head.setBack (temp)

            else :
                temp.setNext (current)
                temp.setBack (current.getBack ())
                current.getBack ().setNext (temp)
                current.setBack (temp)

                if self.head.getData () > temp.getData () :
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
        stop = False
        found = False

        while current.getNext () != self.head and not stop and not found :
            if current.getData () == item :
                found = True

            else :
                if current.getData () > item :
                    stop = True

                else :
                    current = current.getNext ()

        if current.getData () == item :
            found = True

        return found

    def remove (self , item) :
        current = self.head
        found = False
        stop = False

        while current.getNext () != self.head and not found and not stop :
            if current.getData () > item :
                stop = True

            elif current.getData () == item :
                found = True

            else :
                current = current.getNext ()

        if current.getNext () == self.head or stop :
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


    def index (self , item) :
        current = self.head
        found = False
        stop = False
        count = 0

        while current.getNext () != self.head and not found and not stop:
            if current.getData () > item :
                stop = True

            elif current.getData () == item :
                found = True

            else :
                count += 1
                current = current.getNext ()

        if not found or stop :
            if current.getData () != item :
                return "{} is not exist in the list.".format (item)


        return count

    def pop(self, item=None):
        current = self.head
        data = None
        found = False
        count = 0

        if item == None:
            while current.getNext() != self.head :
                current = current.getNext()

            data = current.getData()

            if current.getBack() == current :
                self.head = None

            else:
                current.getBack().setNext(current.getNext())
                current.getNext ().setBack (current.getBack ())

        else:
            if item < 0:
                count = -1
                while current.getNext () != self.head :
                    count -= 1
                    current = current.getNext()

                current = self.head

            while current.getNext () != self.head and not found:
                if count == item:
                    found = True

                else:
                    count += 1
                    current = current.getNext()

            else :

                if count == item :
                    found = True

            if found:
                data = current.getData()

                if current.getBack() == self.head.getBack () :
                    current.getNext ().setBack (self.head.getBack ())
                    self.head.getBack ().setNext (current.getNext ())
                    self.head = current.getNext ()

                else:
                    current.getBack().setNext(current.getNext())
                    current.getNext ().setBack (current.getBack ())

            else:
                data = "The list doesn't have {}. index.".format(item)

        return data

    def slice (self , begin = 0 , end = None , leap = 1) :
        try :
            if begin < 0 or leap < 0 :
                raise TypeError

            else :
                if end != None and end < 0 :
                    raise TypeError

        except TypeError :
            return "The method can execute just with unsigned integers."

        current = self.head
        count = 0
        size = 1
        item_list = '['

        while current.getNext () != self.head :
            size += 1
            current = current.getNext ()

        current = self.head

        if end == None :
            end = size

        elif end > size :
            return "The list doesn't have {}. index.".format (end)

        if begin > size :
            return "The list doesn't have {}. index.".format (begin)

        while count < end :
            if count == begin :
                if (count + 1) == end :
                    item_list += str (current.getData ()) + ']'

                else :
                    item_list += str (current.getData ()) + ", "

                begin += leap

            count += 1
            current = current.getNext ()

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