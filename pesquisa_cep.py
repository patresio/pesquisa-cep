import requests
import json


def pesquisar_cep(estado, cidade, rua):
    cidadeFormatada = formata_cidade(cidade)
    link = f'https://viacep.com.br/ws/{estado}/{cidadeFormatada}/{rua}/json/'
    pesquisa_cep = requests.get(link)
    pesquisa_cep_dic = pesquisa_cep.json()
    for ruacep in pesquisa_cep_dic:
        print(f"A {ruacep['logradouro']} está com o seguinte CEP {ruacep['cep']}, e Bairro {ruacep['bairro']}, começando em {ruacep['complemento']}")


def formata_cidade(cidade):
    cidade = cidade.replace(' ', '%20')
    return cidade
