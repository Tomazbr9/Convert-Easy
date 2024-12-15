import os
import subprocess
from .useful_functions import json_return, file_info



def convert_docx_to_pdf(request, input_path, extension):
    output_path = file_info(input_path, extension)
    output_dir = os.path.dirname(input_path)
    
    try:
        subprocess.run(
            ['soffice', '--headless', '--convert-to', 'pdf', input_path, '--outdir', output_dir], 
            check=True, capture_output=True, text=True
        )
    except subprocess.CalledProcessError as e:
        print('error: ', e)
        return None

    return json_return(request, output_path)














# # Função que converte docx para pdf
# def convert_docx_to_pdf(request, input_path, extension):
#     output_path = file_info(input_path, extension)
#     # Verifica se a extensão do aquivo é 'txt' e altera para 'plain'
#     if extension == 'txt':
#         extension = 'plain'

#     try:
#         # argumentos extras para o formato PDF
#         extra_args = [
#             '--pdf-engine=xelatex',  # Usar o xelatex como motor de PDF
#             '-V', 'geometry:margin=1in',  # Margens de 1 polegada
#             '-V', 'fontsize=30pt',  # Tamanho da fonte
#             '-V', 'papersize=a4paper', # Tamanho da página A4
#             '-V', 'documentclass=extarticle' # Classe que permite fonte maiores
#         ]
        
#         # aqui é usado a função que converte e salva o arquivo convertido
#         pypandoc.convert_file(
#             input_path, extension, outputfile=output_path, extra_args=extra_args)
        
#         print(f"Arquivo convertido e salvo em: {output_path}")
#     except Exception as e:
#         print('Error:', e)

#     return json_return(request, output_path)
