# make_dataset.py
import pathlib
import yaml
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(data_path):
    # Load your dataset from a given path
    df = pd.read_csv(data_path)
    return df

def split_data(df, test_split, seed):
    # Split the dataset into train and test sets
    train, test = train_test_split(df, test_size=test_split, random_state=seed)
    return train, test

def save_data(train, test, output_path):
    # Save the split datasets to the specified output path
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)
    train.to_csv(output_path + '/train.csv', index=False)
    test.to_csv(output_path + '/test.csv', index=False)

def main():

    curr_dir = pathlib.Path(__file__)# directory of the current file i.e. make_dataset.py
    home_dir = curr_dir.parent.parent.parent # home directory of the project
    params_file = home_dir.as_posix() + '/params.yaml' # path to params.yaml file # as_posix() converts string path to python path
    params = yaml.safe_load(open(params_file))["make_dataset"] # load parameters related to make_dataset only from params.yaml file

    input_file = sys.argv[1] # Or /raw/creditcard.csv
    data_path = home_dir.as_posix() + input_file # loacation of creditcard.csv file
    output_path = home_dir.as_posix() + '/data/processed' # location to save the train and test datasets
    
    data = load_data(data_path)# loading the data
    train_data, test_data = split_data(data, params['test_split'], params['seed']) # seed is the factor to random generator in train, test split
    save_data(train_data, test_data, output_path) # saving the train and test datasets

if __name__ == "__main__":
    main()