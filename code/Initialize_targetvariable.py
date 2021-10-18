# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from sklearn.model_selection import train_test_split
from natsort import natsorted
import pickle
from PIL import Image
import pandas as pd
import numpy as np
from numpy import asarray
import argparse
import locale
import glob
import cv2
import os

#The ascii file containing the details of total reaction force are read using pandas dataframe.
def Total_reaction_force_data(inputPath1):
# initialize the list of column names in the CSV file and then
# load it using Pandas
    cols = ["Totalreactionforce"]
    df = pd.read_csv(inputPath1, sep=",", header=None, names=cols)
    print(df.shape)
    #print(df.head(3))
    print(df.describe)
	  #return the data frame
    return df
