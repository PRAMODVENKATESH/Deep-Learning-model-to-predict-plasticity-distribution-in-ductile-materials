#plt.scatter(x_train, y_train, color = "red")
plt.rcParams["figure.figsize"] = (10,10)
plt.scatter(preds2, trainY, color = "black", label = 'Train dataset')
plt.scatter(preds, testY, color = "green",label = 'Test dataset \n mean of abs difference = 0.5631' )
plt.title("Predicted vs Groundtruth values")
plt.xlabel("TOTAL_REACTION_FORCE")
plt.ylabel("Total_Reaction_force_predicted")
plt.legend(loc = 'lower right');
images_dir = '/content/drive/MyDrive '
#code to save the plot 
plt.savefig(f"{images_dir}/filename.png")
plt.show()
