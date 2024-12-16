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

