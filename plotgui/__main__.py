import PySimpleGUI as sg
from source import make_plots

layout = [
    [sg.Text("Статус операции:")],
    [sg.Output(size=(50,4))],
    [sg.Text("Выберите файл: "), sg.InputText(), sg.FileBrowse()],
    [sg.Text("Целевая папка: "), sg.InputText(default_text="~/Desktop"), sg.FolderBrowse()],
    [sg.Submit()]
]

def main():
    window = sg.Window('Simple window').Layout(layout)
    while True:
        event, values = window.Read()

        print(event, values)
        if event is None or event == 'Exit':
            break
        if event == 'Submit':
            (filename, ofolder) = values
            
            make_plots(filename, ofolder=ofolder)
    
    window.Close()


if __name__ == "__main__":
    main()