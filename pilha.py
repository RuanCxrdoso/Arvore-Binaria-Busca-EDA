class Pilha():
  def __init__(self):
    self.pilha = [0] * 1000
    self.max = 1000
    self.topo = -1

  def empilhar(self, chave):
    if self.topo < self.max:
      self.topo += 1
      self.pilha[self.topo] = chave
    else:
       print('Pilha cheia !')

  def desempilhar(self):
    chave = 0
    if self.topo >= 0:
       chave = self.pilha[self.topo]
       self.topo -= 1
       return chave
    else:
       print('|')

  # def __str__(self):
  #       return "[" + ", ".join(map(str, self.pilha)) + "]"
