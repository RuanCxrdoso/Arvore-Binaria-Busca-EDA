from no import No
from pilha import Pilha

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
      print(f'{novo.valor} foi incluído na raíz !') # somento para verificação no terminal
    else:
      pont = self.raiz
      pont, f = self.busca(pont, chave)
      if f == 1:
        print(f'A chave --> {chave} <-- já está na árvore !') # somento para verificação no terminal
      else:
        novo = No()
        novo.valor = chave
        if f == 2:
          pont.esq = novo
          print(f'{novo.valor} foi incluído como filho esquerdo !') # somento para verificação no terminal
        else:
          pont.dir = novo
          print(f'{novo.valor} foi incluído como filho direito !') # somento para verificação no terminal

  def preOrdem(self):
    pont = self.raiz
    pilhaPreOrdem = Pilha()
    while pont != None:
      print(f'-> {pont.valor}', end=' ')
      if pont.dir != None:
        pilhaPreOrdem.empilhar(pont.dir)
      if pont.esq != None:
        pont = pont.esq
      else:
        pont = pilhaPreOrdem.desempilhar()