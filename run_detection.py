#from memory_profiler import memory_usage
import io
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
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import pickle
from PIL import Image

import config


class Model(object):
    def __init__(self):
        self.model = load_model(config.model_path)
        with open(config.model_label, 'rb') as handle:
            self.labels = pickle.load(handle)
            self.labels = dict((v,k) for k,v in self.labels.items())

    def create_spectrogram(self, clip, sample_rate):
        # Create spectrogram from wav files
        plt.interactive(False)
        fig = plt.figure(figsize=[0.72,0.72])
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))

        #save as PIL image
        buf = io.BytesIO()
        plt.savefig(buf, dpi=400, bbox_inches='tight',pad_inches=0)
        buf.seek(0)
        img = Image.open(buf).convert("RGB")
        img = img.resize((64,64))

        # Convert to np array and adjust dim
        img_np = np.array(img, dtype='float32')

        img_np /= 255.
        img_np = np.expand_dims(img_np, 0)  # Add batch dimension.
        return img_np

    def predict(self, clip, sample_rate):
        img = self.create_spectrogram(clip, sample_rate)
        pred = self.model.predict(img)
        predicted_class_indices=np.argmax(pred,axis=1)
        predictions = [self.labels[k] for k in predicted_class_indices]
        return (predictions[0], predicted_class_indices[0])

# # Load test data
# testdf=pd.read_csv('data/test.csv',dtype=str)
# testdf["slice_file_name"]=testdf["slice_file_name"].apply(append_ext)

# test_data_path='data/test/'


# pred = model.predict_generator(test_generator,steps=STEP_SIZE_TEST,verbose=1)


# # Get the class with highest probability (Scream sound/ not scream sound)
# predicted_class_indices=np.argmax(pred,axis=1)


# predictions = [labels[k] for k in predicted_class_indices]
# print("Prediction values= ",predictions)
# print("Real values=",testdf["class"])


if __name__ == "__main__":
    m = Model()
    clip, sample_rate = librosa.load("data/wav/test/scream401.wav", sr=None)
    print(m.predict(clip, sample_rate))
    







