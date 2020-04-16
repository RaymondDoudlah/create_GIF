import PIL
from PIL import Image
import numpy as np
import glob

frames = []
allImgs = sorted(glob.glob("./practiceImages/large/*.png"))
print('Collecting images...')
for i in allImgs:
    print('Adding image: {}'.format(i))
    tmpImg = Image.open(i)

    # Calculate ratio to rescale image
    orig_W, orig_H = tmpImg.size
    origRatio = orig_H / orig_W
    new_W = 720
    new_H = int(np.round(720 * origRatio))  
    newImg = tmpImg.resize((new_W, new_H))
    tmpImg_resize = tmpImg.resize((new_W, new_H))
    frames.append(tmpImg_resize)
    
print('Saving GIF...')
frames[0].save('practiceGIFs/dti_GIF_720.gif',
              save_all=True, append_images=frames[1:],
              optimize=False, duration=100, loop=0)
print('GIF complete!')