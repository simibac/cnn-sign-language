import os
import glob
import pandas as pd

# train test ratio 4:1
ratio = 5

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
    df_test = df_test.append(df_nosign_test)

    df_train = df_train.append(df_numbers_train)
    df_train = df_train.append(df_nosign_train)

    print(df_train)
    print(df_test)

    df_train.to_csv("../sign_mnist_train_complete.csv")
    df_test.to_csv("../sign_mnist_test_complete.csv")