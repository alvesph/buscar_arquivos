import os

path = '/home/ph'
archive = '.mp4'

def lista(caminho, archive):
    for caminho, diretorios, arquivos in os.walk(caminho):
        for l in arquivos:
            if l.endswith(archive):
                print(f'{l} ---- {caminho}/{l}')
                

lista(path, archive)