class NohTabelaHash:
    def __init__ (self, chave):
        self.chave = chave
        self.proximo = None

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho
        self.linguagens_removidas = []
    
    def funcao_hash(self, chave):
        return sum(ord(c) for c in chave) % self.tamanho
    
    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        
        if self.tabela[indice] is None:
            self.tabela[indice] = NohTabelaHash(chave)
        else:
            atual = self.tabela[indice]

            while atual.proximo:
                atual = atual.proximo
            atual.proximo = NohTabelaHash(chave)

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        atual = self.tabela[indice]

        while atual:

            if atual.chave == chave:
                return True
            atual = atual.proximo
        return False
    
    def remover(self, chave):
        indice = self.funcao_hash(chave)
        atual = self.tabela[indice]
        anterior = None

        while atual:

            if atual.chave == chave:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.tabela[indice] = atual.proximo
                self.linguagens_removidas.append(chave)
                return True
            anterior = atual
            atual = atual.proximo
        return False
    def listar_linguagens(self):
        linguagens = []

        for noh in self.tabela:
            atual = noh

            while atual:
                linguagens.append((atual.chave))
                atual = atual.proximo
        return linguagens
def interface_usuario():
    Minha_tabela_hash = TabelaHash(15)

    while True:
        print("\nMenu:")
        print("1-> Inserir uma linguagem")
        print("2-> Remover uma linguagem")
        print("3-> Buscar uma lnguagem")
        print("4-> Listar todas as linguagens cadastradas")
        print("5-> Listar lingugens removidas")
        print("6-> Sair do programa")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            linguagem = input("Digite o nome da lingugagem a inserir: ")
            Minha_tabela_hash.inserir(linguagem)
            print("{} inserida com sucesso.".format(linguagem))

        elif escolha == "2":
            linguagem = input("Digite o nome da linguagem que deseja remover: ")

            if Minha_tabela_hash.remover(linguagem):
                print("{} removido com sucesso.".format(linguagem))
            else:
                print("Não foi possível encontrar {} na tabela".format(linguagem))
            
        elif escolha == "3":
            linguagem = input("Digite o nome da linguagem que deseja buscar: ")

            if Minha_tabela_hash.buscar(linguagem):
                print("A linguagem {} está cadastrada.".format(linguagem))
            else:
                print("A linguagem {} não está cadastrada.".format(linguagem))
        
        elif escolha == "4":
            linguagens = Minha_tabela_hash.listar_linguagens()

            if linguagens:
                print("Todas as linguagens cadastradas são: {}".format(linguagens))

            else:
                print("Nenhuma linguagem cadastrada.")

        elif escolha == "5":
            if Minha_tabela_hash.linguagens_removidas:
                print("Linguagens removidas: ")

                for linguagem in Minha_tabela_hash.linguagens_removidas:
                    print(linguagem)
            else:
                print("Nenhuma linguagens removidas.")

        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha entre 1 e 6.")

interface_usuario()

