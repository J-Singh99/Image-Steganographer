import base64
import itertools
from functools import reduce
from typing import IO, Iterator, List, Tuple, Union
import cv2



ENCODINGS = {
				"UTF-8": 8, 
				"UTF-32LE": 32
			}


def a2bits(chars: str) -> str:
	return bin(reduce(lambda x, y: (x << 8) + y, (ord(c) for c in chars), 1))[3:]


def binary_value(val): #Return the binary value of an integer as a byte
		
		binaryVal = bin(val)[2:]
		
		if len(binaryVal) > 8:
			raise Exception('Binary value larger than the expected size!!!!')
		
		while len(binaryVal) < 8:
			binaryVal = '0' + binaryVal
		
		return binaryVal

	
def binaryToDecimal(n):
	if n == '':
		n = '0'
	return str(int(n,2))


def getImageFromPath(path):
	img = cv2.imread(path)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	return img



#    *********** DEV TOOLS ***********

def show_pic(img):
	fig = plt.figure(figsize=(10,10))
	ax=fig.add_subplot(111)
	ax.imshow(img,cmap='gray') 


def bs(s: int) -> str:
	return str(s) if s <= 1 else bs(s >> 1) + str(s & 1)


def a2bits_list(chars: str, encoding: str = "UTF-8") -> List[str]:
	return [bin(ord(x))[2:].rjust(ENCODINGS[encoding], "0") for x in chars]