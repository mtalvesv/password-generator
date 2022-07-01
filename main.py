import PySimpleGUI as sg
from interface import Interface
from generator import Generator

janelaInicial = Interface.janelaInicial()
while True:
    window,event,values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cancelar':
        break
    if event == 'Gerar Senha':
        nova_senha = Generator.gerar_senha(values)
        print(nova_senha)
        Generator.salvar_senha(nova_senha, values)'''