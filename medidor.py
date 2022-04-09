import speedtest
import datetime
import time

# Função para testar velocidade de conexão
def teste_internet():
    s = speedtest.Speedtest()
    s.get_closest_servers()
    s.get_best_server()

    velocidade_download = s.download(threads = None)
    velocidade_upload = s.upload(threads = None) 
    print(velocidade_download)
    print(velocidade_upload)
    