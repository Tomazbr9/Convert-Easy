import os
from PIL import Image
from .useful_functions import json_return, file_info

# função para converter imagens
def convert_image(request, input_path, extension):
    img = Image.open(input_path)
    output_path = file_info(input_path, extension)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    try:
        img.save(output_path, format=extension.upper())
        return json_return(request, output_path)
    except Exception as e:
        print("erro ao converter imagem: ", e)
