import Conjunto
from operator import itemgetter

a = Conjunto.Conjunto()
a.insereValor(4)
a.insereValor(3)
a.insereValor([3,4])
a.insereValor(1)
a.insereNome("A")
a.imprime()
print()

b = Conjunto.Conjunto()
b.insereNome("B")
b.insereValor(5)
b.insereValor([3,4])
b.imprime()
print()

c = Conjunto.Conjunto()
c.insereNome("C")
c.insereValor(6)
c.insereValor(5)
c.insereValor([7,4])
c.imprime()
print()

# print("B e A: ", t.contemElemento(s))
# print("A e B: ", s.contemElemento(t))

# print("A contem B:", t.contem(s))
# print("B contem A:", s.contem(t))

# print("A esta Contido Propriamente Em B:", t.estaContidoPropriamenteEm(s))
# print("B esta Contido Propriamente Em A:", s.estaContidoPropriamenteEm(t))
'''
op=''
dicionario = {}
while(op != 'sair'):
    op=''
    op = input("Informe a opercação de União: ")
    
    if op in dicionario:
        print(dicionario[op])
    else:
        conjResultante = a.uniao(b).uniao(c)
        lista = Conjunto.Conjunto.permutaChave(op)
        for i in lista:
            dicionario[i] = conjResultante
        print(dicionario[conjResultante.nome].lista)
print("Uniao A v B")
print(a.uniao(b).lista)
print()
print("Interseccao A ^ B")
print(a.interseccao(b).lista)
print()
print("Diferenca A - B")
print(a.diferenca(b).lista)
print()
print("Complemento de ~A U=(A U B)")
print(a.complemento(a.uniao(b)).lista)
print()
print("SubConjuntos de C")
for i in c.subconjuntos():
    print(i if len(i)>0 else i)
print()
print("Plano Cartesiano B e C {}".format(b.planoCartesiano(c)))

print()
print("uniaoDisjunta B e C {}".format(b.uniaoDisjunta(c).lista))'''
 
