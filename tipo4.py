# João Gabriel e Luiz Henrique

class IngressoCinema:
    def __init__(self, data, sala, valor):
        self.data = data  
        self.sala = sala 
        self.valor = valor  

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getSala(self):
        return self.sala

    def setSala(self, sala):
        self.sala = sala

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def calcularDesconto(self, idade):
        if 12 <= idade <= 15:
            desconto = 0.40 * self.valor
        elif 16 <= idade <= 20:
            desconto = 0.30 * self.valor
        elif idade > 20:
            desconto = 0.20 * self.valor
        else:
            desconto = 0
        print(f"O valor do seu desconto é de {desconto:.2f} R$.")
class TestarIngresso:
    def main():
        print(ingresso.getData)


valor =float(input("Diga o valor do ingresso. "))
print("O valor do ingresso e de",valor,"R$.""\n" )
data = str(input("Digite a data que você quer agendar: "))
sala = int(input("Qual sala que você vai?: "))
ingresso = IngressoCinema(data, sala, valor)
idade = int(input("Digite sua idade: "))
ingresso.calcularDesconto(idade)
nova_sala = int(input("Nova sala?: "))
ingresso.setSala(nova_sala)
