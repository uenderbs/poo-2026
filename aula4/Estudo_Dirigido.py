# ============================================================
# SISTEMA DE CADASTRO ESCOLAR
# ============================================================
#
# Domínio:
# Sistema de cadastro escolar para representar uma escola e
# seus alunos, permitindo armazenar dados dos estudantes,
# realizar validações e listar os alunos matriculados.
#
# Classes:
#
# 1. Aluno
#    Atributos:
#    - nome: nome do aluno.
#    - idade: idade do aluno.
#    - matricula: número ou código de matrícula.
#    - nota: nota do aluno, com valor padrão igual a 0.0.
#
# 2. Escola
#    Atributos:
#    - nome: nome da escola.
#    - cidade: cidade onde a escola está localizada.
#    - alunos: lista contendo os objetos da classe Aluno
#      matriculados na escola.
#
# Validações pretendidas:
# 1. Verificar se a idade informada é maior que zero.
# 2. Verificar se a nota informada está no intervalo de 0 a 10.
#
# Tempo previsto:
# - Planejamento das classes e atributos: 5 minutos
# - Implementação da classe Escola: 20 minutos
# - Implementação da classe Aluno: 10 minutos
# - Implementação das validações: 15 minutos
# - Testes e correções: 10 minutos
#
# - Total previsto: 1 hora
#
#
# Uso de Inteligência Artificial:
# Pretendo utilizar IA exclusivamente como apoio para a escrita
# e organização deste cabeçalho, descrevendo o domínio, as classes,
# os atributos, as validações e o planejamento de tempo com base
# no código desenvolvido.
#
# Link do chat: https://chatgpt.com/share/6a902960-8da4-83e9-99c2-e0d8464542c8
#
# ============================================================


class Aluno:

    def __init__(self, nome, idade, matricula, nota=0.0):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.nota = nota

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
        if idade and idade > 0:
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


class Escola: 
    def __init__(self, nome, cidade): 
        self._nome = nome 
        self._cidade = cidade 
        self._alunos = [] 

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





#teste = Aluno("Uender", 10, 12345, 5.0);
#teste.nome = "Maria"
#print(teste.nome)
#print(teste)


# DEMONSTRAÇÃO 
# print("=== SISTEMA DE CADASTRO ESCOLAR ===") 

escola = Escola("IFGo", "Iporá") 

# Forma 1: 
# Criando um aluno informando todos os dados. 

aluno1 = Aluno( "Uender", 40, "2026105231940016", 9.1 ) 
escola.adicionar_aluno(aluno1) 

# Forma 2: 
# Criando um aluno sem informar a nota (padrão 0.0).
aluno2 = Aluno( "Jéssica", 34, "2026105231940017" ) 
escola.adicionar_aluno(aluno2) 

# Mostrando os alunos 
escola.listar_alunos() 



# Teste de validação
print("\n=== TESTE DE NOTA INVÁLIDA ===") 
print("Nota atual de Ana:", aluno1.nota) 

try: 
    aluno1.nota = 12 
except ValueError as erro: 
    print("Alteração recusada:", erro) 
    print("Nota após a tentativa:", aluno1.nota)




# Critérios que atingi:
# - Criei as classes Aluno e Escola.
# - Cadastrei nome, idade, matrícula e nota.
# - Coloquei a nota padrão como 0.0.
# - Criei uma lista de alunos na escola.
# - Fiz métodos para adicionar e listar alunos.
# - Fiz validação de idade e nota.
#
# Parte que deu mais trabalho:
# - Entender e usar property e setter e _ nas variáveis.
#
# Como resolvi:
# - Fiz testes dentro do setter.
# - Testei o programa criando alunos e alterando os valores.
#
# Uso de IA:
# - Usei IA para ajudar a organizar e escrever o cabeçalho do código.
