import os
from PIL import Image

original_images_path = "data/original_images/"
resized_images_path = "data/resized_images/"


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


#resize()

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