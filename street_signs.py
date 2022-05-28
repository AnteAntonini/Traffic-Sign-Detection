from gc import callbacks
import os
import glob
import shutil
from sklearn import metrics
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

from utils import split_data, order_test_set, create_generators

from models import streetsigns_model
import tensorflow as tf

if __name__ == "__main__":

    if False:
        data_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Train"
        train_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\train"
        val_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\val"
        split_data(data_path, train_path = train_path, val_path = val_path)
    
    if False:
        images_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Test"
        csv_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Test.csv"
        order_test_set(images_path, csv_path)

    train_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\train"
    val_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\val"    
    test_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Test"
    batch_size = 32
    epochs = 10
    lr=0.0001

    train_generator, val_generator, test_generator  = create_generators(batch_size,train_path, val_path, test_path)
    num_classes = train_generator.num_classes

    TRAIN=False
    TEST=True

    if TRAIN:
        save_model_path = './Models'
        checkpoint_saver = ModelCheckpoint(
            save_model_path,
            monitor="val_accuracy",
            mode='max',
            save_best_only=True,
            save_freq='epoch',
            verbose=1
        )

        early_stop = EarlyStopping(monitor="val_accuracy", patience=10)

        model = streetsigns_model(num_classes)

        optimizer = tf.keras.optimizers.Adam(learning_rate=lr, amsgrad=True)

        model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

        model.fit(train_generator,epochs = epochs, batch_size = batch_size, validation_data = val_generator, callbacks = [checkpoint_saver, early_stop])

    if TEST:
        model = tf.keras.models.load_model('./Models')
        model.summary()

        print("Evaluating validation set:")
        model.evaluate(val_generator)

        print("Evaluating test set : ")
        model.evaluate(test_generator)

