# Projeto IF Quest
# Aula 3 - POO


# Classe com atributos e comportamentos de cada pesonagem
class Personagem:
    def __init__(self, nome):
        self._nome = nome
        self._vida = 100
        self._nivel = 1
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        if (vida < 0):
            self._vida = 0
        elif (vida > 100):
            self._vida = 100
        else:
            self._vida = vida
        
    
    @property
    def nivel(self):
        return self._nivel
    

    @nivel.setter
    def nivel(self, nivel):
        if (nivel < 1):
            self._nivel = 1
        else:
            self._nivel = nivel
        



# Criando o personagem
teste = Personagem("Scrible")

# Testando o getter
print("Nome: ", teste.nome)
print("Vida: ", teste.vida)
print("Nivel: ", teste.nivel)

print("\nAlterando os valores dos atributos...\n")

# Testando o setter
teste.nome = "Scrible 2"
teste.vida = 150
teste.nivel = 0

# Testando novamente os getters após alteração
print("Nome: ", teste.nome)
print("Vida: ", teste.vida)
print("Nivel: ", teste.nivel)

# Testando a alteração de vida para um valor negativo
teste.vida = -50

# Testando novamente os getters após alteração 
print("\nApós tentar alterar a vida para um valor negativo:")
print("Nome: ", teste.nome)
print("Vida: ", teste.vida)
print("Nivel: ", teste.nivel)