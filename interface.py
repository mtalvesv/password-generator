import PySimpleGUI as sg

class Interface():
    def janelaInicial():
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha'),sg.Button('Cancelar')]
        ]
        return sg.Window('Password Generator',layout=layout, finalize=True)    