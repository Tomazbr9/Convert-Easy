import os
import zipfile
from django.http import FileResponse

# Funcão que Força o Download do arquivo convertido no navegador
def download_return(input_path, output_path, original_filename, extension):
    response = FileResponse(
    open(
        output_path, 'rb'), as_attachment=True, filename=f'{original_filename}.{extension.lower()}'
    )
    response =  delete_files_temporarily(
                    response, original_filename, input_path, output_path
                )
    return response
    

# função que apaga arquivos de entrada e saida
def delete_files_temporarily(response, file_name, input_path, output_path):
    response['Content-Disposition'] += f';filename={file_name}.docx'
    response['File-Cleanup'] = True

    def cleanup():
        if os.path.exists(input_path):
            os.remove(input_path)
        
    response.close = cleanup

    return response

# Compacta arquivos convertidos em uma pasta
def compress_file(files, output_path):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))

