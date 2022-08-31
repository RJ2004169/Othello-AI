import os
import tensorflow as tf
import keras
import matplotlib.pyplot as plt

print("TensorFlow version: {}".format(tf.__version__))
print("Eager execution: {}".format(tf.executing_eagerly()))

train_dataset_url = "C:\Game Dev Practicals\MAT-501\pyOthello-master\pyOthello-master\dataset\archive\othello_dataset.csv"

train_dataset_fp = tf.keras.utils.get_file(fname="othello_dataset.csv",
                                           origin="file:///Game Dev Practicals/MAT-501/pyOthello-master/pyOthello-master/dataset/archive/othello_dataset.csv")

print("Local copy of the dataset file: {}".format(train_dataset_fp))

model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(2,)),  # input shape required
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(1)
])