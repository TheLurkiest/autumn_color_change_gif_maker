
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

a1_poke_id = '002'
a1 = io.imread(str(a1_poke_id)+'.gif')
a1_frame_test=a1[7,:,:,:]
plt.imshow(a1_frame_test)
plt.show()

a1_poke_id = '002'
a1 = io.imread(str(a1_poke_id)+'.gif')

r1=range(len(a1[:,:,:,0]))

#plt.imshow(a1)
#plt.show()

frame_file_list=[]

for frame_elem in r1:

	a1_frame_test=a1[frame_elem,:,:,:]

	a1_poke_id = '002'
	a1 = io.imread(str(a1_poke_id)+'.gif')
	frame_file_list.append(str(a1_poke_id) + '.gif')

	a1_frame_test.shape

	b2=a1_frame_test
	a2=b2
	a2=b2[:,:,2] < b2[:,:,1] + 10
	a2.shape

	booling2=a2
	#b2[:,:,0][booling2] = 255
	b2[:,:,0][booling2] = b2[:,:,0][booling2] + 100

	#plt.imshow(b2)
	#plt.show()
	plt.imsave('autumn_ivy_'+str(frame_elem)+'.png',b2)


print('\n\n--------------------------------')
print('frame_file_list is '+str(frame_file_list))
