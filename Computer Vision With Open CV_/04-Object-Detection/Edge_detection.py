import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../DATA/sammy_face.jpg')
plt.imshow(img)

edges = cv2.Canny(image=img, threshold1=127, threshold2=127)
plt.imshow(edges)

edges = cv2.Canny(image=img, threshold1=0, threshold2=255)
plt.imshow(edges)

# Choosing Thresholds
#  https://stackoverflow.com/questions/25125670/best-value-for-threshold-in-canny

# Calculate the median pixel value
med_val = np.median(img) 

# Lower bound is either 0 or 70% of the median value, whicever is higher
lower = int(max(0, 0.7* med_val))

# Upper bound is either 255 or 30% above the median value, whichever is lower
upper = int(min(255,1.3 * med_val))

edges = cv2.Canny(image=img, threshold1=lower , threshold2=upper)
plt.imshow(edges)

# Sometimes it helps to blur the images first, so we don't pick up minor edges.
blurred_img = cv2.blur(img,ksize=(5,5))
plt.imshow(blurred_img)

edges = cv2.Canny(image=blurred_img, threshold1=lower , threshold2=upper)
plt.imshow(edges)

#Let's play around with these threshold values even further! Often you'll need to experiment in regards to your specific dataset and what your final goal is.

edges = cv2.Canny(image=blurred_img, threshold1=lower , threshold2=upper+50)
plt.imshow(edges)