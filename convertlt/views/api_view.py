import os
from django.conf import settings
from django.http import HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from convertlt.serializer import FileUploadSerializer
from utils.pdf_conversions import *
from utils.docx_conversions import *
from utils.img_conversions import *
from utils.audio_conversions import *
from utils.video_conversions import *

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
            
            # Verifica se o arquivo é PDF e o formato desejado é DOCX
            if input_path.endswith('.pdf') and format.lower() == 'docx':
                # Converte o arquivo PDF para DOCX
                return convert_pdf_to_docx(
                    input_path, output_path, original_filename
                )
            
            # Verifica se o arquivo enviado é PDF e o formato desejado é IMG
            if input_path.endswith('.pdf') and format.lower() == 'img':
                # Converte o arquivo PDF para IMG
                return convert_pdf_to_image(
                    input_path, output_path, original_filename
                )
            
            # Verifica se o arquivo é PDF e o formato desejado é IMG
            if input_path.endswith('.pdf') and format.lower() == 'txt':
                # Converte o arquivo PDF para txt
                return convert_pdf_to_text(
                    input_path, output_path, original_filename)

            # Converte formatos 'docx' em pdf ou txt    
            if input_path.endswith('.docx'):
                return convert_docx_to_pdf(
                    input_path, output_path, original_filename, format)
            
            # Verifica se o arquivo é uma imagem para a conversão
            if input_path.endswith('.png') | input_path.endswith('.jpg') | input_path.endswith('.gif'):
                return convert_image(
                    input_path, output_path, original_filename, format)
            
            # Verifica se o arquivo é um audio para a conversão
            if input_path.endswith('.mp3') | input_path.endswith('.wav') | input_path.endswith('.flac'):
                return convert_audio(input_path, output_path, original_filename, format)
            
            # Verifica se o arquivo é um video para a conversão
            if input_path.endswith('.mp4') | input_path.endswith('.avi') | input_path.endswith('.mov'):
                return convert_video(input_path, output_path, original_filename, format)
                
            # Retorna erro se o formato não for suportado
            return HttpResponseBadRequest("Invalid file type or unsupported format.")
        
        # Retorna erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)