import os
import glob
import shutil
from sklearn.model_selection import train_test_split

from utils import split_data, order_test_set

if __name__ == "__main__":

    if False:
        data_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Train"
        save_train_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\train"
        save_val_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\val"
        split_data(data_path, save_train_path = save_train_path, save_val_path = save_val_path)
    
    images_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Test"
    csv_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Test.csv"
    order_test_set(images_path, csv_path)



