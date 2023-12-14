from noArvore import No
from pilha import Pilha

class Arvore:
  def __init__(self):
    self.raiz = None
    self._menu()
  
  def _buscaInclusao(self, pont, chave):
    if pont.valor == chave:
      f = 1
    else:
      if chave < pont.valor:
        if pont.esq == None:
          f = 2
        else:
          pont = pont.esq
          pont, f = self._buscaInclusao(pont, chave)
      else:
        if pont.dir == None:
          f = 3
        else:
          pont = pont.dir
          pont, f = self._buscaInclusao(pont, chave)    
    return pont, f    

  def inclusao(self, chave):
    if self.raiz == None:
      novo = No()
      novo.valor = chave
      self.raiz = novo
      print(f'\n{novo.valor} foi incluído na raíz da árvore!\n')
    else:
      pont = self.raiz
      pont, f = self._buscaInclusao(pont, chave)
      if f == 1:
        print(f'A chave --> {chave} <-- já está na árvore !')
      else:
        novo = No()
        novo.valor = chave
        if f == 2:
          pont.esq = novo
          print(f'\n{novo.valor} foi incluído como filho esquerdo do seu pai {pont.valor}!\n')
        else:
          pont.dir = novo
          print(f'\n{novo.valor} foi incluído como filho direito do sei pai {pont.valor} !\n')

  def _buscaExclusao(self, pont, pai, chave, f):
    if pont is None:
        f = 0
    else:
        if chave == pont.valor:
            f = 1
        else:
            if chave < pont.valor:
                pai = pont
                pont, pai, f = self._buscaExclusao(pont.esq, pai, chave, f)
            else:
                pai = pont
                pont, pai, f = self._buscaExclusao(pont.dir, pai, chave, f)

    return pont, pai, f

  def exclusao(self, chave):
    f = None
    pont, pai, f = self._buscaExclusao(self.raiz, None, chave, f)
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
    print('\nCaminhamento Pré-Ordem:\n')
    while pont != None:
      print(f'-> {pont.valor}', end=' ')
      if pont.dir != None:
        pilhaPreOrdem.empilhar(pont.dir)
      if pont.esq != None:
        pont = pont.esq
      else:
        pont = pilhaPreOrdem.desempilhar()
    print('\n')

  def mostrarArvore(self):
    raiz = self.raiz
    def altura(raiz):
      return 1 + max(altura(raiz.esq), altura(raiz.dir)) if raiz else -1  
    xNivel = altura(raiz)
    largura =  pow(2, xNivel+1)

    q = [(raiz, 0, largura, 'c')]
    niveis=[]

    while(q):
      no, nivel, x, alinhamento = q.pop(0)
      if no:            
        if len(niveis) <= nivel:
            niveis.append([])
    
        niveis[nivel].append([no, nivel, x, alinhamento])
        seg = largura // (pow(2,nivel+1))
        q.append((no.esq, nivel+1, x-seg, 'l'))
        q.append((no.dir, nivel+1, x+seg, 'r'))
    print('\nEstrutura da Árvore:\n')
    for i, l in enumerate(niveis):
        pre = 0
        preLinha = 0
        strLinha = ''
        pstr = ''
        seg = largura // (pow(2,i+1))
        for n in l:
            valstr = str(n[0].valor)
            if n[3] == 'r':
                strLinha += ' ' * (n[2]-preLinha-1-seg-seg//2) + '¯' * (seg +seg//2) + '\\'
                preLinha = n[2] 
            if n[3] == 'l':
              strLinha += ' ' * (n[2]-preLinha-1) + '/' + '¯' * (seg+seg//2)  
              preLinha = n[2] + seg + seg // 2
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr
            pre = n[2]
        print(strLinha)
        print(pstr)
  
  def _menu(self):
    print('**' * 43)
    print('**' * 15, 'ÁRVORE BINÁRIA DE BUSCA', '**' * 15)
    print('**' * 43)
    selecao = True
    while selecao:
        print('\n MENU DE SELEÇÃO:')
        print('\n1) Inclusão', '\n2) Exclusão', '\n3) Caminhamento Pré-Ordem', '\n4) Estrutura da Árvore', '\n5) Fim\n')
        menu = int(input('-> '))
        if menu == 1:
          valor = int(input('\nDigite o valor a ser inserido na árvore: '))
          self.inclusao(valor)
        elif menu == 2:
          valor = int(input('\nDigite o valor a ser excluído da árvore: '))
          self.exclusao(valor)
          print('\n')
        elif menu == 3:
          self.preOrdem()
        elif menu == 4:
          self.mostrarArvore()
        elif menu == 5:
          print('\n-->', 'Programa encerrado !', '<--\n')
          selecao = False
        else:
          print('\n-->', 'Opção inválida !', '<--\n')

arvore = Arvore()
