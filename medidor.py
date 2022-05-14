#speedtest -> pip install speedtest-cli
#pip install pandas
# https://pypi.org/project/speedtest-cli/
import speedtest as sp
test = sp.Speedtest()

try:
    download = (test.download()) / 1e+6
    upload = (test.upload()) / 1e+6
    try:
        print('\nDOWNLOAD: {:.2f} Mbps'.format(download))
        print('UPLOAD: {:.2f} Mbps\n'.format(upload))
    except:
        print('Error')
except:
    print('Erro ao conectar ao servidor')

#adicionar função para salvar os dados e o horário em arquivo??