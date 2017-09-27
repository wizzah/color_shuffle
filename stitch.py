import imageio
import os
import settings

def stitch():

    images = []
    sort_names = []

    for filename in os.listdir(settings.directory):
        if filename.endswith(settings.input_filetype):
            sort_names.append(int(filename[:-(len(settings.input_filetype))]))

    # this avoids that filename iteration problem with digits
    sort_names = sorted(sort_names)
    for file in sort_names:
            try:
                images.append(imageio.imread(settings.directory+"/"+str(file)+settings.input_filetype))
            except: 
                imageio.mimsave(settings.attempted_output_filename, images)
    imageio.mimsave(settings.output_filename, images)
    return settings.output_filename
    # current issue: https://github.com/imageio/imageio/issues/210