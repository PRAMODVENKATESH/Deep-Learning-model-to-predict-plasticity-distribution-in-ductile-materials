# make predictions on the testing data
print("[INFO] Totalreactionforce...")
preds = new_model.predict(testImagesX)
preds2 = new_model.predict(trainImagesX)
# compute the difference between the *predicted* force and the
# *actual* force, then compute the percentage difference and
# the absolute percentage difference

diff = preds.flatten() - testY
print(diff)
abs_diff = abs(diff)
percentDiff = (diff / testY) * 100
absPercentDiff = np.abs(percentDiff)
#print(absPercentDiff)

# compute the mean and standard deviation of the absolute percentage
# difference
# print("mean of array", np.mean(abs_diff))
mean = np.mean(abs_diff)
max = np.amax(abs_diff)
print('mean', mean)
print('max', max)
