import os

path = '/home/ph'
fileExtension = '.mp4'

def lista(path, fileExtesion):
    for pathFind, dir, archiveFind in os.walk(path):
        for archive in archiveFind:
            if archive.endswith(fileExtension):
                print(f'{archive} ---- {pathFind}/{archive}')
                

lista(path, fileExtension)