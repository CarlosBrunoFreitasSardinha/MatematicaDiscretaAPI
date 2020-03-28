import copy
import itertools
from operator import itemgetter


def ordenaLista(listaConj):
    i=0
    while i<len(listaConj):
        j=i+1
        if  isinstance(listaConj[i], list):
            elementoI = listaConj[i][0]
        else:
            elementoI = listaConj[i]
        while j<len(listaConj):
            if  isinstance(listaConj[j], list):
                elementoj = listaConj[j][0]
            else:
                elementoj = listaConj[j]
            if elementoI>elementoj:
                aux = listaConj[i]
                listaConj[i] = listaConj[j]
                listaConj[j] = aux
                elementoI = aux
            j+=1
        i+=1
    return listaConj
def permutaChave(item):
    item = item.replace(" ", "").split("(", "").split(")", "")
    lista = item.split("U")
    listaFinal = []
    permutacao = itertools.permutations(lista, len(lista))
    for permuta in permutacao:
        listaFinal.append(permuta)
    return chaveString(listaFinal)

def chaveString(listaChaves):
    listaFinal = []
    for chave in listaChaves:
        listaFinal.append((" U ".join(str(i) for i in chave)))
    return listaFinal



class Conjunto:
    def __init__(self):
        self.lista = []
        self.nome=""

    def insereValor(self, valor):
        self.lista.append(valor)

    def insereNome(self, nome):
        self.nome = nome

    def tamanho(self):
        return len(self.lista)

    def imprime(self):
        if len(self.nome)>1:
            print("Conjunto "+ '({}){}'.format(self.nome[:5], self.nome[5:]) +": ")
        else:
            print("Conjunto "+ self.nome +": ")
        print( self.lista)

    def contemElemento(self, item):
        for i in self.lista:
            if i==item:#if i==item.lista[0] if isinstance(item, lista) else i==item:
                return True
        return False
    
    def contem(self, conjunto):
        for i in conjunto.lista:
            flag = 0 
            for j in self.lista:
                if j==i:
                    flag = 1
            if flag==0: return False
        return True
    
    def estaContidoPropriamenteEm(self, conjunto):
        if conjunto.contem(self):
            if self.contem(conjunto)==False:
                return True
        return False
    
    def invalidarCache(self):
        self = {}
    
    def uniao(self, conjB):
        #verifica possiveis vazios
        if len(self.lista) ==0 and len(conjB.lista) == 0:
            return self

        elif len(self.lista) == 0 and len(conjB.lista) > 0:
            return conjB

        elif len(self.lista) > 0 and len(conjB.lista) == 0:
            return self
        #verifica se um contem o outro  ////// idempotencia
        elif self.contem(conjB):
            return self

        elif conjB.contem(self):
            return conjB

        result = copy.deepcopy(self)

        for i in conjB.lista:
            if result.contemElemento(i)==False:
                result.lista.append(i)
        if(len(conjB.nome.upper().split('U'))==1):
            result.nome = self.nome + " U " + conjB.nome
        else:
            result.nome = self.nome + " U (" + conjB.nome+" )"
        return result
    
    def interseccao(self, conjB):
        #verifica possiveis vazios
        if len(self.lista) ==0 or len(conjB.lista) == 0:
            return self

        elif len(self.lista) == 0 and len(conjB.lista) > 0:
            return conjB

        elif len(self.lista) > 0 and len(conjB.lista) == 0:
            return self
        #verifica se um contem o outro  ////// idempotencia
        elif self.contem(conjB):
            return conjB

        elif conjB.contem(self):
            return self

        result = Conjunto()

        for i in self.lista:
            if conjB.contemElemento(i):
                result.lista.append(i)
        if(len(conjB.nome.upper().split('^'))==1):
            result.nome = self.nome + " ^ " + conjB.nome
        else:
            result.nome = self.nome + " ^ (" + conjB.nome+" )"
        return result
    
    def diferenca(self, conjB):
        #verifica possiveis vazios
        if len(self.lista) ==0 and len(conjB.lista) == 0:
            return self

        elif len(self.lista) == 0 and len(conjB.lista) > 0:
            return conjB

        elif len(self.lista) > 0 and len(conjB.lista) == 0:
            return self
        #verifica se um contem o outro  ////// idempotencia
        elif self.contem(conjB) and conjB.contem(self):
            return Conjunto()

        result = Conjunto()

        for i in self.lista:
            if conjB.contemElemento(i)==False:
                result.lista.append(i)
        if(len(conjB.nome.upper().split('-'))==1):
            result.nome = self.nome + " - " + conjB.nome
        else:
            result.nome = self.nome + " - (" + conjB.nome + " )"
        return result
    
    def complemento(self, universo):
        return universo.diferenca(self)

    def subconjuntos(self):
        listaFinal = []
        lista = []
        if [] not in self.lista: listaFinal.append([])
        for i in range(1, len(self.lista)):
            permutacao = itertools.permutations(self.lista, i)
            for permuta in permutacao:
                for itens in permuta:
                    lista.append(itens)
                ordenaLista(lista)
                if lista not in listaFinal:
                    listaFinal.append(lista)
                lista = []
        listaFinal.append(self.lista)
        return listaFinal

    def planoCartesiano(self, conjB):
        listaFinal = []
        for i in self.lista:
            for j in conjB.lista:
                listaFinal.append([i,j])
        return listaFinal
    
    def uniaoDisjunta(self, conjB):
        conjFinal = Conjunto()
        for i in self.lista:
            conjFinal.lista.append([i, self.nome])
        for i in conjB.lista:
            conjFinal.lista.append([i, conjB.nome])
        return conjFinal
