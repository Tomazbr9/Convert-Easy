import os
from django.conf import settings
from django.http import HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from convertlt.models import FileUpload
from convertlt.serializer import FileUploadSerializer
from utils.conversions import convert_pdf_to_docx, convert_pdf_to_image

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        # Serializa e valida os dados enviados pelo formulário
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # Salva o arquivo enviado
            instance = serializer.save()
            # Caminho do arquivo enviado
            input_path = instance.file.path # type: ignore
            
            # Obtém o formato desejado do input
            format = request.data.get('format')
            
            # Nome do arquivo original sem extensão
            original_filename = os.path.splitext(os.path.basename(input_path))[0]
            # Define o caminho do arquivo de saída com o mesmo nome do original
            output_path = os.path.join(settings.MEDIA_ROOT, 'conversions')
            
            # Verifica se o arquivo é PDF e o formato é DOCX
            if input_path.endswith('.pdf') and format.lower() == 'docx':
                # Converte o arquivo PDF para DOCX
                return convert_pdf_to_docx(
                    input_path, output_path, original_filename
                )
            
            print(f'+++++++++++++++++{format.lower()}++++++++++++++++++++')
            
            # Verifica se o arquivo é PDF e o formato é IMG
            if input_path.endswith('.pdf') and format.lower() == 'img':
                # Converte o arquivo PDF para IMG
                return convert_pdf_to_image(
                    input_path, output_path, original_filename
                )
                
            # Retorna erro se o formato não for suportado ou se o arquivo não for PDF
            return HttpResponseBadRequest("Invalid file type or unsupported format.")
        
        # Retorna erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)