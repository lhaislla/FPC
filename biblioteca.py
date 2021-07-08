# classes Biblioteca e Livro:
# - A Biblioteca 0em uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.
class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0
    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor 
    def __cmp__(self, livro):
        return cmp(self.codigo, livro.codigo)
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis
class Biblioteca:
    alugados = []
    disponiveis = []
    def inserir(self, livro):
        self.disponiveis.append(livro)
    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)
    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)
    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)
    def getunir(self):
	    return(self.disponiveis[0:] + self.alugados[0:])
#Metodo do Merge sort para ordenação:            
    def livrosOrdenadosPeloNome(self, valor, inicio=0, fim=None):
        
        if fim is None:
            fim = len(valor)
        if (fim - inicio > 1):
            meio = (fim + inicio) //2
            self.livrosOrdenadosPeloNome(valor, inicio, meio)
            self.livrosOrdenadosPeloNome(valor, meio, fim)
            self.merge(valor, inicio, meio, fim)
        return(valor)  
    def merge(self,valor, inicio, meio, fim):
        esq = valor[inicio:meio]
        dir = valor[meio:fim]
        topo_esq,topo_dir = 0, 0
        for k in range(inicio,fim):
            if topo_esq >= len(esq):
                valor[k] = dir[topo_dir]
                topo_dir = topo_dir + 1
            elif topo_dir >= len(dir):
                valor[k] = esq[topo_esq]
                topo_esq = topo_esq + 1
            elif esq[topo_esq] < dir[topo_dir]:
                valor[k] = esq[topo_esq]
                topo_esq = topo_esq + 1
            else:
                valor[k] = dir[topo_dir]
                topo_dir = topo_dir +1
#Programa Principal(Tratamento das entradas):
biblioteca = Biblioteca()
entrada = input("").split("→")
tam = len(entrada)
n = int(entrada[0])
entrada = entrada[1:tam]
lista_completa = []
info_nomes = []
chaves = {}
while n != 0:
    codigo = entrada[0]
    lista_completa.append(codigo)
    entrada.pop(0)
    nome =  entrada[0]
    entrada.pop(0)
    info_nomes.append(nome)
    lista_completa.append(nome)
    autor = entrada[0]
    lista_completa.append(autor)
    valor = biblioteca.livrosOrdenadosPeloNome(info_nomes)
    entrada.pop(0)
    livro_novo = Livro(codigo,nome,autor)
    chaves[livro_novo.nome] = livro_novo.codigo
    biblioteca.inserir(livro_novo)
    n-=1
  
# Tratamento da Saída:
cont = 0 
temp = []
for ordena in valor:
    resultado = chaves.get(info_nomes[cont])
    temp.append(resultado)
    cont+=1
saida = ' '.join(temp)
print(saida)

#Função Unir(mesclar) Alugados e Disponiveis:
    #mesclar=biblioteca.getunir()
    #mesclar.livrosOrdenadosPeloNome
    #print(g)

# Ordenar livros alugados e disponiveis: 
    #biblioteca.livrosOrdenadosPeloNome(mesclar)

