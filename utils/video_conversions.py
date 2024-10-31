import os
from moviepy.editor import VideoFileClip
from .useful_functions import download_return

# função para converter videos
def convert_video(input_path, output_path, original_filename, extension):
    video = VideoFileClip(input_path)
    output_path = os.path.join(output_path, f'{original_filename}.{extension}')
    video.write_videofile(
        output_path, codec='libx264' if extension == 'mp4' else 'libxvid')
    return download_return(output_path, original_filename, extension)
