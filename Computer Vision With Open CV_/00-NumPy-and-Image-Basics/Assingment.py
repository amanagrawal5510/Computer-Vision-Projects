import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from PIL import Image

# =============================================================================
# arr = np.zeros(shape=(5,5))
# arr[:,:] = 10 
# 
# # This line sets a "seed" so you get the same random numbers we do
# np.random.seed(101)
# # This line creates an array of random numbers
# prr = np.random.randint(low=0,high=100,size=(5,5))
# 
# prr.max()
# prr.min()
# 
# =============================================================================
pic =  Image.open('00-puppy.jpg')

pic_blue = np.asarray(pic)

plt.imshow(pic_blue)


pic_blue[:,:,1] = 0

pic_blue[:,:,0] = 0

plt.imshow(pic_blue)