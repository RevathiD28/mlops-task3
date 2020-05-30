import tensorflow as tf
import tensorflow.keras as keras

mnist = keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt
for i in range(0, 15):
    plt.imshow(x_train[i],cmap=plt.cm.binary)
    plt.show()
    print(y_train[i])

x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

from keras.layers import Activation, Dense
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(512, activation=tf.nn.relu))
model.add(keras.layers.Dense(256, activation=tf.nn.relu))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(64, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Tweak the model to increase the epochs
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)

predictions = model.predict(x_test)
print(predictions)

import numpy as np
for predict in range(0,10):
    print(np.argmax(predictions[predict]))
    plt.imshow(x_test[predict],cmap=plt.cm.binary)
    plt.show()

import os

if accuracy <= 0.9:
    os.system("curl --user "admin:admin" http://10.0.2.15:8080/view/mlops-task3/job/retrain_model/build?token=retrain")
else:
    print("The model is successfully trained for the desired accuracy. You will soon receive a mail.)
    os.system("curl --user "admin:admin" http://10.0.2.15:8080/view/mlops-task3/job/notify_model/build?token=notification")
