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

  def inclusao(self, chave):
    if self.raiz == None:
      novo = No()
      novo.valor = chave
      self.raiz = novo
    else:
      pont = self.raiz
      pont, f = self.busca(pont, chave)
      if f == 1:
        print(f'A chave --> {chave} <-- já está na árvore !')
      else:
        novo = No()
        novo.valor = chave
        if f == 2:
          pont.esq = novo
        else:
          pont.dir = novo
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
        