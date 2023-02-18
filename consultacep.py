import httpx, datetime

url = 'https://viacep.com.br/ws/{}/json/'
cep = input("Informe seu cep: ")

resposta = httpx.get(url.format(cep))
if resposta.status_code == 200:
    now = datetime.datetime.now()
    hora = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    print("\nHorário da consulta: " + hora + " " + data )
    print("CEP:", resposta.json()['cep'])
    print("Rua:", resposta.json()['logradouro'])
    print("Bairro:", resposta.json()['bairro'])
    print("Cidade:", resposta.json()['localidade'])
    print("Estado:", resposta.json()['uf'])