import os
from pdf2docx import Converter
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from .useful_functions import download_return, compress_file

# Função que converte documentos pdf em docx
def convert_pdf_to_docx(input_path, output_path, original_filename):
    extension = 'docx'
    output_path = os.path.join(output_path, f'{original_filename}.{extension}')
    try:
        cv = Converter(input_path)
        cv.convert(output_path, start=0, end=None) # type: ignore
        cv.close()
        return download_return(
            input_path, output_path, original_filename, extension)
    except Exception as e:
        print("Error:", e)
        return None

# Função que converte documentos pdf em imagem
def convert_pdf_to_image(input_path, output_path, original_filename):
    extension = 'png'
    images = convert_from_path(input_path)

    image_paths = []

    for i, image in enumerate(images):
        image_path = os.path.join(
            output_path, f'page{i + 1}.{extension}')

        image.save(image_path, 'PNG')
    
        image_paths.append(image_path)
    
    zip_path = os.path.join(output_path, f'{original_filename}.zip')
    
    compress_file(image_paths, zip_path)
    
    return download_return(input_path, zip_path, original_filename, 'zip')


# Função que converte documentos pdf em texto
def convert_pdf_to_text(input_path, output_path, original_filename):
    extension = 'txt'
    text = extract_text(input_path)
    output_path = os.path.join(output_path, f'{original_filename}.{extension}')
    
    with open(output_path, 'w') as file:
        file.write(text)

    return download_return(input_path, output_path, original_filename, 'txt')




