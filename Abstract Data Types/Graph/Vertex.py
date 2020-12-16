class Vertex () :
    def __init__ (self , key) :
        self.key = key
        self.neighbor = {}

    def addNeighbor (self , neighbor , weight = None) :
        self.neighbor [neighbor] = weight

    def getConnections (self) :
        return self.neighbor.keys ()

    def getWeight (self , neighbor) :
        return self.neighbor [neighbor]

    def __str__ (self) :
        return "{} neighbors : {}".format (self.key , [x for x in self.neighbor])
