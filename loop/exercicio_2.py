print("Digite 5 números (inteiros e positivos), e o programa dirá quantos números são pares")
par = 0
impar = 0
iteracao = 1
while iteracao <= 5:
    n=int(input(f"Digite o {iteracao}º número: "))
    if n%2 == 0:
        print("Seu número é par")
        par+=1 
    else:
        print("Seu número e ímpar")
        impar+=1
    iteracao+=1
print(f"{par} são pares")
print(f"{impar} são ímpares")