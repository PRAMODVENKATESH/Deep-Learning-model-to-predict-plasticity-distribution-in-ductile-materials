#using a DenseNet121 for feature extraction
#Backbbone or Feature Extractor

model = Sequential()
model = tf.keras.applications.DenseNet121(input_shape=[128,128,1], input_tensor=None, weights=None, classes=1, include_top=False)
#Next, let's add some layers to create our Regresor
#First flatten the output from DenseNet121

y = model.output
y = tf.keras.layers.Flatten()(y)

#Now you add one or more hiden layers (and select the number of nodes for each)

y = tf.keras.layers.Dense(50, activation='relu', name='hidden_layer1')(y)

y = tf.keras.layers.Dense(8, activation='relu', name='hidden_layer2')(y)

#Add the output node (or nodes depending on how many outputs correspond to each input) and use a linear activation function
y = tf.keras.layers.Dense(1, activation='linear', name='output_layer')(y)

# Now you put both parts (input and output) together in a single model called new_model
new_model = tf.keras.Model(inputs=model.input, outputs=y) 


# Now compile the new_model specifying the remaining hyperparameters e.g. optimizer, learning rate, loss
opt = tf.keras.optimizers.Adam(learning_rate=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
new_model.compile(optimizer=opt, loss="mse")

#Visualize the final architecture of your model

#print(new_model.summary())

#simple early stopping
from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1 , patience = 30)
# train the model
print("[INFO] training model...")
history = new_model.fit(x=trainImagesX, y=trainY, 
    validation_data=(testImagesX, testY),
    epochs=200, batch_size=55, callbacks=[es])
