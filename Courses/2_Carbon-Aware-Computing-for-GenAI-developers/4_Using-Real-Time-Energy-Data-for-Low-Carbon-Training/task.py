
# import libraries
import numpy as np
from sklearn.datasets import make_blobs
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create dataset
classes = 4
m = 100
centers = [[-5, 2], [-2, -2], [1, 2], [5, -2]]
std = 1.0
X_train, y_train = make_blobs(
    n_samples=m, 
    centers=centers, 
    cluster_std=std,
    random_state=30)

# Create the model
model = Sequential(
    [
        Dense(2, activation = 'relu',   name = "L1"),
        Dense(4, activation = 'linear', name = "L2")
    ]
)

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True),
    optimizer=tf.keras.optimizers.Adam(0.01),
)

# Train
model.fit(
    X_train,y_train,
    epochs=200
)
