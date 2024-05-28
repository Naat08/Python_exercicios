produtos = {}
quant = int(input("Digite a quantos produtos você deseja adicionar: "))

for i in range(quant):
    prod = input("Nome do produto: ")
    valor = float(input("Valor unitário: "))
    qtd = int(input("Quantidade de cada produto: "))
    produtos.update({i:[prod, valor, qtd]})

total = 0

print(50 * '-')
print('Carrinho de Compras')
print(50 * '-')

for cod, prod in produtos.items():
    subtotal = prod[1] * prod[2]
    print(f"{cod} - {prod[0]} - R$ {prod[1]:.2f} - {prod[2]} un - R$ {subtotal:.2f}")
    total += subtotal

print(50 * '-')
print(f"Total da compra R$ {total:.2f}")
print(50 * '-')
