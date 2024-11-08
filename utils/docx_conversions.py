import os 
import pypandoc
from .useful_functions import download_return, json_return, file_info

# Função que converte docx para pdf
def convert_docx_to_pdf(request, input_path, extension):
    output_path = file_info(input_path, extension)
    # Verifica se a extensão do aquivo é 'txt' e altera para 'plain'
    if extension == 'txt':
        extension = 'plain'
    try:
        # aqui é usado a função que converte e salva o arquivo convertido
        pypandoc.convert_file(
            input_path, extension, outputfile=output_path)
    except Exception as e:
        print('Error:', e)

    return json_return(request, output_path)
