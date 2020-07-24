import PySimpleGUI as sg 
import sys
import os

sg.theme('DarkAmber')

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class Tela:
    def __init__(self):
        layout = [
            [sg.Text('Caminho', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text('Extensão', size=(15, 1)), sg.Combo(['.mph', '.avi'], size=(15, 1))],
            [sg.Button('Buscar')]
        ]

        janela = sg.Window("Lista Arquivos").Layout(layout)

        self.button, self.values  = janela.Read()


    def Iniciar(self):
        print(self.values)
    

tela = Tela()
tela.Iniciar()