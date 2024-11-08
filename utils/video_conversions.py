import os
from moviepy.editor import VideoFileClip
from .useful_functions import download_return, json_return, file_info

# função para converter videos
def convert_video(request, input_path, extension):
    video = VideoFileClip(input_path)
    output_path = file_info(input_path, extension)
    video.write_videofile(
        output_path, codec='libx264' if extension == 'mp4' else 'libxvid')
    return json_return(request, output_path)
