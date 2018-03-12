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


def rotar(nodo):
    resp = None
    if (not nodo.getIzq() == None and nodo.getFe() < -1 and nodo.getIzq().getFe() < 0):
        pi = nodo.getPapa()
        alfa = nodo
        beta = nodo.getIzq()
        gamma = beta.getIzq()
        a = gamma.getIzq()
        b = gamma.getDer()
        c = beta.getDer()
        d = alfa.getDer()
        gamma.setDer(None)
        gamma.setIzq(None)
        gamma.cuelga(a)
        gamma.cuelga(b)
        alfa.setDer(None)
        alfa.setIzq(None)
        alfa.cuelga(c)
        alfa.cuelga(d)
        beta.cuelga(gamma)
        beta.cuelga(alfa)
        beta.setPapa(pi)
        if (not pi == None):
            pi.cuelga(beta)
        else:
            this.__raiz = beta
        actualizarFeHeight(beta)
        actualizarFeHeight(gamma)
        actualizarFeHeight(alfa)
        resp = beta

    if (not nodo.getIzq() == None and nodo.getIzq().getFe() > 0 and nodo.getFe() < -1):
        pi = nodo.getPapa()
        alfa = nodo
        beta = alfa.getIzq()
        gamma = beta.getDer()
        a = beta.getIzq()
        b = gamma.getIzq()
        c = gamma.getDer()
        d = alfa.getDer()
        if (not pi  == None):
            pi.cuelga(gamma)
        else:
            this.__raiz = gamma
        gamma.cuelga(beta)
        gamma.cuelga(alfa)
        gamma.setPapa(pi)
        beta.setIzq(None)
        beta.cuelga(a)
        beta.setDer(None)
        beta.cuelga(b)
        alfa.setIzq(None)
        alfa.setDer(None)
        alfa.cuelga(c)
        alfa.cuelga(d)
        actualizarFeHeight(gamma)
        actualizarFeHeight(alfa)
        actualizarFeHeight(beta)
        resp = gamma

    if (not nodo.getDer() == None and nodo.getFe() > 1 and nodo.getDer().getFe() > 0):
        pi = nodo.getPapa()
        alfa = nodo
        beta = nodo.getDer()
        gamma = beta.getDer()
        a = alfa.getIzq()
        b = beta.getIzq()
        c = gamma.getIzq()
        d = gamma.getDer()
        gamma.setDer(None)
        gamma.setIzq(None)
        gamma.cuelga(c)
        gamma.cuelga(d)
        alfa.setDer(None)
        alfa.setIzq(None)
        alfa.cuelga(a)
        alfa.cuelga(b)
        beta.setPapa(pi)
        beta.cuelga(gamma)
        beta.cuelga(alfa)
        if (not pi == None):
            pi.cuelga(beta)
        else:
            this.__raiz = beta
        actualizarFeHeight(gamma)
        actualizarFeHeight(alfa)
        actualizarFeHeight(beta)
        resp = beta

    if (not nodo.getDer() == None and nodo.getDer().getFe() < 0 and nodo.getFe() > 1):
        pi = nodo.getPapa()
        alfa = nodo
        beta = alfa.getDer()
        gamma = beta.getIzq()
        a = alfa.getIzq()
        b = gamma.getIzq()
        c = gamma.getDer()
        d = beta.getDer()
        if (not pi == None):
            pi.cuelga(gamma)
        else:
            this.__raiz = gamma
        gamma.cuelga(beta)
        gamma.cuelga(alfa)
        gamma.setPapa(pi)
        beta.setIzq(None)
        beta.cuelga(c)
        beta.setDer(None)
        beta.cuelga(d)
        alfa.setIzq(None)
        alfa.setDer(None)
        alfa.cuelga(a)
        alfa.cuelga(b)
        actualizarFeHeight(gamma)
        actualizarFeHeight(alfa)
        actualizarFeHeight(beta)
        resp = gamma
    return resp

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
