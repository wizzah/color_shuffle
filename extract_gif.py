import os
from PIL import Image
import settings

def extractFrames(gif, output_folder):
    frame = Image.open(gif)
    nframes = 0
    while frame:
        frame.save( '%s/%s%s' % (output_folder, nframes, settings.input_filetype) , 'GIF')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True
    

extractFrames(settings.input_filename, settings.directory)