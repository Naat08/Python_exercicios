numeros = []
quant = 1

while quant <= 5:
    digit=int(input(f"Digite {quant}º números inteiros: "))
    numeros.append(digit)
    quant+=1
print(f"Sua lista: {numeros}")
print(f"A soma da sua lista: {sum(numeros)}")
print(f"O maior número da sua lista: {max(numeros)}")
print(f"O menor número da sua lista: {min(numeros)}")
print(f"A média dos números é: {sum(numeros)/len(numeros)}")