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

# gif_from_png_autumn
def fin_gif_out_all(a1_in_in_pokemon, png_dir_in, file_name_list_in, images_in, gif_name_out):
    for count_file_elem, file_name in enumerate(file_name_list_in):
        if file_name.endswith('x1.png'):
            if(count_file_elem % 2 == 0):
                file_path = os.path.join(png_dir_in, file_name)
                images_in.append(imageio.imread(file_path))
            else:
                file_path = os.path.join(png_dir_in, file_name)
                images_in.append(imageio.imread(file_path))
    print('\n\nHere is imageio.mimsave: '+str('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif'))
    imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif',images_in,fps=35)
    #imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif')
    return images_in
# gif_from_png_autumn

def fin_gif_out_all777(a1_in_in_pokemon, png_dir_in, file_name_list_in, images_in, gif_name_out):
    for count_file_elem, file_name in enumerate(file_name_list_in):
        if file_name.endswith('x777.png'):
            if(count_file_elem % 2 == 0):
                file_path = os.path.join(png_dir_in, file_name)
                images_in.append(imageio.imread(file_path))
            else:
                file_path = os.path.join(png_dir_in, file_name)
                images_in.append(imageio.imread(file_path))
    print('\n\nHere is imageio.mimsave: '+str('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2777.gif'))
    imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2777.gif',images_in,fps=35)
    #imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif')
    return images_in





# ========================================================================
# source of grass types comes from here: https://sprites.pokecheck.org/i/272.gif

# best source of gifs currently-- is NOW THIS INSTEAD:
# http://www.pokestadium.com/sprites/xy/cubone.gif

# ...therefore default value is now name-- not number:
a1_poke_id = 'venonat'
p_reply = a1_poke_id

a1_poke_id = str(p_reply)

a1_poke_id = input('enter pokemon name: ')
import requests

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
    a1_frame_test=a1[frame_elem,:,:,:]
    a1 = io.imread(str(a1_poke_id)+'.gif')
    b2=a1_frame_test
    a2=b2
    a3 = a2
    a2 = b2[:,:,0] < b2[:,:,1] - 11
    a2_smooth = b2
    a2_smooth=b2[:,:,2] < b2[:,:,1] - 11

    booling2 = a2 & a2_smooth

    b2[:,:,0][booling2] = 255

    a2 = b2

    #booling2=a2
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



p_type_radfall = input('enter NUKE to change electric pokemon type to radiation or FALL to create autumnal version of some grass type: ')

