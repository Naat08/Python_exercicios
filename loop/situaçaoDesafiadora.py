nome=str(input("Digite seu nome: "))
s = 123456
iteracao = 3
while iteracao > 0:
    test=int(input("Digite sua senha: "))
    if test == s:
        print(f"Olá {nome}. Seja bem-vindo ao nosso banco!")
        break
    else:
        iteracao-=1
        if iteracao == 0:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
            break
        print(f"Você agora só tem mais {iteracao} tentativas!")        