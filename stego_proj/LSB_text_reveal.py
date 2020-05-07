#IMPORTS
import cv2
import numpy as np
from .Tools import *


def lsbTextReveal(imgPath, n):
    img = getImageFromPath(imgPath)
    img_arr = np.asarray(img)

    img_r_arr = img_arr[:,:,0]
    img_g_arr = img_arr[:,:,1]
    img_b_arr = img_arr[:,:,2]

    img_r_arr = img_r_arr.flatten()
    bin_r_arr = list(map(binary_value,img_r_arr))
    img_g_arr = img_g_arr.flatten()
    bin_g_arr = list(map(binary_value,img_g_arr))
    img_b_arr = img_b_arr.flatten()
    bin_b_arr = list(map(binary_value,img_b_arr))

    rec_len = ""
    for i in range(100):
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
    mess_len = rec_str.split(':')[0]

    len_of_message = len(rec_str.split(':')[0]) * 8 + 8 + int(mess_len)

    count = ((len_of_message) + (3 - (len_of_message) % 3)) // (3)
    count = (count + (n - count % n)) // n


    final_bin_str = ""
    for i in range(count):
        final_bin_str += bin_r_arr[i][-n:] + bin_g_arr[i][-n:] + bin_b_arr[i][-n:]

    counter = (len(final_bin_str) // 8) * 8
    final_bin_str = final_bin_str[0:counter]
    final_arr = np.asarray(list(final_bin_str))
    
    final_arr = final_arr.reshape((-1,8))
    final_list = []
    for elem in final_arr:
        final_list.append("".join(elem))
    
    dec_final_list = list(map(int,list(map(binaryToDecimal,final_list))))
    str_final_list = list(map(chr,dec_final_list))

    index = len(rec_str.split(':')[0]) + 1
    end = int(mess_len) // 8
    final_str = "".join(str_final_list)[index:]
    final_str = final_str[:end]
    

    FINAL_MESSAGE = final_str
   
    if FINAL_MESSAGE:
        print('TEXT RETRIEVED SUCCESFULLY!!!')
        return FINAL_MESSAGE
    else:
        print('TEXT RETRIEVAL ERROR!!')
        return(-1)