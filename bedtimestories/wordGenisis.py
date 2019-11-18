import numpy as np
import tensorflow as tf
from /gtext import unique_characters , charDict
mod = tf.keras.models.load_model('/my_model.h5')
# denormalize data and translate to characters


def num_decoder(nums):
  newNums = []
  nums = [int(n * 100) for n in nums]
  nums = [unique_characters[num] for num in nums]
  return nums


def genStory(mod, string, length):
  #convert string to number value to be processed
  theBeginning = [charDict[s] for s in string]
  np.expand_dims(theBeginning,0)
  theStory = []
  mod.reset_states()
  #looping though text , and generating new text
  for i in range(lengthStory):
    newChar = mod.predict(theBeginning)
    #take a dim away from array to covert to letter ,and add to list
    #take the largest output from sortmax, and appent it on theBeginnning
    pred = np.argMax(newChar)
    newChar = theStory.append(unique_characters[pred])
    #reuse this variable to feed make into model to get new character
    theBeginning = tf.expand_dims([pred,0])
  A_story = "{} {}". format(string,theStory)
  return  A_story
