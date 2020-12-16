from Vertex import Vertex

class Graph () :
    def __init__ (self) :
        self.vertices = {}

    def addVertex (self , vertex) :
        self.vertices [vertex.key] = vertex

    def getVertex (self , key) :
        if key in self.vertices.keys () :
            return self.vertices [key]

        else :
            return None

    def addEdge (self , from_key , to_key , weight = None) :
        if from_key not in self.vertices :
            self.addVertex (Vertex (from_key))

        if to_key not in self.vertices :
            self.addVertex (Vertex (to_key))

        self.vertices [from_key].addNeighbor (self.vertices [to_key] , weight)

    def getVertices (self) :
        return self.vertices.keys ()

    def __contains__ (self , key) :
        return key in self.vertices

    def __iter__ (self) :
        return iter (self.vertices.values ())
