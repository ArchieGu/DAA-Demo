import os 
from PIL import Image



def rotate(path, outdir):
    out_dir = './DAA/'+outdir
    if outdir not in os.listdir('./DAA'):
        os.mkdir(out_dir)

    angel = 0
    increase = 0.1 
    image = Image.open(path)

    while True:
        angel += increase 
        if angel >= 360:
            break 

        rotated_image = image.rotate(angel)
        name = str(round(angel,1)) + '.png'
        rotated_image.save(os.path.join(out_dir, name))


if __name__ == '__main__':
    path = './DAA/1.png'
    outdir = 'compass'
    rotate(path, outdir)