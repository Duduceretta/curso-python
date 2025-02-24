#Escreva um programa que leia um valor em metros e o exiba convertido para centimetros e milimetros

valor = float(input('Digite o valor em metros: '))
valorDm = valor * 10
valorCm = valor * 100 
valorMm = valor * 1000
valorDc = valor / 10
valorHm = valor / 100 
valorKm = valor / 1000
print(f'Valor em decimetros = {valorDm} dm')
print(f'Valor em centimetros = {valorCm} cm')
print(F'Valor em milimetros = {valorMm} mm')
print(f'Valor em decametros = {valorDc} dam')
print(f'Valor em hectometros = {valorHm} hm')
print(F'Valor em kilometros = {valorKm} km')
