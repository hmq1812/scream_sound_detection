#from memory_profiler import memory_usage
import os
import pandas as pd
from glob import glob
import numpy as np
# from tensorflow.keras import layers
# from tensorflow.keras import models
# from tensorflow.keras.layers.advanced_activations import LeakyReLU
# from tensorflow.keras.optimizers import Adam
import tensorflow.keras.backend as K
import librosa
import librosa.display
import pylab
import matplotlib.pyplot as plt
from matplotlib import figure
import gc
from path import Path
from tensorflow.keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import regularizers, optimizers
import pandas as pd
import numpy as np
from keras_preprocessing.image import ImageDataGenerator
import pickle

# change name extension
def append_ext(fn):
    return fn.replace(".wav",".png")

# Load test data
testdf=pd.read_csv('data/test.csv',dtype=str)
testdf["slice_file_name"]=testdf["slice_file_name"].apply(append_ext)

test_data_path='data/test/'



# Intialize test data
test_datagen=ImageDataGenerator(rescale=1./255.)
test_generator=test_datagen.flow_from_dataframe(
    dataframe=testdf,
    directory=test_data_path,
    x_col="slice_file_name",
    y_col=None,
    batch_size=32,
    seed=42,
    shuffle=False,
    class_mode=None,
    target_size=(64,64))
'''
test_generator_vgg=test_datagen.flow_from_dataframe(
    dataframe=testdf,
    directory=test_data_path,
    x_col="slice_file_name",
    y_col=None,
    batch_size=32,
    seed=42,
    shuffle=False,
    class_mode=None,
    target_size=(224,224))
'''
# Calculate step in testing epock
STEP_SIZE_TEST=test_generator.n//test_generator.batch_size

# start prediction
test_generator.reset()

# Load model
model = load_model('model.h5')
pred = model.predict_generator(test_generator,steps=STEP_SIZE_TEST,verbose=1)


# Get the class with highest probability (Scream sound/ not scream sound)
predicted_class_indices=np.argmax(pred,axis=1)
# Load class name from file
with open('model_indices.pickle', 'rb') as handle:
    labels = pickle.load(handle)

# Display prediction result
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]
print("Prediction values= ",predictions)
print("Real values=",testdf["class"])


# test_generator_vgg.reset()

# model = load_model('modelvgg.h5')
# pred = model.predict_generator(test_generator_vgg,steps=STEP_SIZE_TEST,verbose=1)

# predicted_class_indices=np.argmax(pred,axis=1)
# with open('model_indices.pickle', 'rb') as handle:
#     labels = pickle.load(handle)

# labels = dict((v,k) for k,v in labels.items())
# predictions = [labels[k] for k in predicted_class_indices]
# print("Prediction values= ",predictions[0:10])
# print("Real values=",testdf.head(10))




