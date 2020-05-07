#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy 
import math
import cv2
def psnr(original_img, new_img):
    org_=cv2.imread(original_img)
    new_=cv2.imread(new_img)
    mse = numpy.mean( (org_- new_) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


# In[ ]:




