from ClaseCarrera import Carrera

class Facultad:
    __codigo=0
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=0
    __Carreras=[]



    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo=codigo
        #print(codigo)
        #print(self.__codigo)
        self.__nombre=nombre
        #print(nombre)
        #print(self.__nombre)
        self.__direccion=direccion
        #print(self.__direccion)
        #print(direccion)
        #print(localidad)
        self.__localidad=localidad
        #print(self.__localidad)
        self.__telefono=telefono
        #print(telefono)
        #print(self.__telefono)
        self.__Carreras=[]

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getLocalidad(self):
        return self.__localidad

    def getTelefono(self):
        return self.__telefono

    def agregarCarrera(self,fila):
        unaCarrera=Carrera(fila[1],fila[2],fila[3],fila[4],fila[5])
        self.__Carreras.append(unaCarrera)

    def getCodig(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre


    def mostrar(self):
        print("FACULTAD {}".format(self.__nombre))
        print("Codigo {}  direccion {} localidad {} telefono {}".format(self.__codigo,self.__direccion,self.__localidad,self.__telefono))
        #print("la cantidad de carreras de {} es {}".format(self.__nombre,len(self.__Carreras)))
        for carrera in self.__Carreras:
            print(carrera)

    def mostrardatoscarrera(self):
        for carrera in self.__Carreras:
            print(carrera)

    def buscarCarrera(self,nombre):
        i=0
        nom=self.__Carreras[i].getNombre()
        while(i<len(self.__Carreras))and(nombre!=nombre):
            i+=0
            nom=self.__Carreras[i].getNombre()

    def buscarCarrera(self,nombre):
        i=0
        nom=self.__Carreras[i].getNombre()
        while(i<len(self.__Carreras))and(nombre!=nom):
            nom=str(self.__Carreras[i].getNombre())
            i+=1
        if nom==nombre:
            print("Se encontro la carrera")
            print("Codigo {}{} \nNombre {} Localidad {}".format(self.__codigo,self.__Carreras[i].getCodigo(),self.__nombre,self.__localidad))
            return False

        else:
            return True






