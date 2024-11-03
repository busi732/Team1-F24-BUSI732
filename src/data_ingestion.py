import pandas as pd

def ingest_data(file_path):
    '''
    Function to ingest data form a given file path
    input:
        file_path: a str of data file path
    output:
        DataFrame: loaded data as a DataFrame
    '''

    data = pd.read_csv(file_path)
    return data