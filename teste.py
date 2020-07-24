import os
import time
from tqdm import tqdm
from os.path import getsize

class Listar:
    def __init__(self, path, fileExtension):
        self.path = path
        self.fileExtension = fileExtension


    def files(self):
        for dirpath, dirnames, filenames in os.walk(self.path, topdown=True):
            for namefile in filenames:
                if namefile.endswith(self.fileExtension):
                    print(namefile)


    def root(self):
        for dirpath, dirnames, filenames in os.walk(self.path, topdown=True):
            for namefile in filenames:
                if namefile.endswith(self.fileExtension):
                    caminho = dirpath+'/'+namefile
                    print(caminho)
    

    def info(self):
        for dirpath, dirnames, filenames in os.walk(self.path, topdown=True):
            for namefile in filenames:
                if namefile.endswith(self.fileExtension):
                    caminho = dirpath+'/'+namefile
                    size = getsize(caminho)/1000000
                    info = os.stat(caminho)
                    print(f'{size:.1f} MB {time.ctime(info.st_mtime)}')

mostra = Listar('/home/','.mp4')
mostra.files()
mostra.root()
mostra.info()
