import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
import itertools
import random
import csv
from PIL import Image 

# labels are stored as an array
def retrieve_label(label_array):
    for i in range(10):
        if label_array[i] > 0:
            return i

# show random image with label
def show_random_image():
    nth = random.randint(0, len(data_x))
    plt.imshow(data_x[nth])
    print(retrieve_label(data_y[nth]))
    plt.xlabel(retrieve_label(data_y[nth]))
    plt.show(block=False)
    plt.pause(2)
    plt.close()

# display imgage function
def display_image(img, label):
    plt.imshow(img.reshape(28, 28), 'binary')
    plt.xlabel(chr(label + 65))
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == "__main__":
    # create header for csv
    pix_labels = ["pixel" + str(x+1) for x in range(28*28)]
    fieldnames = ["label"] + pix_labels

    # load files
    data_x = np.load("../digits/X.npy")
    data_y = np.load("../digits/Y.npy")

    # store number of images
    num_images = len(data_x)

    # write each image to csv
    with open('../csv/digits.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        # set headers
        writer.writerow(fieldnames)

        for i in range(num_images):
            # subtracting 17 for ascii encoding
            label = retrieve_label(data_y[i]) - 17

            # resize to 28x28
            new_img = np.array(Image.fromarray(data_x[i]).resize((28,28)))
            # new_img = imresize(data_x[i], (28, 28))
            pix_array = new_img.flatten()

            # scale it to values from 0 to 255
            scaled = np.asarray([int(i * 255) for i in pix_array])

            writer.writerow([label] + list(scaled))