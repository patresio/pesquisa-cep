import PySimpleGUI as sg
from estados_cidades import *


def tela_inicial():
    sg.theme('Reddit')

    coluna_direita = [
        [sg.Combo(values=siglas(), default_value='Escolha o Estado', size=(
            20, 10), font='Arial 12', key='estadosSiglas', enable_events=True)],
        [sg.Combo(values=[], default_value='Escolha a cidade', size=(
            20, 0), font='Arial 12', key='cidadeSiglas', enable_events=True)],
        [sg.Input(font='Arial 12 bold', size=(40, 1),
                  key='nomerua', enable_events=True)],
    ]

    coluna_esquerda = [
        [sg.Text('UF:', font='Arial 12')],
        [sg.Text('CIDADE:', font='Arial 12')],
        [sg.Text('DIGITE O NOME DA RUA:', font='Arial 12')],
    ]

    botoes = [
        [sg.Checkbox('Rua Completa:', default=True, key="ruacompleta")],
        [sg.Button('Consultar', font='Arial 12',
                   size=(10, 1), pad=((0, 15), 0)),
         sg.CButton('Sair', font='Arial 12', size=(8, 1), pad=((0, 15), 0))]
    ]

    caixa_texto = [
        [sg.Output(size=(200, 480), key='_output_', font='Lucida 8')]
    ]

    layout = [
        [sg.Text('Consulta o CEP', font='Arial 18 bold')],
        [
            sg.Column(coluna_esquerda, pad=((0, 20), 0)),
            sg.Column(coluna_direita)
        ],
        [
            sg.Column(botoes, element_justification='center',
                      justification='center')
        ],
        [
            sg.Column(caixa_texto, element_justification='center',
                      justification='center')
        ]
    ]

    window = sg.Window('Consulta CEP', element_padding=(
        0, 10), layout=layout, size=(800, 500), finalize=True)
