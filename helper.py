import pandas as pd
import numpy as np
import json

def json_read(file_name):
    '''reading in the json file '''
    df_= pd.read_json(file_name, orient = 'index').iloc[:1000,:]
    return df_#.reset_index(inplace=True)


'''this turns a dictionary into a list of keys and a list of values'''
def data_to_columns(row): 
    keys, values = [], [] 
    for k,v in row.data.items(): 
        keys.append(k)
        values.append(v) 
    return pd.Series(keys, values)


'''createing a list of all the keys in the data dictionary'''
def all_keys(df):
    all_keys = set([])
    for index, row in df.iterrows():
        all_keys |= row['data'].keys()
    return all_keys


'''making a df of just the data from the data dictionary'''
def data_to_df(keys_list, df):
    # rows in  df
    num_of_rows =  df.shape[0]
    # number of keys in data dictionary
    num_of_keys = len(list(keys_list))
    #return a matrix of zeros of aproprie size
    return pd.DataFrame(columns=list(keys_list), data=np.zeros((num_of_rows ,num_of_keys)))


'''concatenation matrix of zeros to the origonal df'''
def concat_to_df(og_df, data_df):
    return pd.concat([og_df.reset_index(drop=True),data_df],axis=1)
 

''' fill in the values of zeros matrix with the values assosiated with year keys'''
def fill_data_vals( df):
    for i, row in concat_to_df(df, data_to_df( all_keys(df),df)).iterrows():
        for k,v in row.data.items():
            new_df.loc[i,k] = v
    return new_df 
        
