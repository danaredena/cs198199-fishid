import glob, os

def rename(dir, pattern, titlePattern):
	x = 1
	pad = len(str(x))
	# for z in (6-pad):
		
	for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		os.rename(pathAndFilename, os.path.join(dir, titlePattern % str(x) + ext))
		x+=1

# rename(r'/Users/dknredena/Dropbox/4th_1stsem/CS198/cs198199-fishid/train/YFT', r'*.jpg', r'yft-%s')
rename(r'/Users/dknredena/Dropbox/4th_1stsem/CS198/cs198199-fishid/google/SHARK', r'*.jpg', r'shark-google-%s')