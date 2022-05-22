from calendar import c
import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import shutil
from sklearn.model_selection import train_test_split
import csv



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


def order_test_set(images_path, csv_path):

    try:
        with open(csv_path, 'r') as csvfile:

            reader = csv.reader(csvfile, delimiter=',')

            for i, row in enumerate(reader):

                if i==0:
                    continue

                image_name = row[-1].replace('Test/', '')
                label = row[-2]

                folder_path = os.path.join(images_path, label)

                if not os.path.isdir(folder_path):
                    os.makedirs(folder_path)

                image_full_path = os.path.join(images_path, image_name)
                shutil.move(image_full_path, folder_path)

    except:
        print('Error while reading CSV file')


                







