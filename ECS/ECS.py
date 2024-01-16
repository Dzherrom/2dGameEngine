from multiprocessing import pool
import operator
from bitarray import bitarray
from typing import TypeVar
import glm

from Components.components import TransformComponent

# we use a bitset with bitarray() to keep track 
# of which components the entity has
MAX_COMPONENTS = 32
T = TypeVar("T")
Signature = bitarray(MAX_COMPONENTS)
    
class Entity:
    def __init__(self, entity_id):
        self.id = entity_id 
    
    #get Entity ID
    def GetId(self):
        return self.id
        
class Component:
    __id_counter = 0

    #stablish unique id for component
    @classmethod
    #Get component ID
    def get_component_id(cls):
        cls.__id_counter += 1
        return cls.__id_counter
        
class System:
    def __init__(self):
        #component sig will be unique per component
        self.__component_signature = set()
        self.__entities = []

    def add_entity_to_system(self, entity):
        self.__entities.append(entity)
        
    #uses a list comprehension to remove entity with specified ID from list
    def remove_entity_from_system(self, entity):
            self.entities = [e for e in self.entities if e.GetId() != entity.GetId()]

    #return actual entities on system
    def get_system_entities(self):
        return self.__entities

    #return component signature set to keep track of required comps
    def get_component_signature(self):
        return self.__component_signature

    #TO IMPLEMENT
    def require_component(self, component):
        component_id = component.get_id()
        self.__component_signature.add(component_id)
    
    
class Registry:
    def __init__(self, id):
        self.numEntities = 0
        self.componentPool = glm.vec2()
        
    def create_entity(self):
        pass
    
    def kill_entity(self, Entity):
        pass
    
    def add_component(self, __component_signature):
        pass 
    
    def remove_component(self, __component_signature):
        pass