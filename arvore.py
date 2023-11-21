import no as No
import pilha as Pilha

class Arvore():
  def __init__(self):
    self.raiz = None
  
  def busca(self, pont, chave):
    if pont.valor == chave:
      f = 1
    else:
      if chave < pont.valor:
        if pont.esq == None:
          f = 2
        else:
          pont = pont.esq
          pont, f = self.busca(pont, chave)
      else:
        if pont.dir == None:
          f = 3
        else:
          pont = pont.dir
          pont, f = self.busca(pont, chave)    
    return pont, f    
    pont = self.raiz
    while pont != None:
      print(f'--> {pont.valor}')
      if pont.dir != None:
        pilhaPreOrdem = Pilha()
        pilhaPreOrdem.empilhar(pont.dir)
      if pont.esq != None:
        pont = pont.esq
      else:
        pont = pilhaPreOrdem.desempilhar()
        