# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RthvlQ8S4vf2AF6XLmFd_ZqO-6XDG2Bm
"""

pip install tensorflow

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Dataset: MNIST Handwritten Digits
# Downloaded automatically by Keras

# 1. Load and Preprocess the Data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Reshape images to (num_samples, height, width, channels) - required for CNN input
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# One-hot encode the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 2. Define the CNN Model
model = models.Sequential()

# Convolutional Layer 1
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Convolutional Layer 2
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Flatten the output from the convolutional layers
model.add(layers.Flatten())

# Dense (Fully Connected) Layer 1
model.add(layers.Dense(64, activation='relu'))

# Output Layer (10 classes - digits 0-9)
model.add(layers.Dense(10, activation='softmax'))  # softmax for multi-class classification


# 3. Compile the Model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Cross-entropy loss for multi-class
              metrics=['accuracy'])

# 4. Train the Model
history = model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2) #validation_split adds validation images to the training data.

# 5. Evaluate the Model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)




# 7. Save the Model (Optional)
model.save('mnist_cnn_model.h5')  # Saves the model to a file
print("Model saved to mnist_cnn_model.h5")


import matplotlib.pyplot as plt

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()