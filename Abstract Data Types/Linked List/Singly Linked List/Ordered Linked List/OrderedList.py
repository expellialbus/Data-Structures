from Node import Node

class OrderedList () :
    def __init__ (self) :
        self.head = None

    def isEmpty (self) :
        return self.head == None

    def add (self , item) :
        temp = Node (item)

        current = self.head
        previous = None
        stop = False

        while current != None and not stop :
            if current.getData () > item :
                stop = True

            else :
                previous = current
                current = current.getNext ()

        if previous == None :
            temp.setNext (self.head)
            self.head = temp

        else :
            temp.setNext (current)
            previous.setNext (temp)

    def size (self) :
        current = self.head
        count = 0

        while current != None :
            count += 1
            current = current.getNext ()

        return count

    def search (self , item) :
        current = self.head
        stop = False
        found = False

        while current != None and not stop and not found :
            if current.getData () == item :
                found = True

            else :
                if current.getData () > item :
                    stop = True

                else :
                    current = current.getNext ()

        return found

    def remove (self , item) :
        current = self.head
        previous = None
        found = False

        while not found :
            if current.getData () == item :
                found = True

            else :
                previous = current
                current = current.getNext ()

        if previous == None :
            self.head = current.getNext ()

        else :
            previous.setNext (current.getNext ())

    def index (self , item) :
        current = self.head
        found = False
        stop = False
        count = 0

        while current != None and not found and not stop:
            if current.getData () > item :
                stop = True

            elif current.getData () == item :
                found = True

            else :
                count += 1
                current = current.getNext ()

        if not found or stop :
            return "{} is not exist in the list.".format (item)

        else :
            return count

    def pop (self , item = None) :
        current = self.head
        previous = None
        data = None
        count = 0
        found = False

        if item == None :
            while current.getNext () != None :
                previous = current
                current = current.getNext ()

            data = current.getData ()

            if previous == None :
                self.head = current.getNext ()

            else :
                previous.setNext (current.getNext ())

        else :
            if item < 0 :
                while current != None :
                    count -= 1
                    current = current.getNext ()

                current = self.head

            while current != None and not found :
                if count == item :
                    found = True

                else :
                    count += 1
                    previous = current
                    current = current.getNext ()

            if not found :
                data = "The list doesn't has {}. index.".format (item)

            else :
                data = current.getData ()

                if previous == None :
                    self.head = (current.getNext ())

                else :
                    previous.setNext (current.getNext ())

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
        size = 0
        item_list = '['

        while current != None :
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
        count = 0

        while current != None :
            count += 1
            current = current.getNext ()

        temp = Node (count)

        temp.setNext (self.head)
        self.head = temp

        return self.head.getData ()

    def __str__ (self) :
        if self.head == None :
            return "[]"

        else :
            current = self.head
            item_list = '['

            while current != None :
                if current.getNext () != None :
                    item_list += str (current.getData ()) + ", "

                else :
                    item_list += str (current.getData ()) + ']'

                current = current.getNext ()
        return item_list