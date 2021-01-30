# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1plZ6ySNGaddqw8_-HUTRkUc_k2Bd9CqO
"""

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
model1=load_model('/content/drive/MyDrive/H5 files/face.h5')
path='/content/drive/MyDrive/pic/n4.jpg'
import matplotlib.pyplot as plt
img=image.load_img(path=path,target_size=(100,100))
plt.imshow(img)
import numpy as np
img= image.img_to_array(img)
img_batch=np.expand_dims(img,0)
label=['Dissapointed','Happy']
predict=model1.predict(img_batch)
print(label[predict.argmax()])



