import os
from PIL import Image
from math import sqrt

original_images_path = "data/original_images/"
resized_images_path = "data/resized_images/"
small_images_RGB_dict = {}
input_image_RGB_dict = {}


def resize():
    """
    Resize images in 'original_images' directory to 20*20 pixels,
    then save the resized ones in 'resized_images' directory.
    """
    dirs = os.listdir(original_images_path)
    for item in dirs:
        if os.path.isfile(original_images_path + item):
            im = Image.open(original_images_path + item)
            imResize = im.resize((20, 20), Image.ANTIALIAS)
            imResize.save(resized_images_path + 'resized_' + item, 'JPEG', quality=90)


# resize()

def get_avg_RGB(img):
    """
    Given PIL Image,calculate the average RGB values,
    and define this as the average color of the image.
    """
    R = []
    G = []
    B = []
    width, height = img.size
    for w in range(width):
        for h in range(height):
            r, g, b = img.getpixel((w, h))
            R.append(r)
            G.append(g)
            B.append(b)
    return [sum(R) / len(R), sum(G) / len(G), sum(B) / len(B)]


def get_pixels_RGB(image):
    """
    Given PIL image, store pixels RGB values  in 'Big_image_RGB_dict'.
    """
    input_img = Image.open(image)
    width, height = input_img.size
    key = 0  # used as dictionary key
    for w in range(width):
        for h in range(height):
            a = input_img.getpixel((w, h))
            input_image_RGB_dict['tile' + str(key)] = a
            key += 1


def nearest():
    """
    For every pixel in 'input_image_RGB_dict', find closest tile from 'small_images_RGB_dict',
    store them in 'final tiles' and return it .
    The closest tile is the tile which has the minimum Euclidean distance between rgb values.
    """
    diff = {}
    final_tiles = []  # a set of small images which will replaced the input image pixel
    for pixel in input_image_RGB_dict.keys():
        r_pixel, g_pixel, b_pixel = input_image_RGB_dict[pixel]
        for tile in small_images_RGB_dict.keys():
            r_tile, g_tile, b_tile = small_images_RGB_dict[tile]
            distance = sqrt((r_pixel - r_tile) ** 2 + (g_pixel - g_tile) ** 2 + (b_pixel - b_tile) ** 2)
            diff[tile] = distance
        final_tiles.append(min(diff, key=diff.get))
    return final_tiles