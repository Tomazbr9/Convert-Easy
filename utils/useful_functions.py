import os
import zipfile
from django.http import FileResponse, HttpResponse
from rest_framework.response import Response
from django.conf import settings

# Funcão que Força o Download do arquivo convertido no navegador
def download_return(output_path, original_filename, extension):
    if os.path.exists(output_path):
        response = FileResponse(
        open(
            output_path, 'rb'), as_attachment=True, filename=f'{original_filename}.{extension.lower()}'
        )

        response['Content-Disposition'] += f';filename={original_filename}.{extension}'
        response['File-Cleanup'] = True

        return response
    else:
        return HttpResponse("Erro ao Gerar Arquivo", status=500)

# Compacta arquivos convertidos em uma pasta
def compress_file(files, output_path):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))


def json_return(request, fileUrl):
    file_name = os.path.basename(fileUrl)
    path_base = os.path.join(settings.MEDIA_URL, 'conversions/')
    file_path = os.path.join(path_base, file_name)
    full_url = request.build_absolute_uri(file_path)

    return Response({
        'fileName': file_name,
        'fileUrl': fileUrl,
        'fullUrl': full_url
    })


def file_info(input_path, format):
    output_path = os.path.splitext(input_path)[0] + f'.{format}'
    return output_path
   