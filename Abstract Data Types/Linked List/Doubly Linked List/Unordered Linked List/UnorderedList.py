from Node import Node

class UnorderedList () :
    def __init__ (self) :
        self.head = None

    def isEmpty (self) :
        return self.head == None

    def add (self , item) :
        temp = Node (item)
        temp.setNext (self.head)

        if self.head != None :
            self.head.setBack (temp)

        self.head = temp

    def size (self) :
        current = self.head
        count = 0

        while current != None :
            count += 1
            current = current.getNext ()

        return count

    def search (self , item) :
        current = self.head
        found = False

        while current != None and not found :
            if current.getData () == item :
                found = True

            else :
                current = current.getNext ()

        return found

    def remove (self , item) :
        current = self.head
        found = False

        while current != None and not found :
            if current.getData () == item :
                found = True

            else :
                current = current.getNext ()

        if current == None :
            print ("{} is not exist in the list.".format (item))

        elif current.getBack () == None :
            self.head = current.getNext ()
            self.head.setBack (current.getBack ())

        else :
            current.getBack ().setNext (current.getNext ())



    def append (self , item) :
        temp = Node (item)
        temp.setNext (None)

        if self.head == None :
            self.head = temp

        else :
            current = self.head
            previous = None
            found = False

            while not found :
                if current == None :
                    found = True

                else :
                    previous = current
                    current = current.getNext ()

            previous.setNext (temp)

    def index (self , item) :
        current = self.head
        found = False
        count = 0

        while current != None and not found :
            if current.getData () == item :
                found = True

            else :
                count += 1
                current = current.getNext ()

        if not found :
            return "{} is not exist in the list.".format (item)

        else :
            return count

    def pop (self , item = None) :
        current = self.head
        data = None
        found = False
        count = 0

        if item == None :
            while current.getNext () != None :
                current = current.getNext ()

            data = current.getData()

            if current.getBack () == None :
                self.head = current.getNext ()
                self.head.setBack (current.getBack ())

            else :
                current.getBack ().setNext (current.getNext ())

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
                    current = current.getNext ()

            if found :
                data = current.getData()

                if current.getBack () == None :
                    self.head = current.getNext ()

                else :
                    current.getBack ().setNext (current.getNext ())

            else :
                data = "The list doesn't have {}. index.".format (item)

        return data

    def insert (self , index , item) :
        temp = Node (item)

        current = self.head
        found = False
        count = 0

        if current == None :
            self.head = temp

        else :
            if index < 0 :
                while current != None :
                    count -= 1
                    current = current.getNext ()

                current = self.head

            while current != None and not found :
                if count == index :
                    found = True

                else :
                    count += 1
                    current = current.getNext ()

            if found :
                if current.getBack () == None :
                    temp.setNext (current)
                    temp.setBack (current.getBack ())
                    current.setBack (temp)

                    self.head = temp

                else :
                    temp.setNext (current)
                    temp.setBack (current.getBack ())
                    current.getBack ().setNext (temp)
                    current.setBack (temp)

            else :
                print ("The list doesn't have {}. index.".format (index))


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
            return "The list doesn't have {}. index".format (begin)

        while  count < end :
            if count == begin :
                if (count + 1) == end :
                    item_list += str (current.getData ()) + ']'

                else :
                    item_list += str (current.getData ()) + ', '

                begin += leap

            count += 1
            current = current.getNext ()

        return item_list

    def __len__ (self) :               # this len method is count the number of items in the list
        current = self.head            # and then adds the count value to the head of the list as a node
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

