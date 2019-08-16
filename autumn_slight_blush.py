# autumn venusaur makeover:

# here is our newest gif url source--first front gif:
# http://www.pokestadium.com/sprites/xy/cubone.gif

# ...then back gif:
# http://www.pokestadium.com/sprites/xy/back/cubone.gif

# HOW TO USE:
# just enter this terminal command to use this python code:
#  python stripped_down_autumn_makeover5.py
# --for us, 'python' just defaults to python3.6 rather than 3.7
# ...which is what we want here-- also, don't use the usual virtual
# environment here either-- it won't work.

import random

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


import os
import imageio

os.system('rm -r poke_id_gif_frames')
os.system('rm -r *saur_gif_frames/')
os.system('rm -r poke_id*')

# ===================================================================
# now to turn created png into combined gif:



def fin_gif_out(a1_in_in_pokemon, png_dir_in, file_name_list_in, images_in, gif_name_out):
    for file_name in file_name_list_in:
        if file_name.endswith('.png'):
            file_path = os.path.join(png_dir_in, file_name)
            images_in.append(imageio.imread(file_path))
    print('\n\nHere is imageio.mimsave: '+str('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif'))
    imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif',images_in,fps=25)
    #imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif')
    return images_in

# gif_from_png_autumn

def fin_gif_out_even(a1_in_in_pokemon, png_dir_in, file_name_list_in, images_in, gif_name_out):
    for count_file_elem, file_name in enumerate(file_name_list_in):
        if file_name.endswith('.png'):
            if(count_file_elem % 2 == 0):
                file_path = os.path.join(png_dir_in, file_name)
                images_in.append(imageio.imread(file_path))
    print('\n\nHere is imageio.mimsave: '+str('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif'))
    imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif',images_in,fps=35)
    #imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif')
    return images_in

# ========================================================================

p_list_all = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Exeggcute', 'Exeggutor', 'Tangela', 'Chikorita', 'Bayleef', 'Meganium', 'Bellossom', 'Hoppip', 'Skiploom', 'Jumpluff', 'Sunkern', 'Sunflora', 'Celebi', 'back/Bulbasaur', 'back/Ivysaur', 'back/Venusaur', 'back/Oddish', 'back/Gloom', 'back/Vileplume', 'back/Paras', 'back/Parasect', 'back/Bellsprout', 'back/Weepinbell', 'back/Victreebel', 'back/Exeggcute', 'back/Exeggutor', 'back/Tangela', 'back/Chikorita', 'back/Bayleef', 'back/Meganium', 'back/Bellossom', 'back/Hoppip', 'back/Skiploom', 'back/Jumpluff', 'back/Sunkern', 'back/Sunflora', 'back/Celebi']

# best source of gifs currently-- is NOW THIS INSTEAD:
# http://www.pokestadium.com/sprites/xy/cubone.gif

p_list_to_change=[]

# ...therefore default value is now name-- not number:
a1_poke_id = 'venonat'
p_reply = a1_poke_id
a1_poke_id = str(p_reply)



a1_poke_id = input('enter pokemon name or enter "ALL" to add all pokemon of a given type listed: ')
if(a1_poke_id == 'ALL'):
    p_list_to_change = p_list_all
else:
    p_list_to_change.append(a1_poke_id)

import requests


# ==========================================================================
# ==========================================================================

# ==========================================================================

for p_mon_elem in p_list_to_change:
    print('STARTING NEW POKEMON ALTERATIONS NOW: ' + str(p_mon_elem))
    print('----------------------------------------------------------------\n')
    a1_poke_id = str(p_mon_elem)
    p_reply = a1_poke_id
    poke_id = str(p_reply)
    # ==========================================================================
    image_url = 'http://www.pokestadium.com/sprites/xy/'+str(a1_poke_id)+'.gif'

    img_data = requests.get(image_url).content
    with open(str(a1_poke_id)+'.gif', 'wb') as handler:
        handler.write(img_data)

    a1 = io.imread(str(a1_poke_id)+'.gif')
    a1_frame_test=a1[7,:,:,:]
    #plt.imshow(a1_frame_test)
    #plt.show()

    a1 = io.imread(str(a1_poke_id)+'.gif')

    r1=range(len(a1[:,:,:,0]))

    frame_file_list=[]

    poke_id = a1_poke_id

    os.system('mkdir ' + (str('poke_id') + str(poke_id)) + '_gif_frames')



    new_file_name=''
    images_anim = []

    for frame_elem in r1:


        # Use this terminal command to change a black background to transparent:
        ##### gifsicle -bII --transparent "#000000" anim_leafeon.gif
        # ...or to do EVERY gif in the directory:
        # ##### gifsicle -bII --transparent "#000000" *type3.gif

        a1_frame_test=a1[frame_elem,:,:,:]
        a1 = io.imread(str(a1_poke_id)+'.gif')
        b2=a1_frame_test
        a2=b2
        a3 = a2

        a2 = b2[:,:,0] < b2[:,:,1] - 35
        a2_smooth = b2
        a2_smooth=b2[:,:,2] < b2[:,:,1] - 45
        booling2 = a2 & a2_smooth
        b2[:,:,0][booling2] = b2[:,:,0][booling2] + (( 255 - b2[:,:,0][booling2] ) * (2/3))


        a3 = b2[:,:,0] < b2[:,:,1] - 11
        a3_smooth = b2
        a3_smooth=b2[:,:,2] < b2[:,:,1] - 11
        booling3 = a3 & a3_smooth
        b2[:,:,0][booling3] = b2[:,:,0][booling3] + ( (255 - b2[:,:,0][booling3]) * (1/2) )

        b2[:,:,2][booling2] = (b2[:,:,2][booling2])/4
        #b2[:,:,1][booling2] = (b2[:,:,1][booling2])/2
        b2[:,:,1][booling2] = b2[:,:,1][booling2] - (b2[:,:,1][booling2])/4

        b2_black_bg_bool = (b2[:,:,0] > 209) & (b2[:,:,2] < 5)

        a2 = b2
        a2_black = b2

        a2_black[:,:,0][b2_black_bg_bool] = 0

        a2 = a2_black

        #b2[:,:,0][booling2] = 255
        b2[:,:,2][booling2] = b2[:,:,2][booling2] - (b2[:,:,2][booling2] / 3)


        new_file_name='autumn_ivy_'+str(frame_elem)+'_makeover_'+str(a1_poke_id)+'.png'
        # new_file_name = str('autumn_ivy_' + str(frame_elem) + '_makeover_' + str(a1_poke_id) + '.png')
        plt.imsave( str('./' + (str('poke_id') + str(poke_id)) + '_gif_frames' + '/' + new_file_name), b2)
        frame_file_list.append(new_file_name)


    images_anim2=images_anim
    images_anim2 = fin_gif_out_even((str('poke_id') + str(poke_id)), str('./' + (str('poke_id') + str(poke_id)) + '_gif_frames' + '/'), frame_file_list, images_anim, 're_combo_anim')



    # =========================================================================
    # =========================================================================
    # =========================================================================
    os.system( str('cp ' + str('./' + ('poke_id' + str(poke_id)) + '_gif_frames' + '/' + 'output_poke_id' + str(poke_id) + 're_combo_anim2.gif')) + ' ' + './completed_color_change_animations/' + str(poke_id) + '_FALL_type3.gif')
