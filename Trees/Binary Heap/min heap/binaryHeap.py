class BinaryHeap () :
    def __init__ (self) :
        self.heap_list = [0]
        self.current_size = 0

    def percUp (self , i) :
        while i // 2 > 0 :
            if self.heap_list [i] < self.heap_list [i // 2] :
                self.heap_list [i] , self.heap_list [i // 2] = self.heap_list [i // 2] , self.heap_list [i]

            i //= 2

    def insert (self , key) :
        self.heap_list.append (key)
        self.current_size += 1
        self.percUp (self.current_size)

    def percDown (self , i) :
        while (i * 2) <= self.current_size :
            mc = self.minChild (i)

            if self.heap_list [i] > self.heap_list [mc] :
                self.heap_list [i] , self.heap_list [mc] = self.heap_list [mc] , self.heap_list [i]

            i = mc

    def minChild (self , i) :
        if (i * 2) + 1 > self.current_size :
            return i * 2

        else :
            if self.heap_list [i * 2] < self.heap_list [(i * 2) + 1] :
                return i * 2

            else :
                return (i * 2) + 1

    def delMin (self) :
        the_min = self.heap_list [1]

        self.heap_list [1] = self.heap_list.pop ()
        self.current_size -= 1
        self.percDown (1)

        return the_min

    def buildHeap (self , a_list) :
        i = len (a_list) // 2

        self.current_size = len (a_list)
        self.heap_list = [0] + a_list [ : ]

        while i > 0 :
            self.percDown (i)

            i -= 1