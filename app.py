from interface import *
from cep import *
import PySimpleGUI as sg


root()
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Sair':
        break

    if event == 'Consultar':
        try:
            logradouro = consultar(values['cep'])['logradouro']
            bairro = consultar(values['cep'])['bairro']
            localidade = consultar(values['cep'])['localidade']
            uf = consultar(values['cep'])['uf']
            ibge = consultar(values['cep'])['ibge']
            ddd = consultar(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['ibge'].update(ibge)
            window['ddd'].update(ddd)

        except:
            sg.popup('Verifique se o campo "CEP" está correto.\n'
            'ou se está conectado a internet.', title='Error')