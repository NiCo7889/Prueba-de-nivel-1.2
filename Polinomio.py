"""
Ahora quedará a cargo del alumno completar la funcionalidad del TDA polinomio, dado que solo se desarrollaron algunas funciones, agregándole la capacidad de eliminar términos,
y de determinar si en un polinomio existe un término, para evitar tener que llamar a la función “obtener_valor” y luego consultar si el resultado es distinto de cero para
determinar si el polinomio tiene ese término o no. Esta última debe ser una función booleana.
"""

class Nodo(object):
    # Clase nodo simplemente enlazado
    info, sig = None, None

class datoPolinomio(object):
    # Clase dato polinomio
    def __init__(self, valor, termino):
        # Crea un dato polinomio con un valor termino
        self.valor  = valor
        self.termino = termino

class Polinomio(object):
    # Clase polinomio
    def __init__(self):
        # Crea un polinomio de grado cero
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, valor, termino):
        # Agrega un termino y su valor al polinomio
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None and actual.sig.info.termino > termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        # Modifica un termino del polinomio
        aux = polinomio.termino_mayor
        while (aux != None and aux.info.termino != termino):
            aux = aux.sig
        aux.sig.valor = valor

    def obtener_valor(polinomio, termino):
        # Devuelve el valor de un termino del polinomio
        aux = polinomio.termino_mayor
        while (aux != None and aux.info.termino  > termino):
            aux = aux.sig
        if (aux != None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
        
    def mostrar(polinomio):
        # Muestra el polinomio
        aux = polinomio.termino_mayor
        pol = ""
        if(aux is not None):
            while(aux is not None):
                signo = ""
                if(aux.info.valor >= 0):
                    signo += "+"
                pol += signo + str(aux.info.valor)+"x^"+str(aux.info.termino)
                aux = aux.sig
        return pol
    
    def sumar(polinomio1, polinomio2):
        # Suma dos polinomios y devuelve el resultado
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if (total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    
    def restar(polinomio1, polinomio2):
        # Resta dos polinomios y devuelve el resultado
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) - Polinomio.obtener_valor(polinomio2, i)
            if (total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
    

    def multiplicar(polinomio1, polinomio2):
        # Multiplica dos polinomios y devuelve el resultado
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while (pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if (Polinomio.obtener_valor(paux, termino) != 0):
                   valor += Polinomio.obtener_valor(paux, termino)
                   Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def dividir(polinomio1, polinomio2):
        # Divide dos polinomios y devuelve el resultado
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while (pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino - pol2.info.termino
                valor = pol1.info.valor / pol2.info.valor
                if (Polinomio.obtener_valor(paux, termino) != 0):
                   valor += Polinomio.obtener_valor(paux, termino)
                   Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def eliminar_termino(polinomio, termino):
        # Elimina un termino del polinomio
        aux = polinomio.termino_mayor
        if (aux is not None and aux.info.termino == termino):
            polinomio.termino_mayor = aux.sig
        else:
            while (aux.sig is not None and aux.sig.info.termino != termino):
                aux = aux.sig
            if (aux.sig is not None and aux.sig.info.termino == termino):
                aux.sig = aux.sig.sig

    def existe_termino(polinomio, termino):
        # Determina si existe un termino en el polinomio
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return True
        else:
            return False
        
# Prueba de la clase Polinomio

deprueba1 = Polinomio()
deprueba1.agregar_termino(6, 14)
deprueba1.agregar_termino(10, -4)

deprueba2 = Polinomio()
deprueba2.agregar_termino(8, 14)
deprueba2.agregar_termino(2, 2)

print(deprueba1.mostrar())
print(deprueba2.mostrar())
print(deprueba1.obtener_valor(14))
print(deprueba2.obtener_valor(2))


deprueba3 = Polinomio.sumar(deprueba1, deprueba2)
print(deprueba3.mostrar())


deprueba4 = Polinomio.multiplicar(deprueba1, deprueba2)
print(deprueba4.mostrar())

deprueba5 = Polinomio.restar(deprueba2, deprueba1)
print(deprueba5.mostrar()) 

deprueba1.eliminar_termino(3)
print(deprueba1.mostrar()) 

print(deprueba1.existe_termino(5))
print(deprueba2.existe_termino(3))

p6 = Polinomio.dividir(deprueba1, deprueba2)
print(p6.mostrar())