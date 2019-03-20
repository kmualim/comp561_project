#class DownloadDataset(GeneDataset): 
#	def __init__(self):
#		super(DownloadDataset, self).__init__()
import os
import urllib.request as urllib
import glob
import pandas as pd
import numpy as np
import zipfile

def load_data(): 
	data_dir = "datasets"
	origin = "ebi"
	source = "https://www.ebi.ac.uk/arrayexpress/files/E-MTAB-3732"
	filename = "E-MTAB-3732.processed.1.zip"

	if not os.path.exists(data_dir): 
		os.makedirs(data_dir)

	if not os.path.isfile(data_dir + "/%s" %(filename)):
		print("Downloading %s data..." %(origin))
		urllib.urlretrieve("%s/%s" %(source, filename), data_dir + "/%s" %(filename))

		# Extract data 
		file = zipfile.ZipFile(data_dir + "/%s" %(filename))
		file.extractall(data_dir)
		file.close()

	# Preparing data for processing 
	# figure out structure of data set
	print("Preparing %s data for preprocessing" %(origin))


def load_labels(): 
	data_dir = "datasets"
	origin = "ebi"
	source = "https://www.ebi.ac.uk/arrayexpress/files/E-MTAB-3732"
	filename = "E-MTAB-3732.sdrf.txt"

		# Downloading data 
	if not os.path.exists(data_dir): 
		os.makedirs(data_dir)
	if not os.path.isfile(data_dir + "/%s" %(filename)):
		print("Downloading %s data..." %(origin))
		urllib.urlretrieve("%s/%s" %(source, filename), data_dir + "/%s" %(filename))

df = load_data()



		
