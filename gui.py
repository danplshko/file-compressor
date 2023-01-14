import PySimpleGUI as psg
from zip_creator import make_archive

psg.theme('DarkGreen3')

label_to_compress = psg.Text('Select files to compress: ')
input_to_compress = psg.InputText(key="to_compress")
button_to_choose_files = psg.FilesBrowse("Choose", key='button_to_choose_files')

label_select_destination = psg.Text('Select destination folder: ')
input_select_destination = psg.InputText(key="select_destination")
button_to_choose_destination = psg.FolderBrowse('Choose', key='button_to_choose_destination')

output_text = psg.Text(key='output', text_color="green")
compress_button = psg.Button('Compress')


layout = [[label_to_compress, input_to_compress, button_to_choose_files],
          [label_select_destination, input_select_destination, button_to_choose_destination],
          [compress_button, output_text]]

window = psg.Window('File Compressor', layout=layout, font=('Arial', 11))

while True:
    event, values = window.read()
    filepaths = values['to_compress'].split(";")
    folder_path = values['select_destination']
    make_archive(filepaths, folder_path)
    window['to_compress'].update(value="")
    window['select_destination'].update(value="")
    window['output'].update(value="Compression completed!")
    if event == psg.WIN_CLOSED:
        window.close()