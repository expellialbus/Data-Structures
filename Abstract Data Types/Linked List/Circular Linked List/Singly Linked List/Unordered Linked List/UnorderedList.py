from Node import Node

class UnorderedList () :
    def __init__ (self) :
        self.head = None
        self.last = None

    def isEmpty (self) :
        return self.head == None

    def add (self , item) :
        temp = Node (item)

        if self.head == None :
            temp.setNext (temp)
            self.last = temp

        else :
            temp.setNext (self.head)
            self.last.setNext (temp)

        self.head = temp

    def size (self) :
        if self.head == None :
            return 0

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

        else :
            found = current.getData () == item

        return found

    def remove (self , item) :
        current = self.head
        previous = None
        found = False

        while current.getNext () != self.head and not found :
            if current.getData () == item :
                found = True

            else :
                previous = current
                current = current.getNext ()

        if previous == None :
            self.head = current.getNext ()
            self.last.setNext (current.getNext ())

        elif current == self.last :
            if current.getData () != item :
                print ("{} is not exist in the list.".format (item))

            else :
                previous.setNext (current.getNext ())

        else :
            previous.setNext (current.getNext ())

    def append (self , item) :
        temp = Node (item)

        temp.setNext (self.head)
        self.last.setNext (temp)

        self.last = temp

    def index (self , item) :
        current = self.head
        found = False
        count = 0

        while current.getNext () != self.head and not found :
            if current.getData () == item :
                found = True

            else :
                count += 1
                current = current.getNext ()

        if current.getData () == item :
            found = True

        if not found :
            return "{} is not exist in the list.".format (item)

        else :
            return count

    def pop (self , item = None) :
        current = self.head
        previous = None
        data = None
        found = False
        count = 0

        if item == None :
            while current.getNext () != self.head :
                previous = current
                current = current.getNext ()

            data = current.getData()

            if previous == None :
                if current.getNext () != self.head :
                    self.head = current.getNext ()
                    self.last.setNext (current.getNext ())

                else :
                    self.head = None
            else :
                previous.setNext (current.getNext ())

        else :
            if item < 0 :
                while current.getNext () != self.head :
                    count -= 1
                    current = current.getNext ()

                count -= 1
                current = self.head

            while current.getNext () != self.head and not found :
                if count == item :
                    found = True

                else :
                    count += 1
                    previous = current
                    current = current.getNext ()

            if count == item and not found :
                found = True

            if found :
                data = current.getData()

                if previous == None :
                    self.head = current.getNext ()
                    self.last.setNext (current.getNext ())

                else :
                    previous.setNext (current.getNext ())

                    if current == self.last :
                        self.last = previous

            else :
                data = "The list doesn't have {}. index.".format (item)

        return data

    def insert (self , index , item) :
        temp = Node (item)

        current = self.head
        previous = None
        found = False
        count = 0

        if current == None :
            self.head = temp
            self.last = temp
            self.head.setNext (temp)
            self.last.setNext (temp)

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
                    previous = current
                    current = current.getNext ()

            if count == index and not found :
                found = True

            if found :
                if previous == None :
                    temp.setNext (current)
                    self.head = temp
                    self.last.setNext (temp)

                else :
                    temp.setNext (current)
                    previous.setNext (temp)

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

        while current.getNext () != self.head :
            size += 1
            current = current.getNext ()

        size += 1
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

        while current.getNext () != self.head :
            count += 1
            current = current.getNext ()

        count += 1
        temp = Node (count)

        temp.setNext (self.head)
        self.head = temp
        self.last.setNext (temp)

        return self.head.getData ()

    def __str__ (self) :
        if self.head == None :
            return "[]"

        else :
            current = self.head
            item_list = '['

            while current.getNext () != self.head :
                item_list += str (current.getData ()) + ", "
                current = current.getNext ()

            else :
                item_list += str (current.getData ()) + ']'

            return item_list

