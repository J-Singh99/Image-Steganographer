#IMPORTS
import argparse
from . import LSB_img_reveal
from . import LSB_text_reveal

def run_CMD(): #WONT WORK, DONT TRY
	parser = argparse.ArgumentParser(description='REVEAL Steganography', formatter_class = argparse.RawTextHelpFormatter)

	parser.add_argument('stego_type',
						metavar = 'stego_type',
						type = str,
						help = 'Enter type of steganography to reveal.',
						choices = ['IMG', 'TXT'])

	parser.add_argument('covertImagePath',
						metavar = 'covImgPath',
						type = str,
						help='Enter path for the image with the hidden data.')

	parser.add_argument('ls_bit',
						metavar = 'ls_bits',
						type = int,
						help = 'Enter the number of LSBs that were modified.')

	parser.add_argument('-resultFileName',
						metavar = 'resultFileName',
						type = str,
						help = 'Enter the file name of resultant file.\nDO THIS ONLY IF ITS AN IMAGE.')

	args = parser.parse_args()



#Once the appropriate type of steganography is chosen, 
#the image and the LSB parameter can be passed to the suitable function

def run_FLASK(covertImagePath, stego_type, resultFileName='0', lsb_bits=2):
	
	if (stego_type=='IMG'): #Recover Image
	    FINAL_DATA = LSB_img_reveal.lsbImgReveal(covertImagePath, lsb_bits, resultFileName)

	elif (stego_type=='TXT'): #Recover Text
	    FINAL_DATA = LSB_text_reveal.lsbTextReveal(covertImagePath,lsb_bits)

	return FINAL_DATA