import os
from PIL import Image
from .useful_functions import download_return

# função para converter imagens
def convert_image(input_path, outut_path, original_name, extension):
    img = Image.open(input_path)
    outut_path = os.path.join(outut_path, f'{original_name}.{extension}')
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    img.save(outut_path, format=extension.upper())
    return download_return(outut_path, original_name, extension)