images_gif2 = []
images_gif3 = []
images_gif4 = []
images_gif5 = []
if(a1_poke_id == str(poke_id) ):
    a1 = io.imread(str(a1_poke_id)+'.gif')
    for frame_elem in range(len(a1[:,:,:,0])):
        a1_frame_test=a1[frame_elem,:,:,:]
        a2=a1_frame_test

        b2=a2


        # radiation type:
        if(p_type_radfall == 'NUKE'):
            b2=a2[:,:,1] > a2[:,:,2] + 10
            booling2 = b2
            a2[:,:,0][booling2] = a2[:,:,0][booling2] / 2
            a2[:,:,2][booling2] = a2[:,:,2][booling2] / 2
            a2[:,:,1][booling2] = a2[:,:,1][booling2] + ( (255 - (a2[:,:,1][booling2]))/2 )
        else:
            # 50 r ... 70 b
            color_uno_main_buff = 65
            color_dos_main_buff = 17
            b2=a2[:,:,1] > a2[:,:,0] + 52
            booling2 = b2
            booling3=a2[:,:,1] > a2[:,:,2] + 61

            booling4 = booling2 & booling3

            a2[:,:,1][booling4] = (a2[:,:,1][booling4] / 2) + 1
            a2[:,:,2][booling4] = (a2[:,:,2][booling4] / 2) + 1
            a2[:,:,0][booling4] = a2[:,:,0][booling4] + ( (255 - (a2[:,:,0][booling4]))/2 )

            a3 = a2
            a4 = a3

            shine_bool = (a4[:,:,0] > 200) & (a4[:,:,1] > 200)
            a3[shine_bool] = 230 + random.randint(0,5)

            booling5 = booling4
            booling6 = booling4

            buff_light_uno = color_uno_main_buff - (color_uno_main_buff / 3)
            buff_light_dos = color_dos_main_buff - (color_dos_main_buff / 4)

            color_highlighted = 1
            color_uno = 0
            color_dos = 2

            # a1 frame [:,:, changed so that we can alter each image, frame by frame, and re-assemble at the end.
            boo_thresh_high_b = a3[:,:,color_highlighted] > a3[:,:,color_uno] + buff_light_uno
            boo_thresh_high_c = a3[:,:,color_highlighted] > a3[:,:,color_dos] + buff_light_dos

            booling6=boo_thresh_high_b & boo_thresh_high_c

            booling7 = a3[:,:,color_uno] < 200
            booling8 = a3[:,:,color_dos] < 200

            booling9 = booling6 & booling7 & booling8
            #rgb_swap_pic = a2
            #rgb_swap_pic[:,:,color_highlighted][booling6] = a2[:,:,color_hig_hlighted][booling6]



            # IF RED AND GREEN ARE BOTH GREATER THAN 200 THEN: REFLECTION--
            # MEANING,
            a7 = a3

            a7[:,:,1][booling9] = (a7[:,:,1][booling9] / 4) + 2
            a7[:,:,2][booling9] = (a7[:,:,2][booling9] / 4) + 2
            a7[:,:,0][booling9] = a7[:,:,0][booling9] + ( ( 255 - (a7[:,:,0][booling9]) )/2 )



            booling10 = a3[:,:,0] > a3[:,:,1]
            booling11 = a3[:,:,2] > a3[:,:,1]
            booling12 = booling10 & booling11

            a4 = a3
            a4[:,:,0][booling12] = a3[:,:,0][booling12] + ( ( 255 - (a3[:,:,0][booling12]) ) * ((a3[:,:,1][booling12]) - (a3[:,:,0][booling12]) + 1)/255 )
            a5 = a4
            a5[:,:,2][booling12] = a4[:,:,2][booling12] + ( ( 255 - (a4[:,:,2][booling12]) ) * ((a4[:,:,1][booling12]) - (a4[:,:,2][booling12]) + 1)/255 )

            a7 = a5

        plt.imsave('ivy_frame_'+str(frame_elem)+'x1.png',a2)
        images_gif2.append('ivy_frame_'+str(frame_elem)+'x1.png')

        a7 = a2

        plt.imsave('ivy777_frame_'+str(frame_elem)+'x777.png',a7)
        images_gif4.append('ivy777_frame_'+str(frame_elem)+'x777.png')



images_gif3 = fin_gif_out_all( str(str('poke_id') + str(poke_id)), str('./'), images_gif2, images_gif3, 're_combo_anim_xy' )
images_gif5 = fin_gif_out_all777( str(str('poke_id') + str(poke_id)), str('./'), images_gif4, images_gif5, 're_combo_anim_xy777' )


os.system( str('cp ' + str('./' + ('poke_id' + str(poke_id)) + '_gif_frames' + '/' + 'output_poke_id' + str(poke_id) + 're_combo_anim_xy7772777.gif')) + ' completed_color_change_animations/' + str(poke_id) + str(p_type_radfall) + '_type2.gif')
os.system( str('cp ' + str('./' + ('poke_id' + str(poke_id)) + '_gif_frames' + '/' + 'output_poke_id' + str(poke_id) + 're_combo_anim_xy2.gif')) + ' completed_color_change_animations/' + str(poke_id) + str(p_type_radfall) + '_type1.gif')


#

##333333333333



print('displaying original gif now...')
a1_poke_id = str(poke_id)
a1 = io.imread(str(a1_poke_id)+'.gif')
a1_frame_test=a1[7,:,:,:]
plt.imshow(a1_frame_test)
plt.show()
