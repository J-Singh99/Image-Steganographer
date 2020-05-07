#IMPORTS
import numpy as np
import cv2
from .Tools import *
import os


def lsbTextHide(imgPath, message, lsb_num = 2, resImageName = 'resultant_img'):

    input_img = getImageFromPath(imgPath)

    inp_string_bin = a2bits(message)
    prelen = str(len(inp_string_bin)) + ':'
    bin_str = a2bits(prelen)+inp_string_bin

    max_cap=((input_img.size) * 8 * lsb_num)//8

    if(len(bin_str)>max_cap):
        print("FAILED!!!\nInput a smaller message, or increase the bit length.\n(Optimal bit length is usually 2)")
        exit(0)

    
    #get the dimensions
    height, width, chans = input_img.shape


    img_arr = np.asarray(input_img)

    #Convering the overt image to array form, separate channels
    img_r_arr = img_arr[:,:,0] #red channel
    img_g_arr = img_arr[:,:,1] #green channel
    img_b_arr = img_arr[:,:,2] #blue channel

    #flattening the image
    img_r_arr = img_r_arr.flatten()
    bin_r_arr = list(map(binary_value,img_r_arr))

    img_g_arr = img_g_arr.flatten()
    bin_g_arr = list(map(binary_value,img_g_arr))

    img_b_arr = img_b_arr.flatten()
    bin_b_arr = list(map(binary_value,img_b_arr))


    bin_str_arr = np.asarray(list(bin_str))
    bin_str_arr = bin_str_arr.reshape((-1, lsb_num))
 

    #convert to array
    bin_list=[]
    for elem in bin_str_arr:
        bin_list.append("".join(elem))

    
    r_count=0
    g_count=0
    b_count=0
    
    for i in range (len(bin_list)):
        
        chan = i%3 #RGB -> 0, 1, 2
        
        if chan == 0:
            bin_r_arr[r_count] = bin_r_arr[r_count][0:8 - lsb_num] + bin_list[i]
            r_count += 1
        
        elif chan == 1:
            bin_g_arr[g_count] = bin_g_arr[g_count][0:8 - lsb_num] + bin_list[i]
            g_count += 1
        
        elif chan == 2:
            bin_b_arr[b_count] = bin_b_arr[b_count][0:8 - lsb_num] + bin_list[i]
            b_count += 1

   
    final_img=np.zeros(input_img.shape,np.uint8)

    dec_r_arr=list(map(binaryToDecimal,bin_r_arr))
    dec_r_arr=np.reshape(dec_r_arr,(height,width))
    dec_r_arr=dec_r_arr.astype(np.uint8)
   
    dec_g_arr=list(map(binaryToDecimal,bin_g_arr))
    dec_g_arr=np.reshape(dec_g_arr,(height,width))
    dec_g_arr=dec_g_arr.astype(np.uint8)
   
    dec_b_arr=list(map(binaryToDecimal,bin_b_arr))
    dec_b_arr=np.reshape(dec_b_arr,(height,width))
    dec_b_arr=dec_b_arr.astype(np.uint8)


    # Reconstructing image
    final_img[:,:,0]=dec_r_arr
    final_img[:,:,1]=dec_g_arr
    final_img[:,:,2]=dec_b_arr


    #saving the final image
    print('TEXT HIDDEN SUCCESFULLY!!!')

    dirname = os.path.dirname(__file__)
    

    cv2.imwrite('./steganographer/static/ovt_to_cvt/mainHide/'+str(resImageName)+".png", 
                cv2.cvtColor(final_img,cv2.COLOR_BGR2RGB))
    
    return str('./steganographer/static/ovt_to_cvt/mainHide/'+str(resImageName)+".png")
    #cv2.imwrite("./" + resImageName + ".png",cv2.cvtColor(final_img,cv2.COLOR_BGR2RGB))
    #print('The file name: ' + str(resImageName) + '.png')