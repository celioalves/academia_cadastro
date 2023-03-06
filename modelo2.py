# def cadastro(nome, idade, altura, peso, sexo, objetivo):
#     aluno = {'nome': nome, 'idade': idade, 'altura': altura, 'peso': peso, 'sexo': sexo, 'objetivo': objetivo}
#     return aluno
# para criar esse objeto aluno no console, é necessário chamar a referência (aluno) = função (cadastro) e os parâmetros
                                                        #                   aluno = cadastro(nome, idade.....)

# MÉTODO - É O QUE UM OBJETO SABE FAZER
# ATRIBUTO - É O QUE UM OBJETO TEM

class Cadastro:
    def __init__(self, nome, idade, genero, tipo):  # função construtora
        self._nome = nome.title()   # nome.title() #todos os atributos que o cadastro deve ter, não será aceito se faltar algum deles#
        self.idade = idade   # int(idade)
        self._genero = genero
        self._tipo = tipo

    # GET - RETORNAM ALGO ### @property
    # SET - MODIFICAM ALGO ### @.setter
    # o python entende que é uma propriedade e não precisa do () na hora de chamar no console

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, novo_genero):
        self._genero = novo_genero.title()

    @property
    def tipo(self):
        return self._tipo

    def __str__(self):
        return f'{self._nome} - {self._genero} - {self._tipo}'


class Aluno(Cadastro):
    def __init__(self, nome, idade, altura, peso, genero, objetivo, tipo):
        super().__init__(nome, idade, genero, tipo)
        self.altura = altura  # int(altura)
        self._peso = peso    # int(peso)
        self.objetivo = objetivo

    def atualizacao_peso(self, novo_peso): # esse código não deveria estar aqui, e sim dentro de uma classe Aluno, tendo em vistaa que esse cadastro é para funcionários e alunos
        self._peso2 = float(novo_peso)
        print(f'o seu peso era de {self._peso} kg, e agora você está com {self._peso2} kg')
        print(f'Você deve uma diferença de peso de {(self._peso2 - self._peso)} kg')
        self._peso = self._peso2

    @property
    def objetivo(self):
        return self._objetivo.title()

    @objetivo.setter
    def objetivo(self, outro_objetivo):
        self._objetivo = outro_objetivo

    def __str__(self):
        return f'{self._nome},' \
               f'tem {self.idade} anos, {self.altura / 100} de altura, {self._peso} kgs, {self._genero.title()},' \
               f' o seu objetivo é {self.objetivo}, está cadastrado como {self.tipo}.'


class Funcionario(Cadastro):
    def __init__(self, nome, idade, genero, tipo, cargo):
        super().__init__(nome, idade, genero, tipo)
        self._cargo = cargo

    def __str__(self):
        return f'{self._nome}, tem {self.idade} anos, é do sexo {self.genero.title()}, é do quadro de {self.tipo}' \
               f' e é {self._cargo.title()} na academia.'


joao = Aluno('João', 25, 190, 90, 'masculino', 'emagrecimento', 'aluno')
henrique = Funcionario('henrique', 40, 'masculino', 'Funcionário', 'recepcionista')
roberta = Funcionario('roberta', 20, 'feminino', 'Funcionário', 'Instrutor')
henrique2 = Funcionario('henrique', 40, 'masculino', 'Funcionário', 'Instrutor')
marcos = Funcionario('marcos', 29, 'masculino', 'Funcionário', 'Instrutor')
paulo = Funcionario('paulo', 39, 'masculino', 'Funcionário', 'Gerente')
marcia = Aluno('Márcia', 21, 158, 57, 'feminino', 'ganho de massa', 'aluno')
celio = Aluno('célio', 30, 172, 89, 'masculino', 'emagrecimento', 'aluno')
yuri = Aluno('yuri', 33, 188, 127, 'masculino', 'emagrecimento', 'aluno')
gabriel = Aluno('gabriel', 25, 190, 90, 'masculino', 'emagrecimento', 'aluno')
gustavo = Aluno('gustavo', 23, 190, 90, 'masculino', 'ganho de massa', 'aluno')
tiago = Aluno('tiago', 22, 193, 80, 'masculino', 'manutenção', 'aluno')
pedro = Aluno('pedro', 31, 184, 73.4, 'masculino', 'ganho de massa', 'aluno')

alunos_e_funcionarios = [joao, henrique, roberta, henrique2, marcos, paulo, marcia, celio, yuri, gabriel, gustavo,
                         tiago, pedro]

for membros in alunos_e_funcionarios:
    print(membros, end= "\n""\n")

#aluno = Cadastro('pedro', 32, 190, 90.5, 'masculino', 'ganho de massa')  # só vai ser chamado no console se eu importar diretamente
