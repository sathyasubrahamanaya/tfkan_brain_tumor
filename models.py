import tensorflow as tf
import tfkan
from tfkan.layers.dense import DenseKAN


model0 = tf.keras.models.Sequential(
    [
        tf.keras.layers.Input(shape=(64,64,3)),
        tf.keras.layers.Conv2D(16,(2,2),activation='relu'),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32,(2,2),activation='relu'),

        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(32,activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(16,activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(4,activation='softmax')

    ]
)


model0KAN= tf.keras.models.Sequential(
    [
       tf.keras.layers.Input(shape=(64,64,3)),
        tf.keras.layers.Conv2D(16,(2,2),activation='relu'),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32,(2,2),activation='relu'),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Flatten(),
        DenseKAN(32),
        tf.keras.layers.Dropout(0.3),
        DenseKAN(16),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(4,activation='softmax')
    ])

model0convKAN= tf.keras.models.Sequential(
    [
       tf.keras.layers.Input(shape=(64,64,3)),
        tfkan.layers.Conv2DKAN(16,kernel_size= (2,2)),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tfkan.layers.Conv2DKAN(32,kernel_size= (2,2)),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Flatten(),
        DenseKAN(32),
        tf.keras.layers.Dropout(0.3),
        DenseKAN(16),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(4,activation='softmax')
    ])