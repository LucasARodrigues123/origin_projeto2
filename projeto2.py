
class Pessoas:
    
    def __init__(self, Nome, Altura, Peso, Idade, Cor, Genero, Data):
        self.Genero = Genero
        self.Cor = Cor
        self.Nome = Nome
        self.Altura = Altura
        self.Idade = Idade
        self.Peso = Peso
        self.Data = Data
 
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
        print(f' Eu me chamo: {self.Nome} e tenho {self.Idade} de idade naci no {self.Data}.')

class Estudo(Pessoas):
    def __init__(self, Nome, Altura, Peso, Idade, Cor, Genero, Emsino, Etinia, Data): 
        super().__init__(Nome, Altura, Peso, Idade, Cor, Genero, Data)
        self.Emsino = Emsino 
        self.Etinia = Etinia
        self.Data = Data

    def curso_Emsino(self):
        print(f'{self.Nome} Já cursou {self.Emsino} no continente Asia vindo de um país da {self.Etinia}')


    def apresentar(self):
        print(f'Olá me chamo: {self.Nome}, tenho {self.Idade} de idade  e  naceus {self.Data} epretende cursar Academia {self.Emsino}, e pretendo Viajar para {self.Etinia}, Para continuar meus Estudos ') 
           
# Objetos pessoa:
pessoa1 = Pessoas("maria", 1.80, 60, 25, "Branca", "Feminino","10/08/1998")
pessoa1.apresentar()
if pessoa1.VerificarIdade():
    print('é maior de Idade')
else:
    print('é menor de Idade')
print(f"IMC: {pessoa1.Imc():.1f}")
print(f'Categoria de Risco: {pessoa1.Imc_Large()}')

print("----")

pessoa2 = Pessoas("Marcos", 1.90, 80, 35, "Pardo", "Masculino","12/05/1988")
pessoa2.apresentar()
if pessoa2.VerificarIdade():
    print('é maior de Idade')
else:
    print('é menor de Idade')
print(f"IMC: {pessoa2.Imc():.1f}")
print(f'Categoria de Risco: {pessoa2.Imc_Large()}')


print("---")
pessoa3 = Estudo ('Gerson', 2.30, 100, 40, 'Negro','Masculino','egenharia','Asia', '20/03/1983')
pessoa3.VerificarIdade()
pessoa3.Imc_Large()
pessoa3.curso_Emsino()
pessoa3.apresentar()
print('===')
pessoa4 = Estudo  ('Marta', 2.30, 100, 47, 'Negro','Feminino' ,'Musica','Europa', '05/06/1976')
pessoa4.VerificarIdade()
pessoa4.Imc_Large()
pessoa4.curso_Emsino()
pessoa4.apresentar()
import re    
while True:
    userNome = (input (f'Digite seu nome ?:'))
    if re.match(r'^[aA-zZ_áÁ-úÚ\s\.]+$' , userNome):
        break
    else:
        print('Nome invalido digite novamente')

while True:
    userAltura = (input(f'Digite  sua altura ?:'))
    if re.match(r'^[1-9]|[.]|[0-1-9]+$', userAltura):
        break    
    else:
        print('digite uma  altura valida em MM ou CM exemplo:1.50')

while True:
    userIdade = input(f'Digite  sua idade apenas numeros:')
    if re.match(r'^\d{2}$', userIdade):
        break    
    else:
        print('digite uma  idade Valido')
    
while True:
    userPeso = (input(f'Digite  seu peso:'))
    if re.match(r'^\d{2}$', userPeso):
        break    
    else:
        print('digite uma  Peso Valido')
    
while True:
    userData = input(f'Digite sua Data de nacimento desta formar Dd/Mm/Ano:')
    if re.match(r'^(0[1-9]|1[0-9]2[0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$',userData):
        break
    else:
        print('digite uma data valida dd/mm/ano')

while True:
    cpf = input('Digite seu cpf apenas Numeros  sem espasos ?')
    if re.match(r'^\d{11}$',cpf):
        break
    else:
        print('cpf invalido digite nova mente')

pessoa5 = Pessoas(userNome, userAltura, userPeso, 26,"Branca", "Masculino" ,userData)
pessoa5.apresentar()


