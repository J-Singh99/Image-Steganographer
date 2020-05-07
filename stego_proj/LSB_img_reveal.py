#IMPORTS
import cv2
import numpy as np
from .Tools import *

def lsbImgReveal(ImgPath, n, resImageName = 'revealed'):
    
    img = getImageFromPath(ImgPath)

    img_arr = np.asarray(img)

#   Spliting into RGB channels
    img_r_arr = img_arr[:,:,0]
    img_g_arr = img_arr[:,:,1]
    img_b_arr = img_arr[:,:,2]


#   Flattening each channel
    img_r_arr = img_r_arr.flatten()
    bin_r_arr = list(map(binary_value,img_r_arr))
    
    img_g_arr = img_g_arr.flatten()
    bin_g_arr = list(map(binary_value,img_g_arr))
    
    img_b_arr = img_b_arr.flatten()
    bin_b_arr = list(map(binary_value,img_b_arr))

    

    rec_len = ""
    for i in range(120):
        rec_len += bin_r_arr[i][-n:] + bin_g_arr[i][-n:] + bin_b_arr[i][-n:]

    
    counter = (len(rec_len) // 8) * 8
    
    rec_len = rec_len[0:counter]
    rec_arr = np.asarray(list(rec_len))
    rec_arr = rec_arr.reshape((-1,8))
    
    

    rec_list = []
    for elem in rec_arr:
        rec_list.append("".join(elem))

    
    dec_rec_list = list(map(int,list(map(binaryToDecimal,rec_list))))
    str_rec_list = list(map(chr,dec_rec_list))
    rec_str = "".join(str_rec_list)
    

    
    hiddenImgLen, height, width = rec_str.split(':')[0].split(',')
    
    lenHiddenImg = len(rec_str.split(':')[0]) * 8 + 8 + int(hiddenImgLen)


#   Error check
    if(type(lenHiddenImg) !=  int):
        print('UH OH... SOME ERROR... PLEASE CALL JASPREET!!')
        exit(-1)


    count = ((lenHiddenImg) + (3 - (lenHiddenImg) % 3)) // (3)
    count = (count + (n - count % n)) //  n 


#   Getting the image to be extracted 
    final_bin_str = ""
    for i in range(count):
        final_bin_str += bin_r_arr[i][-n:] + bin_g_arr[i][-n:] + bin_b_arr[i][-n:]

    
    counter = (len(final_bin_str) // 8) * 8
    final_bin_str = final_bin_str[0:counter]
    
    final_arr = np.asarray(list(final_bin_str))
    final_arr = final_arr.reshape((-1,8))
    
# Converting to array
    final_list = []
    for elem in final_arr:
        final_list.append("".join(elem))

    dec_final_list = list(map(int,list(map(binaryToDecimal,final_list))))
    str_final_list = list(map(chr,dec_final_list))

    index = len(rec_str.split(':')[0]) + 1
    end = int(hiddenImgLen)

    final_str = "".join(str_final_list)[index:]
    final_str = final_str[:end]
    
    len_of_chan = len(final_str) // 3

#   Adding the RGB channels
    chr_r_str = final_str[0:len_of_chan]
    chr_g_str = final_str[len_of_chan:len_of_chan * 2]
    chr_b_str = final_str[len_of_chan *  2 :]


    img_r_arr = list(map(ord,list(chr_r_str)))
    img_g_arr = list(map(ord,list(chr_g_str)))
    img_b_arr = list(map(ord,list(chr_b_str)))
    

    h = int(height)
    w = int(width)

#   Reconstructing RGB channels for final image (unflattening)
    img_r_arr = np.reshape(img_r_arr,(h,w))
    img_r_arr = img_r_arr.astype(np.uint8)
    
    img_g_arr = np.reshape(img_g_arr,(h,w))
    img_g_arr = img_g_arr.astype(np.uint8)
    
    img_b_arr = np.reshape(img_b_arr,(h,w))
    img_b_arr = img_b_arr.astype(np.uint8)
 

 #  Creating a shell, adding RGB channels, and constructing image
    final_img = np.zeros((h,w,3),np.uint8)

    final_img[:,:,0] = img_r_arr
    final_img[:,:,1] = img_g_arr
    final_img[:,:,2] = img_b_arr
    
#   Saving the image

    cv2.imwrite('./steganographer/static/cvt_to_ovt/rvldimg/'+str(resImageName)+".png", 
                cv2.cvtColor(final_img,cv2.COLOR_BGR2RGB))
    
    return str('./steganographer/static/cvt_to_ovt/rvldimg/'+str(resImageName)+".png")