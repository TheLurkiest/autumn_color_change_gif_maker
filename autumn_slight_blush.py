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

p_list_all_grass = ['Leafeon', 'Bulbasaur', 'Ivysaur', 'Venusaur', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Exeggcute', 'Exeggutor', 'Tangela', 'Chikorita', 'Bayleef', 'Meganium', 'Bellossom', 'Hoppip', 'Skiploom', 'Jumpluff', 'Sunkern', 'Sunflora', 'Celebi', 'back/Leafeon', 'back/Bulbasaur', 'back/Ivysaur', 'back/Venusaur', 'back/Oddish', 'back/Gloom', 'back/Vileplume', 'back/Paras', 'back/Parasect', 'back/Bellsprout', 'back/Weepinbell', 'back/Victreebel', 'back/Exeggcute', 'back/Exeggutor', 'back/Tangela', 'back/Chikorita', 'back/Bayleef', 'back/Meganium', 'back/Bellossom', 'back/Hoppip', 'back/Skiploom', 'back/Jumpluff', 'back/Sunkern', 'back/Sunflora', 'back/Celebi']

e_type_list = ['mareep', 'zapdos', 'emolga', 'joltik', 'back/mareep', 'back/zapdos', 'back/emolga', 'back/joltik']

# grass:
r_mutation_vector_grass = (2/3)
r2_mutation_vector_grass = (1/2)
g_mutation_vector_grass = (1/4)
b_mutation_vector_grass = (1/4)

# electric:
r_gamma_e_type = -(3/4)
r2_gamma_e_type = -(1/2)
g_gamma_e_type = (95/100)
b_gamma_e_type = (7/8)

# best source of gifs currently-- is NOW THIS INSTEAD:
# http://www.pokestadium.com/sprites/xy/cubone.gif
p_list_to_change=[]
a1_poke_id = 'venonat'
p_reply = a1_poke_id
a1_poke_id = str(p_reply)
p_type_choice = "G"

a1_poke_id = input('enter pokemon name or enter a type to create new mutations of for many different individuals of a given type at once-- for now "GRASS" and "ELECTRIC" --enter "G" or "E" to select one of these types-- for now these are the only types that allow for multiple individuals to be altered at once: ')
p_type_choice = a1_poke_id
if(a1_poke_id == 'G'):
    p_list_to_change = p_list_all_grass

    r_factor = r_mutation_vector_grass
    r2_factor = r2_mutation_vector_grass
    g_factor = g_mutation_vector_grass
    b_factor = b_mutation_vector_grass

    r_grass_buffer = -35
    b_grass_buffer = -45
    r_buff = r_grass_buffer
    b_buff = b_grass_buffer

elif(a1_poke_id == 'E'):
    p_list_to_change = e_type_list

    r_factor = r_gamma_e_type
    r2_factor = r2_gamma_e_type
    g_factor = g_gamma_e_type
    b_factor = b_gamma_e_type

    r_e_type_buffer = 14
    b_e_type_buffer = -29
    r_buff = r_e_type_buffer
    b_buff = b_e_type_buffer

else:
    p_list_to_change.append(a1_poke_id)

import requests

# ==========================================================================
# ==========================================================================

# ==========================================================================

for p_mon_elem in p_list_to_change:
    print('STARTING NEW POKEMON ALTERATIONS NOW: ' + str(p_mon_elem))
    print('----------------------------------------------------------------\n')

    a1_poke_id = str(p_mon_elem).lower()
    p_reply = a1_poke_id
    poke_id = str(p_reply)
    # ==========================================================================
    image_url = 'http://www.pokestadium.com/sprites/xy/'+str(a1_poke_id)+'.gif'
    s2 = poke_id
    if (s2.count('/') == 1):
        a1_poke_id = str(a1_poke_id[( a1_poke_id.find('/') + 1 ):]) + 'Back'
        p_reply = a1_poke_id
        poke_id = str(p_reply)
#>>> if (s2.count('/') == 1):
#...     s1=s1[(s1.find('/') +1):]


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


        if(p_type_choice == 'E'):
            # r is 30 higher than g and >100 higher than b

            a2 = b2[:,:,0] > b2[:,:,1] + 29
            a2_smooth = b2
            a2_smooth = b2[:,:,0] > b2[:,:,2] + 99
            booling2 = a2 & a2_smooth

            b2[:,:,0][booling2] = ( b2[:,:,0][booling2] + ( (b2[:,:,0][booling2]) ) * (r_gamma_e_type) )

            #b2[:,:,1][booling2] = ( b2[:,:,1][booling2] + ( 255 - (b2[:,:,1][booling2]) ) * (g_gamma_e_type) )
            b2[:,:,1][booling2] = ( b2[:,:,1][booling2] + ( 255 - (b2[:,:,1][booling2]) ) * (g_gamma_e_type) )

            b2[:,:,2][booling2] = ( b2[:,:,2][booling2] + ( 255 - (b2[:,:,2][booling2]) ) * (b_gamma_e_type) )

        else:
            a2 = b2[:,:,0] < b2[:,:,1] + r_buff
            a2_smooth = b2
            a2_smooth = b2[:,:,2] < b2[:,:,1] + b_buff
            booling2 = a2 & a2_smooth

            b2[:,:,0][booling2] = b2[:,:,0][booling2] + (( 255 - b2[:,:,0][booling2] ) * (r_factor))

            a3 = b2[:,:,0] < b2[:,:,1] - 11
            a3_smooth = b2
            a3_smooth=b2[:,:,2] < b2[:,:,1] - 11
            booling3 = a3 & a3_smooth
            b2[:,:,0][booling3] = b2[:,:,0][booling3] + ( (255 - b2[:,:,0][booling3]) * (r2_factor) )

            b2[:,:,2][booling2] = ((b2[:,:,2][booling2]) * (b_factor))
            #b2[:,:,1][booling2] = (b2[:,:,1][booling2])/2
            b2[:,:,1][booling2] = b2[:,:,1][booling2] - ((b2[:,:,1][booling2]) * (g_factor))



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

    os.system( str('cp ' + str('./' + ('poke_id' + str(poke_id)) + '_gif_frames' + '/' + 'output_poke_id' + str(poke_id) + 're_combo_anim2.gif')) + ' ' + './completed_color_change_animations/' + str(poke_id) + '_FALL_type3.gif')

    os.system('gifsicle --flip-horizontal ' + 'completed_color_change_animations/' + str(poke_id) + '_FALL_type3.gif' + ' -o ' + 'completed_color_change_animations/' + str(poke_id) + 'flipped_FALL_type3.gif' )




# --YOU MAY NEED TO ENTER THIS LAND THING BY HAND VIA THE TERMINAL-- IT WORKS
# WHEN EXECUTED AS A TERMINAL COMMAND (TO RE-CREATE TRANSPARENT BACKGROUND)
os.system('gifsicle -bII --transparent "#000000" completed_color_change_animations/*type3.gif')



#
