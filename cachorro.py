class Cachorro:
    nome = None
    cor = None
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Canil:
    cachorros = None
    def __init__(self):
        self.cachorros = []
    def adicionarCachorro(self, nome, cor):
        self.cachorros.append(Cachorro(nome, cor))
    def imprimeInfo(self, nomeArquivo):
        '''Imprime as informações dos cachorros do canil
           no arquivo informado'''
        f = open(nomeArquivo, "w")
        for c in self.cachorros:
            f.write("Nome: %s\tCor: %s\n"%(c.nome, c.cor))
        f.close()

#### programa principal:
canil = Canil()
canil.adicionarCachorro("Totó", "preto")
canil.adicionarCachorro("Fifi", "branca")
canil.adicionarCachorro("Malvado", "marrom")
canil.adicionarCachorro("Leão", "amarelo")
canil.imprimeInfo("Aula07-cachorros.txt")
canil.adicionarCachorro("Bilú", "rosa")
canil.imprimeInfo("Aula07-cachorros.txt")



        
