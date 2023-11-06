from abc import ABC, abstractmethod
import requests
import json
from clothstore.services.mockup import ShirtMockup
from clothstore.services.design import ShirtDesign
from clothstore.services.printful import PrintfulApi


class interfaceApi(ABC):
    @abstractmethod
    def createMockup(self):
        pass



class PokeShirt(interfaceApi):
    def __init__(self):
        pass
    
    def createMockup(self, pk:str):
        mockup = ShirtMockup()
        return mockup.defaultShirt(pk)
    
class Printful(interfaceApi):
    def __init__(self):
        pass

    def createMockup(self, pk:str):
        mockup = PrintfulApi()
        return mockup.printfulMockup(pk)        

        
#shirt = PokeShirt()
#shirt.getResource("vaporeon")
#shirt.createMockup("flutter-mane")
#camisa = PokeShirt()
#estampado = PrintfulApi()

#mockup = estampado.printfulMockup(camisa.getResource("vaporeon"))
#print(mockup)