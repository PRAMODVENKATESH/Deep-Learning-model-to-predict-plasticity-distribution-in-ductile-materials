from PIL import Image
from natsort import natsorted
import pandas as pd
import numpy as np
from numpy import asarray
import argparse
import locale
import glob
import cv2
import os
def Plasticity_distribution(df,inputPath2):
# initialize our images array (i.e., the analysis files themselves)
    #outputImage = np.zeros((500, 500, 1), dtype="uint8")
    images = []
    #for filename in natsorted(glob.glob('G:\Plasticdeformation-dataset\Plasticitydistribution Dataset\*.png')):
    filelist = natsorted(glob.glob('/content/drive/MyDrive/Grey and resized/*.png'))
    #image_array = np.array([np.array(Image.open(fname)) for fname in filelist])
    for fname in filelist:
        img = Image.open(fname)
        #imgGray = img.convert('L')
        outputImage = np.array(img)
        images.append(outputImage)
        print(fname)
        #img= Image.open(filename)
        #images.append(img)
    #return our set of images
    return np.array(images)
