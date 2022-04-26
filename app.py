from interface_grafica import *
from estados_cidades import *
from pesquisa_cep import *

tela_inicial()


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'estadosSiglas':
        selectSigla = values[event]
        cidades_lista = cidades(selectSigla)
        cidade = cidades_lista[0]
        window['cidadeSiglas'].update(values=cidade, value='', size=(
            20, 10))

    if event == 'Consultar':
        window.FindElement('_output_').Update('')
        estado = values['estadosSiglas']
        cidade = values['cidadeSiglas']
        rua = values['nomerua']
        if values['ruacompleta'] == True:
            rua = rua.replace(' ', '%20')
        else:
            rua = rua.replace(' ', '+')
        pesquisar_cep(estado, cidade, rua)
