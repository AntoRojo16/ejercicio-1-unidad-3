class Carrera:
    __codigoCarrera=0
    __nombreCarrera=0
    __FechaInicio=0
    __duracion=""
    __titulo=""


    def __init__(self,codigo,nombre,fecha,duracion,titulo):
        self.__codigoCarrera=codigo
        self.__nombreCarrera=nombre
        self.__FechaInicio=fecha
        self.__duracion=duracion
        self.__titulo=titulo

    def __str__(self):
        s=("Codigo {} nombre {} fecha inicio {} duracion {} titulo {}".format(self.__codigoCarrera,self.__nombreCarrera,self.__FechaInicio,self.__duracion,self.__titulo))
        return s


    def getNombre(self):
        return self.__nombreCarrera


    def getCodigo(self):
        return self.__codigoCarrera


