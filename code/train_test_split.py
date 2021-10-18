#If the code is executed as a .py file, use the following command line
from Initialize_targetvariable import Total_reaction_force_data
from read_imagedataset import Plasticity_distribution
#construct the path to the input .txt file that contains information
# on each TRF value in the dataset and then load the dataset
print("[INFO] Total_reaction_force_data...")
inputPath1 = ('/content/drive/MyDrive/TRF_2531.txt')
df = Total_reaction_force_data(inputPath1)

# load the house images and then scale the pixel intensities to the
# range [0, 1]
print("[INFO] Plasticity_distribution...")
inputPath2 =('/content/drive/MyDrive/Grey and resized')
images = Plasticity_distribution(df,inputPath2 )
print(images.shape)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
split = train_test_split(df, images, test_size=0.25, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split
