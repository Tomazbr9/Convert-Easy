import os
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
            input_path = instance.file.path  # type: ignore
            # Obtém o formato desejado do input
            format = request.data.get('format')

            # Lista de formatos válidos
            valid_formats = [
                'pdf', 'docx', 'png', 'jpeg', 'jpg', 'gif', 'img',
                'txt', 'mp3', 'wav', 'flac', 'avi', 'mp4', 'mov'
            ]

            if format.lower() not in valid_formats:
                return Response({'error': 'Formato não é suportado.'})
            
            # Verifica se o arquivo é PDF e o formato desejado é DOCX
            if input_path.endswith('.pdf') and format.lower() == 'docx':
                try:
                    return convert_pdf_to_docx(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter PDF para DOCX'})
            
            # Verifica se o arquivo enviado é PDF e o formato desejado é IMG
            if input_path.endswith('.pdf') and format.lower() == 'img':
                try:
                    return convert_pdf_to_image(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter PDF para IMG'})
                    
            
            # Converte PDF para texto
            if input_path.endswith('.pdf') and format.lower() == 'txt':
                try:
                    return convert_pdf_to_text(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter PDF para TXT'})

            # Converte formatos 'docx' em pdf ou txt    
            if input_path.endswith('.docx'):
                try:
                    return convert_docx_to_pdf(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter DOCX'})
            
            # Verifica se o arquivo é uma imagem para a conversão
            if input_path.endswith(('.png', '.jpg', '.gif')):
                try:
                    return convert_image(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter IMG'})
            
            # Verifica se o arquivo é um áudio para a conversão
            if input_path.endswith(('.mp3', '.wav', '.flac')):
                try:
                    return convert_audio(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter AUDIO'})
            
            
            # Verifica se o arquivo é um vídeo para a conversão
            if input_path.endswith(('.mp4', '.avi', '.mov')):
                try:
                    return convert_video(request, input_path, format)
                except Exception as e:
                    return Response({'error': 'Erro ao converter VÍDEO'})
            
            # Retorna erro se o formato não for suportado
            return Response({'error': 'Erro no upload'})
        
        # Retorna erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
