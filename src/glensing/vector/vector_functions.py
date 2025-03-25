import numpy as np
from .vector_class import vector

def dot(v1 , v2):
    """Returns the dot product of two vectors
    """
    if (not isinstance(v1,vector) or not isinstance(v2,vector)):
        raise ValueError('Both arguments must be vector class instances')
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def cross(v1 , v2):
    """Returns the cross product of two vectors
    """
    if (not isinstance(v1,vector) or not isinstance(v2,vector)):
        raise ValueError('Both arguments must be vector class instances')
    
    xcoord =   v1.y*v2.z - v1.z*v2.y
    ycoord = -(v1.x*v2.z - v1.z*v2.x)
    zcoord =   v1.x*v2.y - v1.y*v2.x
    
    return vector([xcoord, ycoord, zcoord])

def norm(v):
    """Returns the norm of a vector
    """
    if not isinstance(v,vector):
        raise ValueError('Arguments must be vector class instance')
    return np.sqrt(v.x*v.x + v.y*v.y + v.z*v.z)

