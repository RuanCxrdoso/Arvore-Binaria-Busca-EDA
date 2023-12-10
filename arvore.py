from noArvore import No
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
      print(f'{novo.valor} foi incluído na raíz !') # somente para verificação no terminal
    else:
      pont = self.raiz
      pont, f = self.busca(pont, chave)
      if f == 1:
        print(f'A chave --> {chave} <-- já está na árvore !') # somente para verificação no terminal
      else:
        novo = No()
        novo.valor = chave
        if f == 2:
          pont.esq = novo
          print(f'{novo.valor} foi incluído como filho esquerdo !') # somente para verificação no terminal
        else:
          pont.dir = novo
          print(f'{novo.valor} foi incluído como filho direito !') # somente para verificação no terminal

  def buscaExclusao(self, pont, pai, chave, f):
    if pont is None:
        f = 0
    else:
        if chave == pont.valor:
            f = 1
        else:
            if chave < pont.valor:
                pai = pont
                pont, pai, f = self.buscaExclusao(pont.esq, pai, chave, f)
            else:
                pai = pont
                pont, pai, f = self.buscaExclusao(pont.dir, pai, chave, f)

    return pont, pai, f

  def exclusao(self, chave):
    f = None
    pont, pai, f = self.buscaExclusao(self.raiz, None, chave, f)
    if pont is not None:
        if pont.esq is None:
            if pont == self.raiz:
                self.raiz = pont.dir
            else:
                if pont == pai.esq:
                    pai.esq = pont.dir
                else:
                    pai.dir = pont.dir
        else:
            if pont.dir is None:
                if pont == self.raiz:
                    self.raiz = pont.esq
                else:
                    if pont == pai.esq:
                        pai.esq = pont.esq
                    else:
                        pai.dir = pont.esq
            else:
                y = pont.dir
                paiy = pont

                while y.esq is not None:
                    paiy = y
                    y = y.esq
                if paiy != pont:
                    paiy.esq = y.dir
                    y.dir = pont.dir
                y.esq = pont.esq
                if pont == self.raiz:
                    self.raiz = y
                else:
                    if pont == pai.esq:
                        pai.esq = y
                    else:
                        pai.dir = y
        print(f"O nó com a chave {pont.valor} foi deletado !")
        del pont
    else:
        print("A chave não foi encontrada !")

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

# arvore = Arvore()
# arvore.inclusao(25)
# arvore.inclusao(49)
# arvore.inclusao(5)
# arvore.inclusao(32)
# arvore.inclusao(41)
# arvore.inclusao(78)
# arvore.inclusao(2)
# arvore.inclusao(4)
# arvore.inclusao(25)
# arvore.preOrdem()
# arvore.exclusao(100)
# arvore.preOrdem()