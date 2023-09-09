class Pessoas:
    def __init__(self, Nome, Altura, Peso, Idade, Cor, Genero):
        self.Genero = Genero
        self.Cor = Cor
        self.Nome = Nome
        self.Altura = Altura
        self.Idade = Idade
        self.Peso = Peso

    def VerificarIdade(self):
        return self.Idade >= 18

    def Imc(self):
        return self.Peso / (self.Altura ** 2)

    def Imc_Large(self):
        Imc = self.Imc()
        if Imc < 17.0:
            return 'Você está abaixo do peso!!'
        elif 17.0 <= Imc < 24.0:
            return 'Você está com peso normal'
        elif 24.0 <= Imc < 29.0:
            return 'Você está acima do peso'
        elif 29.0 <= Imc < 34.0:
            return 'Você está com sobrepeso classe I'
        elif 34.0 <= Imc < 40.0:
            return 'Você está com Obesidade classe II'
        else:
            return 'Você está com Obesidade classe III'

    def comparar_idade(self, outra_pessoa):
        if self.Idade < outra_pessoa.Idade:
            print(f'{self.Nome} é mais novo(a) do que {outra_pessoa.Nome}.')
        elif self.Idade > outra_pessoa.Idade:
            print(f'{self.Nome} é mais velho(a) do que {outra_pessoa.Nome}.')
        else:
            print(f'{self.Nome} tem a mesma idade que {outra_pessoa.Nome}.')

    def apresentar(self):
        print(f' Eu me chamo: {self.Nome} e tenho {self.Idade} de idade.')

class Estudo(Pessoas):
    def __init__(self, Nome, Altura, Peso, Idade, Cor, Genero, Emsino, Etinia): 
        super().__init__(Nome, Altura, Peso, Idade, Cor, Genero)
        self.Emsino = Emsino 
        self.Etinia = Etinia

    def curso_Emsino(self):
        print(f'{self.Nome} Já cursou {self.Emsino} superior no continente Asia vindo de um país da {self.Etinia}')


    def apresentar(self):
        print(f'Olá me chamo: {self.Nome}, tenho {self.Idade} de idade e cursei Academia {self.Emsino}, e pretendo Viajar para {self.Etinia}, Para continuar meus Estudos ') 
           
# Objetos pessoa:
pessoa1 = Pessoas("maria", 1.80, 60, 25, "Branca", "Feminino")
pessoa1.apresentar()
if pessoa1.VerificarIdade():
    print('é maior de Idade')
else:
    print('é menor de Idade')
print(f"IMC: {pessoa1.Imc():.1f}")
print(f'Categoria de Risco: {pessoa1.Imc_Large()}')

print("----")

pessoa2 = Pessoas("Marcos", 1.90, 80, 35, "Pardo", "Masculino")
pessoa2.apresentar()
if pessoa2.VerificarIdade():
    print('é maior de Idade')
else:
    print('é menor de Idade')
print(f"IMC: {pessoa2.Imc():.1f}")
print(f'Categoria de Risco: {pessoa2.Imc_Large()}')

print("---")

pessoa3 = Estudo ('Gerson', 2.30, 100, 40, 'Negro','Masculino','egenharia','Asia')
pessoa3.VerificarIdade()
pessoa3.Imc_Large()
pessoa3.curso_Emsino()
pessoa3.apresentar()
print('===')
pessoa4 = Estudo  ('Marta', 2.30, 100, 40, 'Negro','Feminino','Musica','Europa')
pessoa4.VerificarIdade()
pessoa4.Imc_Large()
pessoa4.curso_Emsino()
pessoa4.apresentar()


