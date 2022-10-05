from Nodo import *


import xml.etree.ElementTree as ET

class ListaDoble:

    def __init__(self ):
        self.nombreLista = ""
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        #print(str(self.nombreLista))
        nuevo = Nodo(dato)
        #self.size = self.size + 1

        if self.primero == None: 
            self.primero = nuevo
            self.ultimo = nuevo

        else: 
            self.ultimo.next = nuevo 
            nuevo.before = self.ultimo 
            self.ultimo = nuevo 
    
    def show(self):

        temp = self.primero 

        while temp != None:

            print(temp.dato) 

            temp = temp.next 

    




                