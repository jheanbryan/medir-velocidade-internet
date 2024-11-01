import PySimpleGUI as sg
import speedtest as sp
import datetime

def medir_velocidade():
    test = sp.Speedtest()
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M")

    try:
        sg.popup('Medindo (Isto pode levar alguns instantes)...')
        download = test.download() / 1e+6  # Conversão para Mbps
        upload = test.upload() / 1e+6

        velocidade_download = f'DOWNLOAD: {download:.2f} Mbps'
        velocidade_upload = f'UPLOAD: {upload:.2f} Mbps'

        with open('relatorio.txt', 'a') as arquivo:
            arquivo.write(f'\n{date} - {hour}    Download: {download:.2f} Mbps    Upload: {upload:.2f} Mbps')

        return velocidade_download, velocidade_upload

    except Exception as e:
        return '[ERRO]: ao conectar ao servidor', str(e)

def first_window():
    sg.theme('Dark Grey 13') 

    layout = [ 
                [sg.Text('Clique em Iniciar para começar o teste', justification='center')],
                [sg.Button('Iniciar'), sg.Button('Cancelar')] 
            ]

    window = sg.Window('Medidor de Velocidade', layout, size=(300, 70))
    event, values = window.read()
    window.close()

    return event == 'Iniciar'

def last_window(download, upload):
    layout = [ 
        [sg.Text(download)],
        [sg.Text(upload)],
        [sg.Text('Foi salvo um relatório com o nome relatorio.txt')],
        [sg.Button('OK')]
    ]

    window_res = sg.Window('Resultado do Teste', layout)

    event, values = window_res.read()
    window_res.close()

def main():
    if first_window():
        velocidade_download, velocidade_upload = medir_velocidade()
        last_window(velocidade_download, velocidade_upload)
    else:
        sg.popup('Teste cancelado.')

if __name__ == "__main__":
    main()
