import cv2
import numpy as np
import csv
import os
import imutils
from shutil import copyfile

src_folder = "temp_folder"
csv_name = src_folder + "/labels.csv"
dst_folder = "New_Augmented"
if not os.path.exists(dst_folder):
	os.makedirs(dst_folder)

def create_new_name(oldname, extension):
	file_out = oldname.split(".")
	new_name = file_out[0] + extension + '.' + file_out[1]
	return new_name

def histo_aug(img,imgname):
	extension  = "_histo"
	img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

	img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

	name = create_new_name(imgname, extension)

	img_loc = dst_folder + "/" + name
	cv2.imwrite(img_loc , img_output)
	#return name

def brightness(img, imgname, key):
	bright_augnames = []

	img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
	img = np.array(img, dtype = np.float64)

	random_bright = .5 + key
	img[:,:,2] = img[:,:,2] * random_bright
	img[:,:,2][img[:,:,2]>255]  = 255
	img = np.array(img, dtype = np.uint8)
	img_output = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
	extension = '_bright' + str(key+1)
	name = create_new_name(imgname, extension)
	img_loc = dst_folder + "/" + name
	cv2.imwrite(img_loc , img_output)

def blur(img,imgname, key):
	blur_type = ''
	extension  = ''

	if key == 'a':
		extension = '_aveBlur'
		blur_type = cv2.blur(img,(5,5))
	elif key == 'g':
		extension = '_gBlur'
		blur_type = cv2.GaussianBlur(img,(5,5),0)
	elif key == 'm':
		extension = '_mBlur'
		blur_type = cv2.medianBlur(img,5)
	else:
		extension = '_bFilter'
		blur_type = cv2.bilateralFilter(img,9,75,75)
	
	name = create_new_name(imgname, extension)	
	img_loc = dst_folder + "/" + name
	cv2.imwrite(img_loc , blur_type)
	#return name
def clahe(img,imgname,key):
	extension  ="_clahe" + str(key)

	img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8*key,8*key))
	img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
	img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

	name = create_new_name(imgname, extension)
	img_loc = dst_folder + "/" + name
	cv2.imwrite(img_loc , img_output)
	#return name

def rotate_img(img,imgname, deg):
	extension = "_rot" + str(deg)
	rotated = imutils.rotate_bound(img, deg)

	name = create_new_name(imgname, extension)
	img_loc = dst_folder + "/" + name
	cv2.imwrite(img_loc , rotated)

def flip_img(img,imgname,key):
	extension = "_flip" +  key.upper()
	rimg = ''
	if key == 'v':
		rimg=cv2.flip(img,1)
		#return "FlipV" + "_" + imgname
	else:
		rimg=cv2.flip(img,0)	
		#return "FlipH" + "_" + imgname
	name = create_new_name(imgname, extension)
	img_loc = dst_folder + "/" + name
	cv2.imwrite(img_loc , rimg)


for filename in os.listdir(src_folder):
	print "> Flip and Rotate: " + filename

	copyfile(src_folder+"/"+filename,dst_folder+"/"+filename)

	img = cv2.imread(src_folder+"/"+filename)

	#FLIP and ROTATE images first
	flip_img(img, filename,'v')
	flip_img(img, filename,'h')
	rotate_img(img, filename,90)
	rotate_img(img, filename,180)
	rotate_img(img, filename,270)

#Apply changes to the rotated and flipped images	
print "==> Additional Augmentations..."
for filename in os.listdir(dst_folder):
	

	img = cv2.imread(dst_folder+"/"+filename)

	histo_aug(img,filename)
	blur(img, filename, 'a')
	blur(img, filename, 'g')
	blur(img, filename, 'm')
	blur(img, filename, 'b')
	clahe(img, filename, 1)
	clahe(img, filename, 2)
	brightness(img, filename, 0.05)
	brightness(img, filename, 0.1)
	brightness(img, filename, 0.15)
	brightness(img, filename, 0.2)

