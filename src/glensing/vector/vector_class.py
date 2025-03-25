import numpy as np 

class vector:

    #Constructor
    def __init__(self, input_vector):
        self.x = input_vector[0]
        self.y = input_vector[1]
        self.z = input_vector[2]

        self.values = [self.x , self.y, self.z]

    #
    # Self functions
    #

    def norm(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    #
    #Overwrite methods
    #
    
    def __add__(self, other):
        if isinstance(other, vector):
            out_vec = tuple( a + b for a, b in zip(self.values, other.values) )
        elif isinstance(other, (int, float)):
            out_vec = tuple( a + other for a in self .values)
        else:
            raise ValueError("Addition with type {} not supported".format(type(other)))

        return self.__class__(out_vec)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, vector):
            out_vec = tuple( a - b for a, b in zip(self.values, other.values) )
        elif isinstance(other, (int, float)):
            out_vec = tuple( a - other for a in self .values)
        else:
            raise ValueError("Addition with type {} not supported".format(type(other)))

        return self.__class__(out_vec)

    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self,other):
        if isinstance(other,vector):
            out_vec = tuple( a*b for a, b in zip(self.values, other.values) )
        elif isinstance(other, (int, float)):
            out_vec = tuple( a * other for a in self.values )
        return self.__class__(out_vec)

    def __rmul__(self, other):
        return self.__mul__(other)    

    def __truediv__(self, other):
        if isinstance(other, vector):
            out_vec = tuple( a/b for a, b in zip(self.values, other.values) )
        elif isinstance(other, (int, float)):
            out_vec = tuple( a / other for a in self.values ) 
        else:
            raise ValueError("Division with type {} not supported".format(type(other)))
        
        return self.__class__(out_vec)

    def __str__(self):
        return "[ {:.20f} , {:.20f} , {:.20f} ]".format(self.x , self.y, self.z)
