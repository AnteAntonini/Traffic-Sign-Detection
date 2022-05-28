import os
import glob
import shutil
from sklearn.model_selection import train_test_split

from utils import split_data, order_test_set, create_generators

from models import streetsigns_model

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

    train_generator, val_generator, test_generator  = create_generators(batch_size,train_path, val_path, test_path)

    

