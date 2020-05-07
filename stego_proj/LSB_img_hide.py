#IMPORTS
import numpy as np
import cv2
from .Tools import *
import os

def getRatio(height, width, chans, max_cap):
	
	range_ = np.linspace(1,0,101)[1:]
		
	for i in range_:
		
		input_img_size = (((height * i)//1) * ( (width * i)//1) * chans) * 8

		if(max_cap > input_img_size):
			ratio = i
			break

	return ratio


def imgtoString(imgPath,max_cap):
	
	try:
		input_img = getImageFromPath(imgPath)
	except:
		print('top lol')
		print("Failed to load the overt image.\nPlease try again. \nMake sure the overt file path is correctly specified.")
		exit(-1)
		

	#get the dimensions
	height, width, chans = input_img.shape
	

	#max ratio of covert to overt image to be compressed
	ratio = getRatio(height, width, chans, max_cap)

	res_img = cv2.resize(input_img, (0,0), input_img, ratio, ratio)
	img_arr = np.asarray(res_img)
	
	height, width, chans = res_img.shape
	
	img_r_arr = img_arr[:,:,0]
	img_g_arr = img_arr[:,:,1]
	img_b_arr = img_arr[:,:,2]

	bin_r_str = ''.join(list(map(binary_value, list(map(int, img_r_arr.flatten())))))
	bin_g_str = ''.join(list(map(binary_value, list(map(int, img_g_arr.flatten())))))
	bin_b_str = ''.join(list(map(binary_value, list(map(int, img_b_arr.flatten())))))
	
	final_str = bin_r_str + bin_g_str + bin_b_str
	
	return final_str,height,width


def lsbImageHide(covertImgPath, overtImgPath, n = 2, resImageName = 'resultant_img'):
	
	try:
		input_img=getImageFromPath(covertImgPath)
	except:
		print(covertImgPath)
		print('lol')
		print("Failed to load the covert image.\nPlease try again. \nMake sure the covert file path is correctly specified.")
		exit(-1)
		
	
	max_cap = ( (input_img.size) * 8 * n) // 8

	print('1')
	img_str, height, width = imgtoString(overtImgPath,max_cap)
	print('2')
	prelen = str(len(img_str)) + ',' + str(height) + ',' + str(width) + ':'

	binaryStr = a2bits(prelen) + img_str

	o_height, o_width, chans = input_img.shape

	img_arr = np.asarray(input_img)
	

	#Convering the overt image to array form, separate channels
	img_r_arr = img_arr[:,:,0] #red channel
	img_g_arr = img_arr[:,:,1] #green channel
	img_b_arr = img_arr[:,:,2] #blue channel
	

	#flattening the image.
	img_r_arr = img_r_arr.flatten()
	bin_r_arr = list(map(binary_value,img_r_arr))
	
	img_g_arr = img_g_arr.flatten()
	bin_g_arr = list(map(binary_value,img_g_arr))
	
	img_b_arr = img_b_arr.flatten()
	bin_b_arr = list(map(binary_value,img_b_arr))

	
	
	bin_str_arr = np.asarray(list(binaryStr)).reshape((-1, n))

	
	#convert to an array
	bin_list=[]
	for elem in bin_str_arr:
		bin_list.append("".join(elem))


	r_count, g_count, b_count = 0, 0, 0
	for i in range (len(bin_list)):
		
		channelNum = i%3  #RGB -> 0, 1, 2
		
		if channelNum == 0:
			bin_r_arr[r_count] = bin_r_arr[r_count][0:8-n] + bin_list[i]
			r_count += 1     
		
		elif channelNum == 1:
			bin_g_arr[g_count] = bin_g_arr[g_count][0:8-n] + bin_list[i]
			g_count += 1
		
		elif channelNum == 2:
			bin_b_arr[b_count] = bin_b_arr[b_count][0:8-n] + bin_list[i]
			b_count += 1
		

	final_img=np.zeros(input_img.shape,np.uint8)

	dec_r_arr=list(map(binaryToDecimal,bin_r_arr))
	dec_r_arr=np.reshape(dec_r_arr,(o_height,o_width)).astype(np.uint8)
	
	dec_g_arr=list(map(binaryToDecimal,bin_g_arr))
	dec_g_arr=np.reshape(dec_g_arr,(o_height,o_width)).astype(np.uint8)
	
	dec_b_arr=list(map(binaryToDecimal,bin_b_arr))
	dec_b_arr=np.reshape(dec_b_arr,(o_height,o_width)).astype(np.uint8)

   
	# Reconstructing image
	final_img[:,:,0]=dec_r_arr
	final_img[:,:,1]=dec_g_arr
	final_img[:,:,2]=dec_b_arr


	#saving the final image
	
	print('IMAGE HIDDEN SUCCESFULLY!!!')

	dirname = os.path.dirname(__file__)
	
	cv2.imwrite('./steganographer/static/ovt_to_cvt/mainHide/'+str(resImageName)+".png", 
				cv2.cvtColor(final_img,cv2.COLOR_BGR2RGB))
	
	return str('./steganographer/static/ovt_to_cvt/mainHide/'+str(resImageName)+".png")