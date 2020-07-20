import os
from os.path import join, getsize

path = '/home/ph'
fileExtension = '.mp4'

def lista(path, fileExtesion):
    for pathFind, dir, archiveFind in os.walk(path):
        for archive in archiveFind:
            if archive.endswith(fileExtension):
                p = pathFind+'/'+archive
                size = getsize(p)
                print(f'{archive} ---- {pathFind}/{archive} - {size}')
                

lista(path, fileExtension)