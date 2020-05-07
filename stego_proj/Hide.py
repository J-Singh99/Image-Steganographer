#IMPORTS
import argparse
from . import LSB_img_hide
from . import LSB_text_hide
from . import PSNR


def run_CMD(): #WONT WORK, DONT TRY
	parser = argparse.ArgumentParser(description='HIDE Steganography', formatter_class = argparse.RawTextHelpFormatter)

	parser.add_argument('stego_type',
						metavar = 'stego_type',
						type = str,
						help = 'Enter "image"/"text" for type of steganography.',
						choices = ['IMG', 'TXT'])

	parser.add_argument('overtImagePath',
						metavar = 'overtImagePath',
						type = str,
						help = 'Enter path for overt image.')

	parser.add_argument('dataToHide',
						metavar = 'dataToHide',
						type = str,
						help = 'If stego_type is "image", enter path for hidden image. \nIf stego_type is "text", enter text.')

	parser.add_argument('lsb_bits',
						metavar = 'ls_bits',
						type = int,
						help = 'Enter number of LSBs to modify.', 
						choices = [1, 2, 4])

	parser.add_argument('-resultFileName',
						metavar = 'resultFileName',
						type = str,
						help = 'Enter the file name of resultant file.')

	parser.add_argument('--p','--ps', 
						action = 'store_true', 
						help = 'Calculate PSNR (Peak Signal to Noise Ratio).')


	args = parser.parse_args()



	#Once the appropriate type of steganography is chosen, 
	#the images, text, and the LSB parameter can be passed to the suitable function

	if(args.stego_type == 'IMG'): #Hiding Image
	    LSB_img_hide.lsbImageHide(args.overtImagePath, args.dataToHide, args.lsb_bits, args.resultFileName)
	    
	elif(args.stego_type == 'TXT'): #Hiding Text
	    LSB_text_hide.lsbTextHide(args.overtImagePath,args.dataToHide,args.lsb_bits)



	#Check PSNR Value
	if (args.p==True):
	    result_path = "./" + args.resultFileName + ".png"
	    psnr = PSNR.psnr(args.overtImagePath,result_path)
	    print("Peak  Signal to Noise Ratio: ", psnr)


def run_FLASK(overtImagePath, stego_type, dataToHide, resultFileName, lsb_bits=2, p=False):

	if(stego_type == 'IMG'): #Hiding Image
	   FINAL_IMAGE = LSB_img_hide.lsbImageHide(overtImagePath, dataToHide, lsb_bits, resultFileName)
	    
	elif(stego_type == 'TXT'): #Hiding Text
	    FINAL_IMAGE = LSB_text_hide.lsbTextHide(overtImagePath,dataToHide,lsb_bits)

	#Check PSNR Value
	if (p==True):
	    result_path = "./" + resultFileName + ".png"
	    psnr = PSNR.psnr(overtImagePath,result_path)
	    print("Peak  Signal to Noise Ratio: ", psnr)

	return FINAL_IMAGE