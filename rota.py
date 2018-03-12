class rota  :
    def rotar(self, nodo)  :
        resp = null 
        if (nodo.getIzq() != null and nodo.getFe() < -1 and nodo.getIzq().getFe() < 0)  :
            pi = nodo.getPapa() 
            alfa = nodo 
            beta = nodo.getIzq() 
            gamma = beta.getIzq() 
            a = gamma.getIzq() 
            b = gamma.getDer() 
            c = beta.getDer() 
            d = alfa.getDer() 
            gamma.setDer(null) 
            gamma.setIzq(null) 
            gamma.cuelga(a) 
            gamma.cuelga(b) 
            alfa.setDer(null) 
            alfa.setIzq(null) 
            alfa.cuelga(c) 
            alfa.cuelga(d) 
            beta.cuelga(gamma) 
            beta.cuelga(alfa) 
            beta.setPapa(pi) 
            if (pi != null)  :
                pi.cuelga(beta) 
            else  :
                raiz = beta 
            actualizarFeHeight(beta) 
            actualizarFeHeight(gamma) 
            actualizarFeHeight(alfa) 
            resp = beta 

        if (nodo.getIzq() != null and nodo.getIzq().getFe() > 0 and nodo.getFe() < -1)  :
            pi=nodo.getPapa() 
            alfa=nodo
            beta=alfa.getIzq()
            gamma=beta.getDer()
            a=beta.getIzq() 
            b=gamma.getIzq() 
            c=gamma.getDer() 
            d=alfa.getDer() 
            if (pi != null)  :
                pi.cuelga(gamma) 
            else  :
                raiz =gamma 
            gamma.cuelga(beta) 
            gamma.cuelga(alfa) 
            gamma.setPapa(pi) 
            beta.setIzq(null) 
            beta.cuelga(a) 
            beta.setDer(null) 
            beta.cuelga(b) 
            alfa.setIzq(null) 
            alfa.setDer(null) 
            alfa.cuelga(c) 
            alfa.cuelga(d) 
            actualizarFeHeight(gamma) 
            actualizarFeHeight(alfa) 
            actualizarFeHeight(beta) 
            resp= gamma 

        if (nodo.getDer() != null and nodo.getFe() > 1 and nodo.getDer().getFe() > 0)  :
            pi = nodo.getPapa() 
            alfa = nodo 
            beta = nodo.getDer() 
            gamma = beta.getDer() 
            a = alfa.getIzq() 
            b = beta.getIzq() 
            c = gamma.getIzq() 
            d = gamma.getDer() 
            gamma.setDer(null) 
            gamma.setIzq(null) 
            gamma.cuelga(c) 
            gamma.cuelga(d) 
            alfa.setDer(null) 
            alfa.setIzq(null) 
            alfa.cuelga(a) 
            alfa.cuelga(b) 
            beta.setPapa(pi) 
            beta.cuelga(gamma) 
            beta.cuelga(alfa) 
            if (pi != null)  :
                pi.cuelga(beta) 
            else  :
                raiz=beta 
            actualizarFeHeight(gamma) 
            actualizarFeHeight(alfa) 
            actualizarFeHeight(beta) 
            resp= beta 

        if (nodo.getDer() != null and nodo.getDer().getFe() < 0 and nodo.getFe() > 1)  :
            pi=nodo.getPapa() 
            alfa=nodo 
            beta=alfa.getDer() 
            gamma=beta.getIzq() 
            a=alfa.getIzq() 
            b=gamma.getIzq() 
            c=gamma.getDer() 
            d=beta.getDer() 
            if (pi != null)  :
                pi.cuelga(gamma) 
            else  :
                raiz=gamma 
            gamma.cuelga(beta) 
            gamma.cuelga(alfa) 
            gamma.setPapa(pi) 
            beta.setIzq(null) 
            beta.cuelga(c) 
            beta.setDer(null) 
            beta.cuelga(d) 
            alfa.setIzq(null) 
            alfa.setDer(null) 
            alfa.cuelga(a) 
            alfa.cuelga(b) 
            actualizarFeHeight(gamma) 
            actualizarFeHeight(alfa) 
            actualizarFeHeight(beta) 
            resp= gamma 
        return resp 


    def balanceaE(self, nodo)  :
        termine = false
        while (not (nodo.getPapa() == None) and not termine)  :
            e = nodo.getPapa().getFe()
            papa = nodo.getPapa()
            if (nodo == papa.getIzq())  :
                nodo.getPapa().setFe(e+1)
            if (e == 0)  :
                termine = true
            else  :
                papa.setFe(e-1)
                if (e == 0)  :
                    termine = true
            if (Math.abs(papa.getFe()) == 2)  :
                papa = rotar(papa)
                if (Math.abs(papa.getFe()) == 1)  :
                    termine=true
            nodo = papa 

    def imprime(self)  :
        self.imprime2(self.__raiz)


    def imprime2(self, temp)  :
        if(not (temp == None))  :
            self.imprime2(temp.getIzq())
            print(temp.getElem())
            self.imprime2(temp.getDer())

    def imprimeNiveles(self):
        self.imprimeNiveles2(self.__raiz)

    def imprimeNiveles2(self, nodo):
        tam = getHeight(nodo)
        tam = (int)(Math.pow(2, tam))
        i = 0
        j = 0
        arre[0] = nodo 
        while (i < tam - 1):
            aux=arre[j]
            print(aux.getElem()+", ")
            arre[i+1]=aux.getIzq()
            arre[i+2]=aux.getDer()
            i=i+2
            j=j+1
        while (j < tam - 1):
            aux=arre[j]
            if (aux != null):
                print(aux.getElem()+", ")
            j=j+1




