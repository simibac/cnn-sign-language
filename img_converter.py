from PIL import Image
import os
import glob
import csv

# label for no-sign
label = -1
size = 28, 28
color = "LA"

# create header for csv
pix_labels = ["pixel" + str(x+1) for x in range(28*28)]
fieldnames = ["label"] + pix_labels

with open('no-sign.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # set headers
    writer.writerow(fieldnames)

    for i, infile in enumerate(glob.glob("./images/*")):
        file = infile.split("/")[-1]
        im = Image.open(infile).convert('LA')

        # resize
        im.thumbnail(size)
        width, height = im.size
        # gives a list of  [(123, 255), (12, 255), ...]
        pixel_values = list(im.getdata())

        # create list of black values
        pix_array = [x[0] for x in pixel_values]

        # append to csv
        writer.writerow([-1] + pix_array)
