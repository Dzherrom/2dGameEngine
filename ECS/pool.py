from operator import index
from typing import TypeVar
import glm
import sdl2, sdl2.ext, sdl2.sdlimage
from ECS.ECS import Entity

T = TypeVar('T', bound=Entity)
class Pool(object):
    def __init__(self):
        self.data = []
        T = TypeVar('T', bound= Entity)
        self._pool : list[T] = []
        
    def IsEmpty(self):
        return not bool(self.data)
    
    def GetSize(self):
        return len(self.data)
    
    def Resize(self, n):
        self.data = [None]*n
    
    def Celar(self):
        self.data.clear()
    
    def Add(self, object):
        self.data.append(object)
        
    def Set(self, index, object):
        self.data[index] = object
        
    def Get(self, index):
        return self.data[index]

      