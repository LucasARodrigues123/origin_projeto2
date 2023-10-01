import re

class Pessoas:
    def __init__(self, nome, altura, peso, idade, cor, genero, data):
        self.genero = genero
        self.cor = cor
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso
        self.data = data

    def verificar_idade(self):
        return self.idade >= 18

    def imc(self):
        return self.peso / (self.altura ** 2)

    def imc_longo(self):
        imc = self.imc()
        if imc < 17.0:
            return 'Você está abaixo do peso!!'
        elif 17.0 <= imc < 24.0:
            return 'Você está com peso normal'
        elif 24.0 <= imc < 29.0:
            return 'Você está acima do peso'
        elif 29.0 <= imc < 34.0:
            return 'Você está com sobrepeso classe I'
        elif 34.0 <= imc < 40.0:
            return 'Você está com Obesidade classe II'
        else:
            return 'Você está com Obesidade classe III'

    def comparar_idade(self, outra_pessoa):
        if self.idade < outra_pessoa.idade:
            print(f'{self.nome} é mais novo(a) do que {outra_pessoa.nome}.')
        elif self.idade > outra_pessoa.idade:
            print(f'{self.nome} é mais velho(a) do que {outra_pessoa.nome}.')
        else:
            print(f'{self.nome} tem a mesma idade que {outra_pessoa.nome}.')

    def apresentar(self):
        print(f'Eu me chamo: {self.nome} e tenho {self.idade} anos, nasci em {self.data}.')

class Estudo(Pessoas):
    def __init__(self, nome, altura, peso, idade, cor, genero, ensino, etnia, data): 
        super().__init__(nome, altura, peso, idade, cor, genero, data)
        self.ensino = ensino 
        self.etnia = etnia

    def curso_ensino(self):
        print(f'{self.nome} já cursou {self.ensino} no continente Ásia, vindo de um país da {self.etnia}')

    def apresentar(self):
        print(f'Olá, me chamo: {self.nome}, tenho {self.idade} anos e nasci em {self.data}. Pretendo cursar Academia {self.ensino} e pretendo viajar para {self.etnia} para continuar meus estudos.') 

# Objetos pessoa:
pessoa1 = Pessoas("Maria", 1.80, 60, 25, "Branca", "Feminino", "10/08/1998")
pessoa1.apresentar()
if pessoa1.verificar_idade():
    print('É maior de idade')
else:
    print('É menor de idade')
print(f"IMC: {pessoa1.imc():.1f}")
print(f'Categoria de Risco: {pessoa1.imc_longo()}')

print("----")

pessoa2 = Pessoas("Marcos", 1.90, 80, 35, "Pardo", "Masculino", "12/05/1988")
pessoa2.apresentar()
if pessoa2.verificar_idade():
    print('É maior de idade')
else:
    print('É menor de idade')
print(f"IMC: {pessoa2.imc():.1f}")
print(f'Categoria de Risco: {pessoa2.imc_longo()}')

print("---")
pessoa3 = Estudo('Gerson', 2.30, 100, 40, 'Negro', 'Masculino', 'Engenharia', 'Ásia', '20/03/1983')
pessoa3.comparar_idade(pessoa1)
pessoa3.curso_ensino()
pessoa3.apresentar()
print('===')
pessoa4 = Estudo('Marta', 2.30, 100, 47, 'Negro', 'Feminino', 'Música', 'Europa', '05/06/1976')
pessoa4.comparar_idade(pessoa2)
pessoa4.curso_ensino()
pessoa4.apresentar()
