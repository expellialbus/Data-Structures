class HashTable () :
    def __init__ (self , size) :
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def put (self , key , value) :
        hash_value = self.hashFunction (key)

        if self.slots [hash_value] == None :
            self.slots [hash_value] = key
            self.data [hash_value] = value

        else :
            if self.slots [hash_value] == key :
                self.data [hash_value] = value

            else :
                next_slot = self.rehash (hash_value)

                while self.slots [next_slot] != None and self.slots [next_slot] != key and self.isEmpty (key) :
                    next_slot = self.rehash (next_slot)

                if self.slots [next_slot] == None :
                    self.slots [next_slot] = key
                    self.data [next_slot] = value

                else :
                    self.data [next_slot] = value

    def get (self , key) :
        start_slot = self.hashFunction (key)

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots [position] != None and not found and not stop :
            if self.slots [position] == key :
                data = self.data [position]
                found = True

            else :
                position = self.rehash (position)

                if position == start_slot :
                    stop = True

        return data

    def hashFunction (self , key) :
        return key % self.size

    def rehash (self , old_hash) :
        return (old_hash + 1) % self.size

    def isEmpty (self , key) :
        for i in self.slots :
            if i == None or i == key :
                return True

        else :
            print ("There are not any empty slot.!")

            return False