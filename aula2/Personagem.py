# Projeto IF Quest
# Aula 2 - POO

# Classe com atributos e comportamentos de cada pesonagem
class Personagem:
    def __init__(self):
        self.nome = ""
        self.vida = 100
        self.forca = 10


    def receberDano(self, dano):
        self.vida -= dano
        print(f"{self.nome} sofreu {dano} de dano.")


    def estaVivo(self):
        return self.vida > 0


    def ficha(self):
        return f"Nome: {self.nome}\nVida: {self.vida}\nForça: {self.forca}"


    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome} com {self.forca} de força.")
        alvo.receberDano(self.forca)



# Programa principal
if __name__ == "__main__":

    # Criando o herói
    heroi = Personagem()
    heroi.nome = "Scribble"
    #heroi.vida = 100 # já está definido com esse valor inicialmente
    #heroi.forca = 10 # já está definido com esse valor inicialmente

    # Criando o chefe
    chefe = Personagem()
    chefe.nome = "Dragão Azul de Olhos Vermelhos"
    chefe.vida = 200
    chefe.forca = 20

    # Ficha antes da batalha
    print("Ficha do Herói antes da Batalha:")
    print(heroi.ficha())
    print("------------------------------------\n")
    print("Ficha do Chefe antes da Batalha:")
    print(chefe.ficha())
    print("------------------------------------\n")

    print("---------- Início da Batalha ---------\n")


    # Simule uma batalha: cada personagem ataca o outro alternadamente até que um deles morra.
    while heroi.estaVivo() and chefe.estaVivo():
        
        # Ataque do herói
        heroi.atacar(chefe)

        if not chefe.estaVivo():
            print(chefe.nome + " está morto.")
            print(heroi.nome + " venceu a batalha!")
            break
        
        print()

        # Ataque do chefe
        chefe.atacar(heroi)

        if not heroi.estaVivo():
            print(heroi.nome + " está morto.")
            print(chefe.nome + " venceu a batalha!")
            break


    print()


    # Ficha depois da batalha
    print("Ficha do Herói depois da Batalha:")
    print(heroi.ficha())
    print("------------------------------------\n")
    print("Ficha do Chefe depois da Batalha:")
    print(chefe.ficha())
    print("------------------------------------\n")

    print("---------- Fim da Batalha ---------\n")

