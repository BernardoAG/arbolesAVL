class NodoAVL:
    __variable= "dato", "izq","der","papa", "fe"

    def __init__(self, dat=0):
        self.__fe = 0
        self.__dato = dat
        self.__der=None
        self.__izq=None
        self.__papa=None

    def getFe(self):
        return self.__fe

    def setFe(self, fe):
        self.__fe = fe;

    def getDer(self):
        return self.__der

    def getIzq(self):
        return self.__izq

    def getPapa(self):
        return self.__papa

    def getElem(self):
        return self.__dato

    def setDer(self, lig):
        self.__der = lig

    def setIzq(self, lig):
        self.__izq = lig

    def setPapa(self, lig):
        self.__papa = lig

    def setElem(self, da):
        self.__dato = da

    def cuelga(self, n):
        if (n == None):
            return
        n.setPapa(self)
        if n.getElem() <= self.__dato:
            self.__izq=n;
        else:
            self.__der=n;

    def suma(self, n):
        if n.getElem() <= self.__dato:
            self.fe =self__.fe-1
        else:
            self.fe =self.__fe+1

    def toString(self):
        return self.__dato + ""

def nuevoN(dato=0):
    n=NodoAVL(dato)
    return n


class ArbolAVL:
    __variable = "raiz", "contador"

    def __init__(self):
        self.__contador=0
        self.__raiz=nuevoN()

    def inserta(self, elem):
        nuevo = nuevoN(elem)
        actual = nuevoN()
        papa = nuevoN()
        actual = self.__raiz
        papa = self.__raiz

        if self.__raiz == None:
            self.__raiz = nuevo
        else:
            while actual != None:
                papa = actual
                if elem < actual.getElem():
                    actual = actual.getIzq()
                else:
                    actual = actual.getDer()
            papa.cuelga(nuevo)
            factoresNuevos(nuevo)
        self.__contador=self.__contador+1

def factoresNuevos(actual):
    termino = False
    papa = actual.getPapa()
    while (not (papa == None) and (not termino)):
        fe = papa.getFe()
        if actual == papa.getDer():
            papa.setFe(fe + 1)
        else:
            papa.setFe(fe - 1)

        if papa.getFe() == 0:
            termino = True
        if papa.getFe() == 2 or papa.getFe() == -2:
            print("Rota")
            termino = True
            actual = rotar(papa)
            papa = actual.getPapa()
        else:
            actual = papa
            papa = actual.getPapa()



a = ArbolAVL()
a.inserta(1)
a.inserta(-3)
a.inserta(-2)
a.inserta(-1)
a.inserta(4)
a.inserta(3)

#a.eliminaIterativo(1);
a.inserta(5)
a.inserta(6)

#a.imprime();

print("\nRaiz: ")
print("Fe: " + "\n")
print("\nPor niveles:\n")
#a.imprimeNiveles();
#a.eliminaIterativo(3);
#a.imprimeNiveles();
# arbolesAVL
