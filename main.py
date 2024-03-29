import PySimpleGUI as sg
import speedtest as sp
import datetime

def medir_velocidade():
    test = sp.Speedtest()
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M")

    try:
        print('Medindo...')
        download = (test.download()) / 1e+6
        upload = (test.upload()) / 1e+6

        velocidade_download = 'DOWNLOAD: {:.2f} Mbps'.format(download)
        velocidade_upload = 'UPLOAD: {:.2f} Mbps'.format(upload)

        with open('relatorio.txt', 'a') as arquivo:
            arquivo.write('\n{} - {}    Download:{:.2f} Mbps    Upload:{:.2f} Mbps'.format(date, hour, download, upload))

        return velocidade_download, velocidade_upload

    except:
        print('[ERRO]: ao conectar ao servidor')

def first_window():
    sg.theme('Dark Grey 13') 

    layout = [ 
                [sg.Text('Clique em Iniciar para começar o teste', justification='center')],
                [sg.Button('Iniciar'), sg.Button('Cancelar')] 
            ]

    window = sg.Window('Medidor de Velocidade', layout, size=(300, 70))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            cancel = True
            window.close()
            return cancel
            break
        else:
            cancel = False
            window.close()
            return cancel
def last_window(download, upload):
    layout = [ 
        [sg.Text(download)],
        [sg.Text(upload)],
        [sg.Text('Foi salvo um relatório com o nome relatorio.txt')],
        [sg.Button('OK')]
    ]

    window_res = sg.Window('Medidor de Velocidade', layout)

    event, values = window_res.read()
    if event == sg.WIN_CLOSED or event == 'Ok':
        window_res.close()


cancel = first_window()
if cancel == True:
    print('Cancelou')
else:
    print('Não cancelou')
    velocidade_download, velocidade_upload = medir_velocidade()
    last_window(velocidade_download, velocidade_upload)

