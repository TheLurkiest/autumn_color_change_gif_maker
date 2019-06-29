# autumn venusaur makeover:

import numpy as np
from skimage import io
import imageio
import matplotlib.pyplot as plt

# ===========================================

import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob

# ===========================================

from scipy.misc import imsave

# ===========================================

# image .png and .gif sources:
# https://sprites.pokecheck.org/i/002.gif
# https://img.pokemondb.net/sprites/x-y/normal/ivysaur.png

#>>> a1 = io.imread('002.gif')
#>>> a1.shape
#(111, 51, 58, 3)

#>>> plt.imshow(a1)
#Traceback (most recent call last):
# ....................
#  File "/home/rustyb69/.local/lib/python3.6/site-packages/matplotlib/image.py", line 653, in set_data
#    raise TypeError("Invalid dimensions for image data")
#TypeError: Invalid dimensions for image data

#>>> a1 = io.imread('ivysaur.png')
#>>> a1.shape
#(120, 120, 4)
#>>> 


# =============================================================================
#for .png file, here is how you make changes:
# -----------------------------------------

#>>> a1 = io.imread('ivysaur.png')
#>>> a1.shape
#(120, 120, 4)
#>>> 
a1_pokemon = 'ivysaur'
a1 = io.imread(str(a1_pokemon)+'.png')

color_prop_buffer_b = 9
color_prop_buffer_c = color_prop_buffer_b

# rgb here-- leaf is getting altered-- so highlight green-- which is 1.
color_highlighted = 1
color_b = 0
color_c = 2

boo_thresh_high_b = a1[:,:,color_highlighted] > a1[:,:,color_b] + color_prop_buffer_b
boo_thresh_high_c = a1[:,:,color_highlighted] > a1[:,:,color_c] + color_prop_buffer_c
    
booling2=boo_thresh_high_b & boo_thresh_high_c

rgb_swap_pic = a1
rgb_swap_pic[:,:,color_highlighted][booling2] = 0

plt.imshow(rgb_swap_pic)
plt.show()

# this creates ONE image:
imsave('makeover1.png', rgb_swap_pic)
plt.imshow(rgb_swap_pic)
plt.show()

# ===================================================================

# now to turn created png into combined gif:

import os
import imageio
os.system('mkdir '+str(a1_pokemon) + '_gif_frames')

png_dir = './' + str(a1_pokemon) + '_gif_frames/'
images = []

# now to make a gif from those .png files, it's as simple as this--
# this creates a series of 25 images of slow color change you can use to make a gif:
list_png=list(range(0,250,10))
for frame_elem in list_png:
    rgb_swap_pic[:,:,color_highlighted][booling2] = frame_elem
    imsave(str(png_dir) + 'gif_frame_' + str(frame_elem)+ '_makeover_' +str(a1_pokemon)+'.png', rgb_swap_pic)

# check if ends in: '_makeover_' +str(a1_pokemon)+'.png' --below

for file_name in os.listdir(png_dir):
    if file_name.endswith('_makeover_' +str(a1_pokemon)+'.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))

imageio.mimsave('./' + str(a1_pokemon) + '_gif_frames/' + 'output_' + str(a1_pokemon) + '.gif', images)









