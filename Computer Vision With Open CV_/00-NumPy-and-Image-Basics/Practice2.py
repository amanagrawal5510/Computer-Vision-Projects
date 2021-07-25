import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from PIL import Image

pic = Image.open('00-puppy.jpg')

#pic
#print(type(pic))

# =============================================================================
# pic_arr = np.asarray(pic)
# type(pic_arr)
# pic_arr.shape
# plt.imshow(pic_arr)
# =============================================================================

pic_red = pic_arr.copy()

pic_red.shape

plt.imshow(pic_red[:,:,0],cmap="gray")

pic_red[:,:,1] = 0
pic_red[:,:,2] = 0

plt.imshow(pic_red)

# =============================================================================
# pic_x = pic_red[:,:,0]
# plt.imshow(pic_x)
# Not Worked
# =============================================================================

