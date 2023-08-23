import PySimpleGUI as sg

def second_window():
    layout = [ 
        [sg.Text('A velocidade da sua internet é tal')] 
    ]

    window_res = sg.Window('Medidor de Velocidade', layout)

    event, values = window_res.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        window_res.close()


def initial_window():
    sg.theme('Dark Grey 13') 

    layout = [ 
                [sg.Text('Clique em Iniciar o teste')],
                [sg.Button('Iniciar'), sg.Button('Cancelar')] 
            ]

    window = sg.Window('Medidor de Velocidade', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            break
        else:
            #calcular a velocidade da internte
            print('vou calcular')
            second_window()
            window.close()

initial_window()