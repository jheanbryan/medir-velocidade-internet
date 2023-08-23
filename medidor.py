#speedtest -> pip install speedtest-cli
#pip install pandas
#https://pypi.org/project/speedtest-cli/
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
        try:
            velocidadeDownload = 'DOWNLOAD: {:.2f} Mbps'.format(download)
            velocidadeUpload = 'UPLOAD: {:.2f} Mbps'.format(upload)

            with open('relatorio.txt', 'a') as arquivo:
                arquivo.write('\n{} - {}    Download:{:.2f} Mbps    Upload:{:.2f} Mbps'.format(date, hour, download, upload))
        except:
            print('[ERRO]: Desconhecido')
    except:
        print('[ERRO]: ao conectar ao servidor')
