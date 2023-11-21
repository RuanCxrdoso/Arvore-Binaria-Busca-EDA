from noPilha import No

class Pilha():
  def __init__(self):
    # self.pilha = [0] * 1000
    # self.max = 1000
    self.topo = None

  def empilhar(self, chave):
    novo = No()
    novo.valor = chave
    if self.topo == None:
      self.topo = novo
    else:
      novo.prox = self.topo
      self.topo = novo

  def desempilhar(self):
    if self.topo != None:
      aux = self.topo.valor
      self.topo = self.topo.prox
      return aux
    else:
       print('|')

  # def __str__(self):
  #       return "[" + ", ".join(map(str, self.pilha)) + "]"
