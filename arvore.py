from noArvore import No
from pilha import Pilha

class Arvore:
  def __init__(self):
    self.raiz = None
    self.menu()
  
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
      print(f'\n{novo.valor} foi incluído na raíz da árvore!\n') # somente para verificação no terminal
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
          print(f'\n{novo.valor} foi incluído como filho esquerdo do seu pai {pont.valor}!\n') # somente para verificação no terminal
        else:
          pont.dir = novo
          print(f'\n{novo.valor} foi incluído como filho direito do sei pai {pont.valor} !\n') # somente para verificação no terminal

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
        print(f"\nO nó com a chave {chave} foi deletado !")
        del pont
    else:
        print(f"\nA chave {chave} não foi encontrada na árvore!")

  def preOrdem(self):
    pont = self.raiz
    pilhaPreOrdem = Pilha()
    print('\nCaminhamento Pré-Ordem:')
    while pont != None:
      print(f'-> {pont.valor}', end=' ')
      if pont.dir != None:
        pilhaPreOrdem.empilhar(pont.dir)
      if pont.esq != None:
        pont = pont.esq
      else:
        pont = pilhaPreOrdem.desempilhar()
    print('\n')

  def menu(self):
    print('**' * 43)
    print('**' * 15, 'ÁRVORE BINÁRIA DE BUSCA', '**' * 15)
    print('**' * 43)
    print('\n MENU DE SELEÇÃO:')
    selecao = True
    while selecao:
        print('1) Inclusão', '\n2) Exclusão', '\n3) Caminhamento Pré-Ordem', '\n4) Estrutura da Árvore', '\n5) Fim')
        selecao = int(input('-> '))
        if selecao == 1:
          valor = int(input('\nDigite o valor a ser inserido na árvore: '))
          self.inclusao(valor)
        elif selecao == 2:
          valor = int(input('\nDigite o valor a ser excluído da árvore: '))
          self.exclusao(valor)
          print('\n')
        elif selecao == 3:
          self.preOrdem()
        elif selecao == 4:
          # Em desenvolvimento
          pass
        elif selecao == 5:
          print('\n-->', 'Programa encerrado !', '<--\n')
          selecao = False
        else:
          print('\n-->', 'Opção inválida !', '<--\n')

arvore = Arvore()
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