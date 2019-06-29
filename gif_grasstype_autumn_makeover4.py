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
p_reply=''
p_reply=input('enter the name of a starting grass pokemon: ')
a1_pokemon = p_reply
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

# ===================================================================

# now to turn created png into combined gif:

import os
import imageio
os.system('mkdir '+str(a1_pokemon) + '_gif_frames')

png_dir = './' + str(a1_pokemon) + '_gif_frames/'
images = []

# now to make a gif from those .png files, it's as simple as this--
# this creates a series of 25 images of slow color change you can use to make a gif:

color_change_rate=10
alpha1 = 'abcdefghijklmnopqrstuvwxyzZ'

#l1=[]
#s1=alpha1
#r1=range(len(s1))
#for elem_r in r1:
#    l1.append(s1[elem_r])
#l2=l1

list_png=list(range(0,250,color_change_rate))
for frame_elem in list_png:
    rgb_swap_pic[:,:,color_highlighted][booling2] = frame_elem
    if(frame_elem == 0):
        print('this is the current frame: ' + str(int(frame_elem)))
        print(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem)]) + str(frame_elem) + '_makeover_' + str(a1_pokemon) + '.png')
        imsave(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem)]) + str(frame_elem) + '_makeover_' + str(a1_pokemon) + '.png', rgb_swap_pic)
    else:
        print('this is the current frame: '+str(int(frame_elem/color_change_rate)))
        print(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem/color_change_rate)]) + str(frame_elem) + '_makeover_' + str(a1_pokemon)+'.png')
        imsave(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem/color_change_rate)]) + str(frame_elem) + '_makeover_' + str(a1_pokemon)+'.png', rgb_swap_pic)

# check if ends in: '_makeover_' +str(a1_pokemon)+'.png' --below
frame_num_start=0
frame_num_end=0
current_frame=0

num1=[]
file_name_list=[]

# 'frame_' + str(alpha1[int(frame_elem/color_change_rate)]    )

for file_name in os.listdir(png_dir):
    frame_num_start = int(file_name.find('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ) +len('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ))
    frame_num_end = int(file_name.find('_makeover'))
    if file_name.endswith('_makeover_' +str(a1_pokemon)+'.png'):
        frame_num_start=int(file_name.find('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ) +len('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ))
        frame_num_end = int(file_name.find('_makeover'))
        file_name_list.append(file_name)
        #print('current frame is ' + str( int( file_name[frame_num_start:frame_num_end]) ) )


def fin_gif_out(a1_pokemon_in, png_dir_in, file_name_list_in, images_in, gif_name_out):
    for file_name in file_name_list_in:
        if file_name.endswith('_makeover_' +str(a1_pokemon_in)+'.png'):
            file_path = os.path.join(png_dir_in, file_name)
            images_in.append(imageio.imread(file_path))
    imageio.mimsave('./' + str(a1_pokemon_in) + '_gif_frames/' + 'output_' + str(a1_pokemon_in) + str(gif_name_out) + '2.gif',images_in,fps=25)
    #imageio.mimsave('./' + str(a1_pokemon_in) + '_gif_frames/' + 'output_' + str(a1_pokemon_in) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_pokemon_in) + '_gif_frames/' + 'output_' + str(a1_pokemon_in) + str(file_name_list_in[0][:16]) + '2.gif')


print('\n\n-------------------------------------\n')

file_name_list.sort()
print('sorted file name list is: ' + str(file_name_list))

print('our new function gets called for the first time with the normal list')
fin_gif_out(a1_pokemon, png_dir, file_name_list, images, 'list_norm')

print('\n\n-------------------------------------\n')
print('\n\n-----------------------------------------------------------\n')


file_name_list2 = file_name_list
images2=[]
png_dir2=png_dir

print('\n\n-----------------------------------------------------------\n')
print('\n\n-------------------------------------\n')


file_name_list2.reverse()
print('reverse file name list is: ' + str(file_name_list2))

print('\n\n-------------------------------------\n')

print('...and now the reverse list is plugged into our function: ')
fin_gif_out(a1_pokemon, png_dir2, file_name_list2, images2, 'flipped_list')








# then we add both those lists together
