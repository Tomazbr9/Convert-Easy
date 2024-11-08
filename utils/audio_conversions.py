import os
from pydub import AudioSegment
from .useful_functions import download_return, json_return, file_info

# função para converter audios
def convert_audio(request, input_path, extension):
    audio = AudioSegment.from_file(input_path)
    output_path = file_info(input_path, extension)
    audio.export(output_path, format=extension)
    return json_return(request, output_path)

    