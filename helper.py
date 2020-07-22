import pandas as pd
import numpy as np
import json

def json_read(file_name):
    '''reading in the json file '''
    df_= pd.read_json(file_name, orient = 'index').iloc[:1000,:]
    return df_#.reset_index(inplace=True)




#df = df.iloc[:1000,:]

#data_df = df.data

#x = data_df[0]
'''this turns a dictionary into a list of keys and a list of values'''
def data_to_columns(row): 
    keys, values = [], [] 
    for k,v in row.data.items(): 
        keys.append(k)
        values.append(v) 
    return pd.Series(keys, values)

#print(data_to_columns(df.iloc[0,:]))

'''createing a list of all the keys in the data dictionary'''
def all_keys(df):
    all_keys = set([])
    for index, row in df.iterrows():
        all_keys |= row['data'].keys()
    return all_keys

#all_keys = all_keys(df)


'''making a df of just the data from the data dictionary'''
def data_to_df(keys_list, df):
    # rows in coal df
    num_of_rows =  df.shape[0]
    # number of keys in data dictionary
    num_of_keys = len(list(keys_list))
    return pd.DataFrame(columns=list(keys_list), data=np.zeros((num_of_rows ,num_of_keys)))


#data_df = data_to_df(all_keys,df)

'''adding empty data_df to the origonal df'''
def concat_to_df(og_df, data_df):
    return pd.concat([og_df.reset_index(drop=True),data_df],axis=1)
 

#new_df = concat_to_df(df,data_df)
#print(new_df.shape)  # = (1000, 106)

''' fill in the values of data_df part of new_df  with the values assosiated with keys/columns'''
def fill_data_vals(new_df):
    for i, row in new_df.iterrows():
        for k,v in row.data.items():
            new_df.loc[i,k] = v
    return    
        
        
        #new_df.replace(new_df.loc[k], new_df.data[k])
    #print(new_df.data.[i])
    

    ################################################3

    '''subset of columns with starting string'''
    


