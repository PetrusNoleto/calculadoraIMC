'''
Abaixo de 17	Muito abaixo do peso
Entre 17 e 18,49	Abaixo do peso
Entre 18,5 e 24,99	Peso normal
Entre 25 e 29,99	Acima do peso
Entre 30 e 34,99	Obesidade I
Entre 35 e 39,99	Obesidade II (severa)
Acima de 40	Obesidade III (mórbida)
'''
nome = str(input("qual é seu nome! "))
peso = float(input('qual é seu peso! '))
altura = float(input('qual é sua altura! '))

def calcImc(peso, altura):
     imc = (peso / (altura**2))
     
     if imc <= 17:
          print("Muito abaixo do peso")
     if imc > 17 and imc <= 18.49:
          print("Abaixo do peso")
     if imc > 18.5 and imc <= 24.99:
          print("Peso normal")
     if imc > 25 and imc <= 29.99:
          print("Acima do peso")
     if imc > 30 and imc <= 34.99:
          print("Obesidade I")
     if imc > 35 and imc <= 39.99:
          print("Obesidade II (severa)")
     if imc >= 40:
          print("Obesidade III (mórbida)")
     return(imc)


if peso  == 0 and peso == 0.0:
     print("insira um valor no peso")
if altura   == 0 and altura == 0.0:
     print("insira um valor na altura")
else:
     calcImc(peso, altura)   






