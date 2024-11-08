import os
from django.conf import settings
from pdf2docx import Converter
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from .useful_functions import compress_file, json_return, file_info

# Função que converte documentos pdf em docx
def convert_pdf_to_docx(request, input_path, format):
    output_path = file_info(input_path, format)

    try:
        cv = Converter(input_path)
        cv.convert(output_path, start=0, end=None) # type: ignore
        cv.close()
        return json_return(request, output_path)
    except Exception as e:
        print("Error:", e)
        return None

# Função que converte documentos pdf em imagem
def convert_pdf_to_image(request, input_path, extension):
    images = convert_from_path(input_path)
    output_path = os.path.join(settings.MEDIA_ROOT, 'conversions')
    original_filename = os.path.splitext(os.path.basename(input_path))[0]
    image_paths = []

    for i, image in enumerate(images):
        image_path = os.path.join(
            output_path, f'page{i + 1}.png')

        image.save(image_path, 'PNG')
    
        image_paths.append(image_path)

    zip_path = os.path.join(output_path, f'{original_filename}.zip')

    compress_file(image_paths, zip_path)
    return json_return(request, zip_path)


# Função que converte documentos pdf em texto
def convert_pdf_to_text(request, input_path, extension):
    text = extract_text(input_path)
    output_path = file_info(input_path, extension)
    
    with open(output_path, 'w') as file:
        file.write(text)

    return json_return(request, output_path)




