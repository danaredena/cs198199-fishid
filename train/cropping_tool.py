import cv2
import csv
import os

#Constants
specie =  "LAG"

folder = specie# + "-sample"
csv_name = specie + "_sample.csv"
new_folder = folder + "_cropped"

if not os.path.exists(new_folder):
	os.makedirs(new_folder)
with open(csv_name, 'rb') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in csv_reader:
		#print "here!==============================="
		#print row[5]
		
		annotations = row[5].strip("}").split(",")

		if len(annotations) == 1:
			continue
		img_name = folder + "/" + str(row[0])
		x = int(annotations[1].split(":")[1])
		y = int(annotations[2].split(":")[1])
		w = int(annotations[3].split(":")[1])
		h = int(annotations[4].split(":")[1])
		#print x,y,w,h
		#print annotations
		img = cv2.imread(img_name)
		crop_img = img[y: y + h, x: x + w] # Crop from x, y, w, h -> 100, 200, 300, 400
		# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
		cv2.imwrite(new_folder + "/" + str(row[0]), crop_img)
