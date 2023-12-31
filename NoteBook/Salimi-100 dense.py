# -*- coding: utf-8 -*-
"""Copy of final-all-100-optimize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D6Z82M3nTN3F41biku-1tNIcwwDsOkYS
"""

from google.colab import drive
drive.mount('/content/drive')

!ls 'drive/My Drive'
# Define the path

from sklearn.preprocessing import  normalize
from keras.layers import Input, Dense, BatchNormalization, Dropout, GaussianNoise, GaussianDropout
from keras.models import Model
import keras
from sklearn.metrics import mean_squared_error as mse
from keras.utils import np_utils
from keras.callbacks import CSVLogger, History
import pandas as pd
from random import random
from keras.optimizers import Adam
from keras.initializers import RandomNormal
from keras.models import Model
from keras.models import Input
from keras.layers import Conv2D
from keras.layers import Conv2DTranspose
from keras.layers import LeakyReLU
from keras.layers import Activation
from keras.layers import Concatenate
from matplotlib import pyplot
from keras.layers import Input, Dense, BatchNormalization, Dropout, GaussianNoise, GaussianDropout
from keras.models import Model
import keras.backend as backend
import numpy as np
from sklearn.preprocessing import LabelEncoder, normalize
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from keras.utils import np_utils
from keras.callbacks import CSVLogger, History
import pandas as pd
np.random.seed(seed=2019)
#Define the libraries and prerequisite.

import pandas as pd
pd.__version__ #must be 0.23.0

! pip install pandas==0.25.0

pd.__version__

path="drive/My Drive/data/"+""
df_m_rna_address=path+"all.xlsx"
df=pd.read_excel(df_m_rna_address,header=0)
df.drop(["GeneSymbol"],axis=1,inplace=True)
df_m_rna = pd.DataFrame.as_matrix(df).transpose()
m_rna = normalize(X=df_m_rna, axis=0, norm="max")
m_rna_indices = np.arange(m_rna.shape[0])
np.random.shuffle(m_rna_indices)
m_rna[m_rna_indices]
mrna_train=m_rna[:int(0.85*m_rna.shape[0])]
mrna_test=m_rna[int(0.85*m_rna.shape[0]):]
#خواندن داده ها 

#مشاهده شمای دیتا

df_m_rna = pd.DataFrame.as_matrix(df).transpose() #*

df_m_rna = pd.DataFrame.values().transpose()

df_m_rna=np.matrix (df.values ()).transpose()

(df.head())
df.columns

batch_size=32
epochs=nb_epochs=10 # برای ایپوک های بیشتر 
inputs = Input(shape=(m_rna.shape[1],), name="inputs")
inputs_noise = GaussianNoise(stddev=0.0)(inputs)
inputs_noise = GaussianDropout(rate=0.0 ** 2 / (1 + 0.0 ** 2))(inputs_noise)
inputs_0 = BatchNormalization(name="inputs_0")(inputs_noise)
inputs_1 = Dense(100, activation="linear", name="inputs_1")(inputs_0) #softmax to linear


#
inputs_00 = BatchNormalization(name="inputs_00")(inputs_1)
inputs_11 = Dense(100, activation="tanh", name="inputs_11")(inputs_00)
#

inputs_2 = BatchNormalization(name="inputs_2")(inputs_1)
encoded = Dense(units=12, activation='softmax', name='encoded')(inputs_2) # relu to softmax تغییر فانکشن و تست سیگموئید
decoded_tcga = Dense(units=m_rna.shape[1], activation='softmax', name="m_rna")(inputs_2) # linear to softmax

scae = Model(inputs=inputs, outputs=decoded_tcga)


scae.compile(optimizer='RMSprop',loss="mse")

result_folder = path

file_name = "best-scae.log"

csv_logger = CSVLogger(result_folder + file_name)
history = History()

scae.fit(mrna_train, mrna_train, batch_size=batch_size, epochs=nb_epochs,callbacks=[csv_logger, history],
          validation_data=(mrna_test, mrna_test), verbose=1)

print(history.history.keys())
print("fitting has just been finished")
# save the model and encoded-layer output

scae.save(filepath=result_folder + "scae.h5")

import tensorflow
tensorflow.__version__

! pip install tensorflow==1.10.0

model_a=keras.models.load_model(result_folder + "scae.h5")
model_a.compile(optimizer='RMSprop',loss="mse")  #nadam to RMSprop
#ذخیره مدل

# وی لاس خیلی زیاد شود !!!





inputs = Input(shape=(m_rna.shape[1],), name="inputs")
inputs_noise = GaussianNoise(stddev=0.0)(inputs)
inputs_noise = GaussianDropout(rate=0.0 ** 2 / (1 + 0.0 ** 2))(inputs_noise)
inputs_0 = BatchNormalization(name="inputs_0")(inputs_noise)
inputs_1 = Dense(100, activation="softmax", name="inputs_1")(inputs_0)# relu to softmax
model_b=Model(inputs=inputs,outputs=inputs_1)#Changed by me output to outputs
#شبکه تا لایه انکود

model_a.summary() # نمایش شبکه

for i in range(5):
  model_b.layers[i].set_weights(model_a.layers[i].get_weights())
# وزن یالها را به شبکه دوم منتقل میکند

model_b.compile(optimizer='nadam',loss="mse")#وزن دهی به شبکه  nadam to RMSprop

mrna_coded=model_b.predict(mrna_train) #پیش بینی

mrna_coded.shape

np.savetxt(X=mrna_coded, fname=result_folder+"all-100"+".csv", delimiter=",", fmt='%1.3f')

mrna_coded=model_b.predict(m_rna)

import numpy
a = numpy.append(np.reshape(np.array(df.columns),(210,1)),mrna_coded,axis=1)#

np.reshape(np.array(df.columns),(210,1)).shape #

a

fm=['%s ']+['%1.3f']*100# 2000 to 100 تعداد فیچرهای لایه دنس

np.savetxt(X=a, fname=result_folder+"all_coded_name_1400"+".csv", delimiter=",", fmt=fm)

keras.utils.plot_model(
    model, to_file='model.png', show_shapes=False, show_layer_names=True,
    rankdir='TB', expand_nested=False, dpi=96
)

