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


import os
import imageio

os.system('rm -r poke_id_gif_frames')
os.system('rm -r *saur_gif_frames/')
os.system('rm -r poke_id*')


a1_poke_p = 'ivysaur'
p_reply=''
p_reply=input('enter the name of a starting grass pokemon: ')
a1_poke_p = p_reply
a1 = io.imread(str(a1_poke_p)+'.png')

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
    imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif',images_in,fps=25)
    #imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif')
    return images_in

# gif_from_png_autumn




def gif_from_png_autumn(a1_within_pokemon):

    os.system('mkdir '+str(a1_within_pokemon) + '_gif_frames')

    png_dir = './' + str(a1_within_pokemon) + '_gif_frames/'
    images = []

    # now to make a gif from those .png files, it's as simple as this--
    # this creates a series of 25 images of slow color change you can use to make a gif:

    color_change_rate=10
    alpha1 = 'abcdefghijklmnopqrstuvwxyzZ'

    list_png=list(range(0,250,color_change_rate))
    for frame_elem in list_png:
        rgb_swap_pic[:,:,color_highlighted][booling2] = frame_elem
        if(frame_elem == 0):
            print('this is the current frame: ' + str(int(frame_elem)))
            print(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem)]) + str(frame_elem) + '_makeover_' + str(a1_within_pokemon) + '.png')
            imsave(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem)]) + str(frame_elem) + '_makeover_' + str(a1_within_pokemon) + '.png', rgb_swap_pic)
        else:
            print('this is the current frame: '+str(int(frame_elem/color_change_rate)))
            print(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem/color_change_rate)]) + str(frame_elem) + '_makeover_' + str(a1_within_pokemon)+'.png')
            imsave(str(png_dir) + 'gif_frame_' + str(alpha1[int(frame_elem/color_change_rate)]) + str(frame_elem) + '_makeover_' + str(a1_within_pokemon)+'.png', rgb_swap_pic)

    # check if ends in: '_makeover_' +str(a1_within_pokemon)+'.png' --below
    frame_num_start=0
    frame_num_end=0
    current_frame=0

    num1=[]
    file_name_list=[]

    for file_name in os.listdir(png_dir):
        frame_num_start = int(file_name.find('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ) +len('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ))
        frame_num_end = int(file_name.find('_makeover'))
        if file_name.endswith('_makeover_' +str(a1_within_pokemon)+'.png'):
            frame_num_start=int(file_name.find('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ) +len('frame_' + str(alpha1[int(frame_elem/color_change_rate)]) ))
            frame_num_end = int(file_name.find('_makeover'))
            file_name_list.append(file_name)
            #print('current frame is ' + str( int( file_name[frame_num_start:frame_num_end]) ) )

    print('\n\n-------------------------------------\n')

    file_name_list.sort()
    print('sorted file name list is: ' + str(file_name_list))

    print('our new function gets called for the first time with the normal list')
    images = fin_gif_out(a1_within_pokemon, png_dir, file_name_list, images, 'list_norm')

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
    images2 = fin_gif_out(a1_within_pokemon, png_dir2, file_name_list2, images2, 'flipped_list')

    # then we add both those lists together
    images = fin_gif_out(a1_within_pokemon, png_dir2, file_name_list2, images, 'list_combo')

    print('\n\n-----------------------------------------------------------\n')
    print('\n\n-----------------------------------------------------------\n')
    print('\n\n-----------------------------------------------------------\n')


gif_from_png_autumn(a1_poke_p)

# ========================================================================


a1 = io.imread('ivysaur.png')
a1_simp_gif=a1

#def simp_gif_maker():

a1_poke_id = '002'
a1 = io.imread(str(a1_poke_id)+'.gif')
a1_frame_test=a1[7,:,:,:]
plt.imshow(a1_frame_test)
plt.show()

a1_poke_id = '002'
a1 = io.imread(str(a1_poke_id)+'.gif')

r1=range(len(a1[:,:,:,0]))

frame_file_list=[]

os.system('mkdir ' + str('poke_id') + '_gif_frames')



new_file_name=''
images_anim = []

for frame_elem in r1:
    a1_frame_test=a1[frame_elem,:,:,:]
    a1_poke_id = '002'
    a1 = io.imread(str(a1_poke_id)+'.gif')
    b2=a1_frame_test
    a2=b2
    a2=b2[:,:,2] < b2[:,:,1] + 10

    booling2=a2
    #b2[:,:,0][booling2] = 255
    b2[:,:,0][booling2] = (b2[:,:,0][booling2] + 100)
    new_file_name='autumn_ivy_'+str(frame_elem)+'_makeover_'+str(a1_poke_id)+'.png'
    # new_file_name = str('autumn_ivy_' + str(frame_elem) + '_makeover_' + str(a1_poke_id) + '.png')
    plt.imsave( str('./' + str('poke_id') + '_gif_frames' + '/' + new_file_name), b2)
    frame_file_list.append(new_file_name)

# poke_id002gif_frames


# autumn_ivy_107_makeover_002.png

images_anim2=images_anim
images_anim2 = fin_gif_out_even('poke_id', str('./' + str('poke_id') + '_gif_frames' + '/'), frame_file_list, images_anim, 're_combo_anim')

#images = fin_gif_out(a1_frame_test, png_dir2, file_name_list2, images, 'list_combo')
images_anim = fin_gif_out('poke_id', str('./' + str('poke_id') + '_gif_frames' + '/'), frame_file_list, images_anim, 're_combo_anim2')
#images = fin_gif_out(a1_within_pokemon, png_dir, file_name_list, images, 'list_norm')

# a1_poke_id
print('\n\n--------------------------------')
print('frame_file_list is '+str(frame_file_list))


#simp_gif_maker()








# ========================================================================

#s>>> a1_poke_id='002'
#s>>> a1 = io.imread(str(a1_poke_id)+'.gif')
#>>> a1.shape
#(111, 51, 58, 3)
#>>> a1_frame = a1[:,:,0,:]
#>>> a1_frame.shape
#(111, 51, 3)



def fin_gif_out_combo(a1_in_in_pokemon, png_dir_in, file_name_list_in, images_in, gif_name_out):
    for count_file_elem, file_name in enumerate(file_name_list_in):
        file_name = ('autumn_ivy_0_makeover_00' + str(count_file_elem))
        png_dir_in = './poke_id_gif_frames/'
        if file_name.endswith('.png'):
            #l1[29][ (l1[29].find('_ivy_') + len('_ivy_')): l1[29].find('_makeover')]
            s1=''
            s1 = file_name[( file_name.find('frame_') + len('frame_') ): file_name.find('.png') ]
            print('s1 is: ' + str(s1))

            #autumn_ivy_0_makeover_002.png
            #if(int(s1) % 2 == 0):
            #    print('file_name '+str(file_name)+ 'should be even...')
            #if( int(): file_name.find('_makeover') ] ) % 2 == 0 ):
            #if( int( [ (file_name.find('_ivy_') + len('_ivy_')): file_name.find('_makeover') ] ) % 2 == 0 ):



            file_path = os.path.join(png_dir_in, file_name)
            images_in.append(imageio.imread(file_path))
            #/home/rustyb69/Desktop/example_pokemon_numpy_image_alteration/venusaur_fall_foliage/poke_id002_altered_gif/002id_frame_0.png
    imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(gif_name_out) + '2.gif',images_in,fps=55)
    return images_in

# this sort of thing will set things up so that only the even numbered items will get output if we incorporate this sort of thing into fin_gif_out_combo:
#>>> l2=[]
#>>> for elem_l in l1:
#...     if(elem_l % 2 == 0):
#...             l2.append(elem_l)
#...

# 'autumn_ivy_'+str(frame_elem)+'_makeover_'+str(a1_poke_id)+'.png'


    #imageio.mimsave('./' + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif',images_in,fps=25)
    #print('our new file is named using ' + str(file_name_list_in[0][:16]) + str(a1_in_in_pokemon) + '_gif_frames/' + 'output_' + str(a1_in_in_pokemon) + str(file_name_list_in[0][:16]) + '2.gif')
    return images_in



p_reply=input('enter "y" if you wish to alter an existing .gif now:')
if(p_reply=='y'):
    a1_poke_id=''
    p_reply=''
    p_reply=input('enter pokemon id as three digit number using zero characters preceding in order to fill your answer in to three digits if needed.')
    a1_poke_id=str(p_reply)
    a1 = io.imread(str(a1_poke_id)+'.gif')
    for frame_elem in range(len(a1[:,:,:,0])):
        a1_frame_test=a1[frame_elem,:,:,:]
        a2=a1_frame_test
        b2=a2
        b2=a2[:,:,1] > a2[:,:,2] + 10
        booling2 = b2
        a2[:,:,1][booling2] = 0
        plt.imsave('ivy_frame_'+str(frame_elem)+'.png',b2)


    gif_frames_range = range(a1.shape[2])

    altered_gif_list=[]
    # /home/rustyb69/Desktop/example_pokemon_numpy_image_alteration/venusaur_fall_foliage/
    # poke_id002_altered_gif/002id_frame_0.png
    png_dir_gif = str('./poke_id002_altered_gif/')
    os.system('mkdir ' + str('poke_id') + str(a1_poke_id) + '_altered_gif')

    images_gif2=[]

    for elem_frame in gif_frames_range:
        a1_frame = a1[:,:,elem_frame,:]
        a2_out_png = (str(a1_poke_id) + 'id_frame_' + str(elem_frame) + '.png')
        altered_gif_list.append(a2_out_png)



        color_prop_buffer_b = 9
        color_prop_buffer_c = color_prop_buffer_b

        # rgb here-- leaf is getting altered-- so highlight green-- which is 1.
        color_highlighted = 1
        color_b = 0
        color_c = 2

        # a1 frame [:,:, changed so that we can alter each image, frame by frame, and re-assemble at the end.
        boo_thresh_high_b = a1_frame[:,:,color_highlighted] > a1_frame[:,:,color_b] + color_prop_buffer_b
        boo_thresh_high_c = a1_frame[:,:,color_highlighted] > a1_frame[:,:,color_c] + color_prop_buffer_c

        booling2=boo_thresh_high_b & boo_thresh_high_c

        rgb_swap_pic = a1_frame
        rgb_swap_pic[:,:,color_highlighted][booling2] = 0

        images_gif2.append(rgb_swap_pic)

        #plt.imshow(rgb_swap_pic)
        #plt.show()

    # def fin_gif_out(a1_in_in_pokemon, png_dir_in, file_name_list_in, images_in, gif_name_out):
    # images = fin_gif_out(a1_within_pokemon, png_dir, file_name_list, images, 'list_norm')

    images_gif2 = fin_gif_out_combo('poke_id', png_dir_gif, altered_gif_list, images_gif2, 'out_back_to_gif')

# '/home/rustyb69/Desktop/example_pokemon_numpy_image_alteration/venusaur_fall_foliage/poke_id002_altered_gif/002id_frame_0.png'
print('images_gif2 is: '+str(images_gif2))









# =========================
