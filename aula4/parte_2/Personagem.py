# Projeto IF Quest
# Aula 3 - POO
# Parte 2 - Sobrecarga

# Classe com atributos e comportamentos de cada personagem
class Personagem:

    # Construtor com parâmetros padrão
    def __init__(self, nome="Personagem", vida=100, nivel=1):
        self._nome = nome
        self._vida = vida
        self._nivel = nivel

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
        if vida < 0:
            self._vida = 0
        elif vida > 100:
            self._vida = 100
        else:
            self._vida = vida

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        if nivel < 1:
            self._nivel = 1
        else:
            self._nivel = nivel

    def ficha(self):
        return f"Nome: {self._nome}\nVida: {self._vida}\nNível: {self._nivel}"

    # Método atacar com parâmetro opcional
    def atacar(self, dano=None):
        if dano is None:
            print(self.nome, "realizou um ataque padrão de 10 de dano.")
        else:
            print(self.nome, "realizou um ataque de", dano, "de dano.")



# Classe Item 
class Item:
    # construtor
    def __init__(self,nome, bonus):
        self._nome = nome;

        # validando bonus
        if bonus < 0:
            self._bonus = 0
        else:
            self._bonus = bonus

    # getters
    def obterNome(self):
        return self._nome

    def obterBonus(self):
        return self._bonus

    # descricao
    def __str__(self):
        return f"{self._nome} (+{self._bonus})"





# Criando personagem usando o construtor com valores padrão
personagem1 = Personagem()

# Criando personagem usando o construtor parametrizado
personagem2 = Personagem("Scrible", 80, 5)


print("Personagem criado com construtor padrão:")
print("Nome:", personagem1.nome)
print("Vida:", personagem1.vida)
print("Nivel:", personagem1.nivel)

print("\nPersonagem criado com construtor parametrizado:")
print("Nome:", personagem2.nome)
print("Vida:", personagem2.vida)
print("Nivel:", personagem2.nivel)


print("\nTestando os ataques:")

# Ataque padrão
personagem1.atacar()

# Ataque com dano definido
personagem2.atacar(30)


# testando item
espada = Item("Espada de Aço", 3)
print(espada)

espada_quebrada = Item("Espada quebrada", -10)
print(espada_quebrada)


