# -*- coding: utf-8 -*-
"""customdogcatmodel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sdyTRLlHBGXnm1zfhCFxnZub0038DIWH
"""

import tensorflow

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,MaxPooling2D,Conv2D,Dropout,BatchNormalization,Flatten,Activation
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt
import glob
import shutil
import random
import os

train_path = 'D/train'
valid_path = 'D/test'

imggen_train=ImageDataGenerator(rescale=1./255,horizontal_flip=.2,zoom_range=.5,rotation_range=0.4)
imggen=ImageDataGenerator(rescale=1./255)
train_data=imggen.flow_from_directory(directory=train_path,target_size=(100,100),class_mode='categorical'
                                      ,batch_size=200)
val_data=imggen.flow_from_directory(directory=valid_path,target_size=(100,100),class_mode='categorical',
                                    batch_size=200)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(100,100, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dropout(.3))
model.add(Dense(128, activation='relu'))
model.add(Dropout(.3))
model.add(Dense(2, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

len(train_data)

model.fit(x=train_data,validation_data=val_data,epochs=20,steps_per_epoch=95,validation_steps=31)

model.save('face.h5')

