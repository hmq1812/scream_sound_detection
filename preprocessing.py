#from memory_profiler import memory_usage
import os
import pandas as pd
from glob import glob
import numpy as np

import keras.backend as K
import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib import figure
import gc
import pandas as pd
import numpy as np

train_data_path='data/train/'
test_data_path='data/test/'
wav_path = 'data/wav_notscream/'

# Create spectrogram from wav files
def create_spectrogram(filename,name, file_path):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72,0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename  = file_path + name + '.png'
    plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S

# create folder data/wav/train and generate spectrogram images
Data_dir=np.array(glob(wav_path+"train/*"))

for file in Data_dir:
    filename,name = file,file.split('/')[-1].split('.')[0]
    create_spectrogram(filename,name, train_data_path)

gc.collect()

# create folder data/wav/test and generate spectrogram images
Test_dir=np.array(glob(wav_path+"test/*"))


for file in Test_dir:
    filename,name = file,file.split('/')[-1].split('.')[0]
    create_spectrogram(filename,name,test_data_path)

gc.collect()

print("Process done!")