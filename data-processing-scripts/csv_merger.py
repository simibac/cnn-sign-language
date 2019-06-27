import os
import glob
import pandas as pd

# train test ratio 4:1
ratio = 5

# header for csv
pix_labels = ["pixel" + str(x+1) for x in range(28*28)]

def convert_to_ascii(num):
    return num + 65

# 0-9: digits, 10-35: characters, 36:?
def map(num):
    if num==63:
        return 36
    elif num < 91 and num > 64:
        return num - 55
    elif num < 58 and num > 47:
        return num - 48

if __name__ == "__main__":
    # load data frames
    df_test = pd.read_csv("../csv/sign_mnist_test.csv")
    df_train = pd.read_csv("../csv/sign_mnist_train.csv")
    df_numbers = pd.read_csv("../csv/digits.csv")
    df_nosign = pd.read_csv("../csv/no-sign.csv")

    # shuffle digits dataset
    df_numbers = df_numbers.sample(frac=1)

    num_rows = df_numbers.shape[0]

    df_numbers_train = df_numbers.iloc[:int(num_rows * (4/5)), :]
    df_numbers_test = df_numbers.iloc[int(num_rows * (4/5)):, :]

    # shuffle nosign dataset
    df_nosign = df_nosign.sample(frac=1)

    num_rows = df_nosign.shape[0]

    df_nosign_train = df_nosign.iloc[:int(num_rows * (4/5)), :]
    df_nosign_test = df_nosign.iloc[int(num_rows * (4/5)):, :]

    #combine all files in the list
    df_test = df_test.append(df_numbers_test)
    #df_test = df_test.append(df_nosign_test)

    df_train = df_train.append(df_numbers_train)
    #df_train = df_train.append(df_nosign_train)

    # bring all labels in ASCII encoding
    df_train['label'] = df_train['label'].apply(convert_to_ascii)
    df_test['label'] = df_test['label'].apply(convert_to_ascii)

    # bring all labels in compact encoding
    df_train['label'] = df_train['label'].apply(map)
    df_test['label'] = df_test['label'].apply(map)

    print(df_train)
    print(df_test)

    df_train.to_csv("../sign_mnist_train_digit_chars.csv")
    df_test.to_csv("../sign_mnist_test_digit_chars.csv")