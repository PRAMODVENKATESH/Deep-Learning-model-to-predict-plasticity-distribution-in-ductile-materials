import matplotlib.pyplot as plt
from google.colab import files
plt.rcParams["figure.figsize"] = (20,10)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('Loss(MSE)')
plt.ylim(0, 15)
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
images_dir = '/content/drive/MyDrive'
#to save the plots to required files
plt.savefig(f"{images_dir}/filename nodes.png")
plt.show()
