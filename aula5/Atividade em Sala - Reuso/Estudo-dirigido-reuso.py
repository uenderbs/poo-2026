# ============================================================
# SISTEMA DE CADASTRO ESCOLAR
# ============================================================
#
# Este código foi adaptado do código desenvolvido na aula anterior, disponível em:
# https://github.com/uenderbs/poo-2026/blob/main/aula4/Estudo_Dirigido.py
# 
# Domínio:
# Sistema de cadastro escolar para representar uma escola e
# diferentes tipos de alunos matriculados.
#
# Superclasse:
# - Aluno
#
# Subclasses:
# - AlunoRegular (é um aluno, logo herda tudo de aluno)
# - AlunoBolsista (é um aluno, logo herda tudo de aluno)
#
#
# Atributos da superclasse Aluno:
# - nome: nome do aluno.
# - idade: idade do aluno.
# - matricula: número ou código de matrícula.
# - nota: nota do aluno, com valor padrão igual a 0.0.
#
# O que cada subclasse possui de próprio:
# AlunoRegular (turma)
# AlunoBolsista (percentual_bolsa)
#
#
# Método abstrato:
# - situacao(): Cada subclasse implementará sua própria regra para informar 
#   a situação acadêmica do aluno.
#
# Método sobrescrito:
# - __str__(): As subclasses sobrescrevem esse método, mas reutilizam a
#   implementação da superclasse usando super().__str__().
#
#
# Polimorfismo:
# - A escola armazenará objetos AlunoRegular e AlunoBolsista
#   na mesma lista.
# - Um único laço chamará situacao() para todos os alunos,
#   sem usar isinstance.
#
# Planejamento de tempo:
# - Planejamento: 10 minutos
# - Implementação 45 minutos
# - Autoavaliação: 5 minutos
#
# Total previsto: 1 hora
#
# Uso de Inteligência Artificial:
# Foi utilizada IA na versão anterior do código para a escrita
# e organização do cabeçalho, descrevendo o domínio, as classes,
# os atributos, as validações e o planejamento de tempo com base
# no código desenvolvido.
#
# Link do chat: https://chatgpt.com/share/6a902960-8da4-83e9-99c2-e0d8464542c8
#
# ============================================================


from abc import ABC, abstractmethod



# Superclasse Aluno
class Aluno(ABC):

    def __init__(self, nome, idade, matricula, nota=0.0):
        self._nome = nome
        self._idade = idade
        self._matricula = matricula
        self._nota = nota

    # Nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome:
            self._nome = nome
        else:
            print("Indique um nome, não pode ser vazio")

    # Idade
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade > 0:
            self._idade = idade
        else:
            print("Indique uma idade válida")

    # Matricula
    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        if matricula:
            self._matricula = matricula
        else:
            print("Indique uma matricula")


    # Nota
    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota >=0 and nota <=10:
            self._nota = nota
        else:
            print("Indique uma nota válida")

    # Impressão
    def __str__(self):
        return (f"Nome: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula} | Nota: {self.nota}")


    # Método abstrato (obrigar as subclasses a implementar seu método situacao())
    @abstractmethod
    def situacao(self):
        pass




# Subclasse aluno regular
class AlunoRegular(Aluno):
    def __init__(self, nome, idade, matricula, turma, nota=0.0):
        # Chama o construtor da superclasse
        super().__init__(nome, idade, matricula, nota)

        # Atributo dessa subclasse
        self._turma = turma


    # Implementação do método abstrato
    def situacao(self):
        if self.nota >= 6:
            return "Aprovado"
        return "Reprovado"

    # Sobrescrever impressão da superclasse
    def __str__(self):
        dados_aluno = super().__str__()
        return (f"{dados_aluno} | Turma: {self._turma}")


# Subclasse aluno bolsista
class AlunoBolsista(Aluno):
    def __init__(self, nome, idade, matricula, percentual_bolsa, nota=0.0):
        # Chama o construtor da superclasse
        super().__init__(nome, idade, matricula, nota)

        # Atributo dessa subclasse
        self._percentual_bolsa = percentual_bolsa

    # Implementação do método abstrato
    def situacao(self):
        # Para manter a bolsa, o aluno precisa de nota 7.
        if self.nota >= 7:
            return "Aprovado e bolsa mantida"
        return "Abaixo da média exigida para a bolsa"

    # Sobrescrever impressão da superclasse
    def __str__(self):
        dados_aluno = super().__str__()
        return (f"{dados_aluno} | Bolsa: {self._percentual_bolsa}%"
        )



# Classe escola
class Escola:

    def __init__(self, nome, cidade):
        self._nome = nome
        self._cidade = cidade
        self._alunos = [] # Coleção de objetos do tipo Aluno

    @property
    def nome(self):
        return self._nome

    @property
    def cidade(self):
        return self._cidade

    @property
    def alunos(self):
        return self._alunos

    def adicionar_aluno(self, aluno):
        self._alunos.append(aluno)

    def listar_alunos(self):
        print(f"\nAlunos matriculados na escola {self.nome}:")
        for aluno in self._alunos:
            print(aluno)

            # Polimorfismo: o mesmo comando para todos os objetos
            # Cada um executa o sua versão do método implementado
            print("Situação:", aluno.situacao())

            print("-" * 60)










escola = Escola("IFGo", "Iporá")


# Aluno regular
aluno1 = AlunoRegular("Uender", 40, "2026105231940016", "1º Período", 6.5)

# Aluno bolsista
aluno2 = AlunoBolsista("Jéssica", 34, "2026105231940017", 100, 6.5)


# Adicionando objetos das duas subclasses na lista de alunos da classe escola
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)


# Teste de polimorfismo (mesma nota, resultados diferentes)
print("Teste polimorfismo")
print(aluno1.situacao())
print(aluno2.situacao())


escola.listar_alunos()


# Teste de validação


print("Nota atual de Uender:", aluno1.nota)

try:
    aluno1.nota = 12
except ValueError as erro:
    print("Alteração recusada:", erro)

print("Nota após a tentativa:", aluno1.nota)



# AUTOAVALIAÇÃO
#
# Critérios não atingidos:
# - Todos
#
# Parte que deu mais trabalho:
# - Entender polimorfismo
#
# Uso de IA:
# - Uso de Ia na versão anterior