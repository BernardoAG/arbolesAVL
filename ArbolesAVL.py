class NodoAVL:
    __variable= "dato", "izq","der","papa", "fe"

    def __init__(self, dat=0):
        self.__fe = 0
        self.__dato = dat


    def getFe(self):
        return fe

    def setFe(self, fe):
        self.__fe = fe;

    def getDer(self):
        return self.der

    def getIzq(self):
        return self.izq

    def getPapa(self):
        return self.papa

    def getElem(self):
        return self.dato

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
        if n.getElem() <= dato:
            self.__izq=n;
        else:
            self.__der=n;

    def suma(self, n):
        if n.getElem() <= self.__dato:
            self.fe =self.fe-1
        else:
            self.fe =self.fe+1

    def toString(self):
        return self.dato + ""

def nuevoN(dato=0):
    n=NodoAVL(dato)
    return n


class ArbolAVL:
    __variable = "raiz", "contador"

    def __init__(self):
        self.contador=0
        self.raiz=nuevoN()

    def inserta(self, elem):
        nuevo = nuevoN(elem)
        actual = nuevoN()
        papa = nuevoN()
        actual = self.raiz
        papa = self.raiz

        if self.raiz == None:
            self.raiz = nuevo
        else:
            while actual != None:
                papa = actual
                if elem < actual.getElem():
                    actual = actual.getIzq()
                else:
                    actual = actual.getDer()
            papa.cuelga(nuevo)
            factoresNuevos(nuevo)
        self.contador=self.contador+1


a = ArbolAVL()
a.inserta(1)
a.inserta(-3)
a.inserta(-2)
a.inserta(-1)
a.inserta(4)
a.inserta(3)

a.eliminaIterativo(1);
a.inserta(5);
a.inserta(6);

a.imprime();

System.out.println("\nRaiz: " + a.raiz.getElem());
System.out.println("Fe: " + a.raiz.getFe() + "\n");
System.out.println("\nPor niveles:\n");
a.imprimeNiveles();
a.eliminaIterativo(3);
a.imprimeNiveles();
# arbolesAVL
