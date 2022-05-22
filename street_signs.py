import os
import glob
import shutil
from sklearn.model_selection import train_test_split

def split_data(data_path, save_train_path, save_val_path, split_size=0.1):

    folders = os.listdir(data_path)

    for folder in folders:
        
        full_path = os.path.join(data_path, folder)
        images_paths = glob.glob(os.path.join(full_path, '*.png'))

        x_train, x_val = train_test_split(images_paths, test_size=split_size)

        for x in x_train:

            path_to_folder = os.path.join(save_train_path, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)

        for x in x_val:

            path_to_folder = os.path.join(save_val_path, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)

if __name__ == "__main__":

    data_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Train"
    save_train_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\train"
    save_val_path = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\training_data\\val"
    split_data(data_path, save_train_path = save_train_path, save_val_path = save_val_path)



