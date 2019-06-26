from PIL import Image
import os
import glob
import csv

if __name__ == "__main__":
    # label for no-sign -2 -> ?
    label = -2

    # create header for csv
    pix_labels = ["pixel" + str(x+1) for x in range(28*28)]
    fieldnames = ["label"] + pix_labels

    with open('../csv/no-sign.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # set headers
        writer.writerow(fieldnames)

        for i, infile in enumerate(glob.glob("../images/*")):
            # extract file name
            file = infile.split("/")[-1]
            im = Image.open(infile).convert('LA').resize((28,28))

            # gives a list of  [(123, 255), (12, 255), ...]
            pixel_values = list(im.getdata())

            # create list of black values
            pix_array = [x[0] for x in pixel_values]

            print(len(pix_array))

            # append to csv
            writer.writerow([label] + pix_array)
