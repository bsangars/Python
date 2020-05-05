import numpy as np 
import mnist
import matplotlib.pyplot as plt 
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Load the data sets
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

# Normalize the images from pixel values from [0,255]tp
# normalize the vector between [0,1] for easy access
train_images = (train_images/255)
test_images = (test_images/255)
# Flatten the 28*28 image into a 784 dimension vector to pass into neural network.
train_images = train_images.reshape((-1,784))
test_images =test_images.reshape((-1,784))

#print teh shape 


print(train_images.shape)

print(test_images.shape)

#Once we have the data for images now build the model
# 3 layers, 2 layers with 64 neurons and relu function
# 1 layer with 10 neurons and softmax function
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=784))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
#loss function would measure the training model efficinecy, improves them based on optimizer
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    train_images,
    to_categorical(train_labels),
    epochs =5,
    batch_size=32
)

model.evaluate(
    test_images,
    to_categorical(test_labels)
)
predictions =model.predict(test_images[:5])
print(predictions)
#print our models predictions
print(np.argmax(predictions, axis=1))
print(test_labels[:5])

for i in range(0,5):
    first_range =test_images[i]
    first_image =np.array(first_range,dtype='float')
    pixels= first_range.reshape((28,28))
    plt.imshow(pixels)
    plt.show()
