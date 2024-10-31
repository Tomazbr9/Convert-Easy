import os
from pydub import AudioSegment
from .useful_functions import download_return

# função para converter audios
def convert_audio(input_path, output_path, original_filename, extension):
    audio = AudioSegment.from_file(input_path)
    output_path = os.path.join(output_path, f'{original_filename}.{extension}')
    audio.export(output_path, format=extension)
    return download_return(output_path, original_filename, extension)

    