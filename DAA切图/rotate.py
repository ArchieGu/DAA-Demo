import os 
from PIL import Image


def rotate(path, outdir):
    out_dir = './DAA切图/'+outdir
    if outdir not in os.listdir('./DAA切图'):
        os.mkdir(out_dir)

    angel = 0
    increase = 1.5 
    image = Image.open(path)

    while True:
        angel += increase 
        if angel >= 360:
            break 

        rotated_image = image.rotate(angel)
        name = str(angel) + '.png'
        rotated_image.save(os.path.join(out_dir, name))


if __name__ == '__main__':
    path = './DAA切图/编组.png'
    outdir = 'compass'
    rotate(path, outdir)