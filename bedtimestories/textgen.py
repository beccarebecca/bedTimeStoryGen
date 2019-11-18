import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Flatten 
from keras.optimizers import RMSprop
from keras.models import load_model
from keras.callbacks import EarlyStopping
from keras.losses import sparse_categorical_crossentropy
import os 
import re
from sklearn.model_selection import train_test_split

pathText = tf.keras.utils.get_file('fairy_tales.text', 'https://www.gutenberg.org/files/52521/52521-0.txt')

text = open(pathText, 'rb').read().decode(encoding='utf-8')
text.lower()
#[text.append(ch) for ch in ptext]
text[1:]
#text = re.sub(r'[^\x00-\x7f]' ,r", text)

unique_characters = sorted(set(text))
#print(unique_characters)

charDict = {}
for i in range(len(unique_characters)):
  charDict[unique_characters[i]] = i


# normalize data to be between 0 and 1
#preDataset = []

preDataset = np.array([charDict[ch]/100 for ch in text ])
#finding the inputs and targets to train dataset

#subtracting 109 from training set to make it even to feed in to network

text_X = preDataset[109:-1]
text_Y = preDataset[110:]

# divided training data by 200 for batch preparation
oneByOne = len(text_X[0])/200
batchSize = 200

text_X = np.reshape(text_X,(-1,oneByone,1))
text_Y = np.reshape(text_Y, (-1, oneByone,1))


print(text_X.shape)


# denormalize data and translate to characters

#split data to training and test data
xtrain ,xtest, ytrain ,ytest = train_test_split(text_X,text_Y)

print(xtrain.shape)
print(xtest.shape)

#model building

input_train = xtrain.shape


 def nn():
     model = Sequential()
     model.add(LSTM(1028, return_sequences=True, input_shape =(None, 1)))
     model.add(Dense(len(unique_characters), activation='softmax'))
     model.compile(loss = 'sparse_categorical_crossentropy', optimizer='adam')
     model = model.fit(x = xtrain, y = ytrain ,epochs = 35, batch_size = batchSize , validation_data = [xtest,ytest], callbacks=[EarlyStopping(monitor='val_loss', patience=2)])
     return model


nn()
model.save("mymodel.h5")
