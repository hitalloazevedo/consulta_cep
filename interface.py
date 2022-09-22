import PySimpleGUI as sg


def root(): 
    sg.theme('Dark2')

    cep = [

        [sg.Text('Informe um CEP:', font='Arial 12', pad=(0,0))],
        [sg.Input(size=(20, 0), font='Arial 12', pad=(0,0), key='cep')]

    ]

    coluna1 = [

        [sg.Text('Logradouro', font='Arial 12')],
        [sg.Text('Bairro', font='Arial 12')],
        [sg.Text('Localidade', font='Arial 12')],
        [sg.Text('UF', font='Arial 12')],
        [sg.Text('IBGE', font='Arial 12')],
        [sg.Text('DDD', font='Arial 12')]

    ]

    coluna2 = [

        [sg.Input(font='Arial 12 bold', key='logradouro', size=(35, 1))],
        [sg.Input(font='Arial 12 bold', key='bairro', size=(30, 1))],
        [sg.Input(font='Arial 12 bold', key='localidade', size=(30, 1))],
        [sg.Input(font='Arial 12 bold', key='uf', size=(4, 1))],
        [sg.Input(font='Arial 12 bold', key='ibge', size=(15, 1))],
        [sg.Input(font='Arial 12 bold', key='ddd', size=(4, 1))]

    ]

    botoes = [

        [sg.Button('Consultar', font='Arial 12', size=(10, 1), pad=((0, 15), 0)),
        sg.Button('Sair', font='Arial 12', size=(8, 1))]

    ]

    layout = [

        [sg.Text('ConsultaCEP', font='Arial 18 bold')],
        [sg.Column(cep, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0)),
        sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]

    ]

    main_root = sg.Window('ConsultaCEP', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True)