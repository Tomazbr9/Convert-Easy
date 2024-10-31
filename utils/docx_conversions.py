import os 
import pypandoc
from .useful_functions import download_return

# Função que converte docx para pdf
def convert_docx_to_pdf(input_path, output_path, original_filename, extension):
    output_path = os.path.join(output_path, f'{original_filename}.{extension}')
    
    # Verifica se a extensão do aquivo é 'txt' e altera para 'plain'
    if extension == 'txt':
        extension = 'plain'
    
    try:
        # aqui é usado a função que converte e salva o arquivo convertido
        pypandoc.convert_file(
            input_path, extension, outputfile=output_path)
    except Exception as e:
        print('Error:', e)

    return download_return(output_path, original_filename, extension)
