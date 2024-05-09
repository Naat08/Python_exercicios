import json
import urllib.request

# Solicitar ao usuário o CEP
cep = input("Digite o CEP: ")

# Construir na URL de consulta
url = f"https://viacep.com.br/ws/{cep}/json/"
