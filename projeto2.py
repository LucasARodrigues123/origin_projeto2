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

    def apresentar(self):
        print(f'Eu me chamo {self.Nome} e tenho {self.Idade} anos.')

    def comparar_idade(self, outra_pessoa):
        if self.Idade < outra_pessoa.Idade:
            print(f'{self.Nome} é mais novo(a) do que {outra_pessoa.Nome}.')
        elif self.Idade > outra_pessoa.Idade:
            print(f'{self.Nome} é mais velho(a) do que {outra_pessoa.Nome}.')
        else:
            print(f'{self.Nome} tem a mesma idade que {outra_pessoa.Nome}.')

# Exemplo de uso:
pessoa1 = Pessoas("Maria", 1.65, 60, 25, "Branca", "Feminino")
pessoa2 = Pessoas("João", 1.75, 80, 30, "Parda", "Masculino")

print(pessoa1.Imc_Large())
print(pessoa2.Imc_Large())

pessoa1.apresentar()
pessoa2.apresentar()

pessoa1.comparar_idade(pessoa2)
