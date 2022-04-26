import json


def estados_json():
    estados_cidades = r'H:\Meu Drive\repos\pesquisa-cep\estados_cidades.json'
    with open(estados_cidades, encoding='UTF-8') as estados_cidades_json:
        estados_cidades_dic = json.load(estados_cidades_json)
    return estados_cidades_dic


def siglas():
    estados = estados_json()
    siglas_list = []
    for estado in estados['estados']:
        siglas_list.append(estado['sigla'])
    return siglas_list


def cidades(sigla):
    estados = estados_json()
    cidade_list = []
    for estado in estados['estados']:
        if estado['sigla'] == sigla:
            cidade_list.append(estado['cidades'])
    return cidade_list
