import imageio
import os
import math
import PIL
from PIL import Image
import settings

# images = []

def brightness(r, g, b):
    r = (r*r*0.241)
    g = (g*g*0.691)
    b = (b*b*0.068)
    brightness = math.sqrt(r+g+b)
    return brightness


def process_gif():
    sort_names = []

    for filename in os.listdir(settings.directory):
        if filename.endswith(settings.input_filetype):
            # basically makes a list of the filenames without the filetype at the end-
            # so, a list of numbers
            sort_names.append(int(filename[:-(len(settings.input_filetype))]))

    # pixel_list = []
    sort_names = sorted(sort_names)
    for file in sort_names:

        imgobj = Image.open(settings.directory+"/"+str(file)+settings.input_filetype)

        pixels = imgobj.convert('RGBA')
        data = list(pixels.getdata())

        old_data = list(pixels.getdata())
        old_pixels = []
        for pixel in old_data:
            old_pixels.append(list(pixel))

        new_img = []
        for ind, pixel in enumerate(data):
            pixel_info = list(pixel)

            # lots of options here to play with

            if pixel_info[0] < pixel_info[1]:
                pixel_info[0] += 10

            bright = brightness(pixel_info[0], pixel_info[1], pixel_info[2])
            if bright <= 100:
                # is bright
                pixel_info[1] += 13
                pixel_info[2] += 99
            elif bright >= 200:
                # not bright
                pixel_info[2] = 20

            if pixel_info[0] < old_data[ind][1]:
                pixel_info[0] -= 20
                pixel_info[2] += 45

            if pixel_info[1] + 50 < 255:
                pixel_info[1] += 10
            else:
                pixel_info[1] -= 10

            if ind + 3 < len(data):
                pixel_info[1] = data[ind+3][2]
                pixel_info[2] += 50

            if ind - 1 < len(data) and ind - 1 > 0:
                pixel_info[1] -= data[ind-1][2]

            new_img.append(tuple(pixel_info))
        try:
            im = Image.new(pixels.mode, pixels.size)
            im.putdata(new_img)
            im.save(settings.directory+"/"+str(file)+settings.input_filetype)
        except Exception as e:
            print e
