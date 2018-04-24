import cv2
import csv
import os
import random
csv_name = 'test_results_80k.csv'
from shutil import copyfile
#default_lib = {'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}
conf_matrix = {'alb':{'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}, 'bet':{'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}, 'dol':{'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}, 'lag':{'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}, 'shark':{'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}, 'yft':{'alb':0, 'bet':0, 'dol':0, 'lag':0, 'shark':0, 'yft':0}}

with open(csv_name, 'rb') as csvfile_main:
	csv_reader = csv.reader(csvfile_main, delimiter=',')
	for row in csv_reader:
		
		if 'alb' in row[0]:
			if "Thunnus alalunga" in row[6]:
				conf_matrix['alb']['alb']+=1
			elif "Thunnus obesus" in row[6]:
				conf_matrix['alb']['bet']+=1
			elif "Species=Coryphaena hippurus" in row[6]:
				conf_matrix['alb']['dol']+=1
			elif "Species=Lampris guttatus" in row[6]:
				conf_matrix['alb']['lag']+=1
			elif "Species=Shark" in row[6]:
				conf_matrix['alb']['shark']+=1
			elif "Species=Thunnus albacares" in row[6]:
				conf_matrix['alb']['yft']+=1
		elif 'bet' in row[0]:
			if "Thunnus alalunga" in row[6]:
				conf_matrix['bet']['alb']+=1
			elif "Thunnus obesus" in row[6]:
				conf_matrix['bet']['bet']+=1
			elif "Species=Coryphaena hippurus" in row[6]:
				conf_matrix['bet']['dol']+=1
			elif "Species=Lampris guttatus" in row[6]:
				conf_matrix['bet']['lag']+=1
			elif "Species=Shark" in row[6]:
				conf_matrix['bet']['shark']+=1
			elif "Species=Thunnus albacares" in row[6]:
				conf_matrix['bet']['yft']+=1
		elif 'dol' in row[0]:
			if "Thunnus alalunga" in row[6]:
				conf_matrix['dol']['alb']+=1
			elif "Thunnus obesus" in row[6]:
				conf_matrix['dol']['bet']+=1
			elif "Species=Coryphaena hippurus" in row[6]:
				conf_matrix['dol']['dol']+=1
			elif "Species=Lampris guttatus" in row[6]:
				conf_matrix['dol']['lag']+=1
			elif "Species=Shark" in row[6]:
				conf_matrix['dol']['shark']+=1
			elif "Species=Thunnus albacares" in row[6]:
				conf_matrix['dol']['yft']+=1
		elif 'lag' in row[0]:
			if "Thunnus alalunga" in row[6]:
				conf_matrix['lag']['alb']+=1
			elif "Thunnus obesus" in row[6]:
				conf_matrix['lag']['bet']+=1
			elif "Species=Coryphaena hippurus" in row[6]:
				conf_matrix['lag']['dol']+=1
			elif "Species=Lampris guttatus" in row[6]:
				conf_matrix['lag']['lag']+=1
			elif "Species=Shark" in row[6]:
				conf_matrix['lag']['shark']+=1
			elif "Species=Thunnus albacares" in row[6]:
				conf_matrix['lag']['yft']+=1
		elif 'shark' in row[0]:
			if "Thunnus alalunga" in row[6]:
				conf_matrix['shark']['alb']+=1
			elif "Thunnus obesus" in row[6]:
				conf_matrix['shark']['bet']+=1
			elif "Species=Coryphaena hippurus" in row[6]:
				conf_matrix['shark']['dol']+=1
			elif "Species=Lampris guttatus" in row[6]:
				conf_matrix['shark']['lag']+=1
			elif "Species=Shark" in row[6]:
				conf_matrix['shark']['shark']+=1
			elif "Species=Thunnus albacares" in row[6]:
				conf_matrix['shark']['yft']+=1
		elif 'yft' in row[0]:
			if "Thunnus alalunga" in row[6]:
				conf_matrix['yft']['alb']+=1
			elif "Thunnus obesus" in row[6]:
				conf_matrix['yft']['bet']+=1
			elif "Species=Coryphaena hippurus" in row[6]:
				conf_matrix['yft']['dol']+=1
			elif "Species=Lampris guttatus" in row[6]:
				conf_matrix['yft']['lag']+=1
			elif "Species=Shark" in row[6]:
				conf_matrix['yft']['shark']+=1
			elif "Species=Thunnus albacares" in row[6]:
				conf_matrix['yft']['yft']+=1
for specie in conf_matrix:
	print "=>",specie
	for classifications in conf_matrix[specie]:
		print "===>",classifications,"=",conf_matrix[specie][classifications]