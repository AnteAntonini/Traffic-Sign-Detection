import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import shutil
from sklearn.model_selection import train_test_split



def display_some_examples(examples, labels):

    plt.figure(figsize=(10,10))

    for i in range(25):

        idx = np.random.randint(0, examples.shape[0]-1)
        img = examples[idx]
        label = labels[idx]

        plt.subplot(5,5, i+1)
        plt.title(str(label))
        plt.tight_layout()
        plt.imshow(img, cmap='gray')

    plt.show()

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