import numpy as np 
import pandas as pd 
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
    standardScaler,
    Minmaxscaler,
    robustscaler,
)

#missing value handle 
def fill_missing (df,colum,mathod="mean",value=None):
    """fill missing value in a column 
    method:
    mean 
    median 
    constant
    mode
    """
df=df.copy()
if column not in df.columns:
    return df
if method =="mean":
    if pd.api.types.is _numeric_dtyope(df[column]):
        df[column]=df[column].fillna(df[column].mean())
        elif method == "median":
            if pd.api.types.is_numeric _dtype(df[column]):
                df[column]=df[column].fillna(df[column].median())
                elif method == "mode":
                    mode = df[column].mode ()
                    if len(mode)> 0:
                        df [column] = df[column].fillna(made[0])
                        elif method == "constant":
                            df[column] = df[column].fillna(value)
                            return df 

# remove rows
def remove_missing_rows(df):
    df = df.copy() 
    return df.dropna()

    #remove column 
    def remove_missing_columns(df):
        df = df.copy() 
        return df.dropna(axis = 1) 

        # drop seledted columns
        def drop_columns(df,columns): 
            df = df.copy() 
            return df.drop(columns=columns)

            #remove duplicates 
            def remove_duplicates(df):
                df = df.copy()
                return df.drop_duplicates() 

                #rename columns
                def rename_column(df,old_name.need_name):
                    df =df.copy()
                    if old_name not in df.columns:
                        return df
                        return df .rename(
                            columns = {
                                old_name:new_name
                            }
                        ) 

# change datatypes 
def convert_datatype(df,column,datatype):
    df = df.copy() 
    try:
        if datatype == "int":
            df[column] = df[column].astype(int)
            elif datatype =="float":
                df[column] = df[column].astype(float)
            elif datatype == "str":
                df[column] = df[column].astype(str) 
            elif datatype == "bool":
                df[column]= df[column].astype(bool)
            elif datatype == "datatime":
                df [column] = pd.to_datatime(df[column])
                except Exception:
                    pass
                    return df 

                    # replace values 
                    def replace_values(df, column, old_value, new_value):
                        df = df.copy()
                        df[column] =df[column].replace(old_value,new_value)
                        return df

#remove negative values 
def remove_negative_values(df,column):
    df = df.copy()
    if pd.api.types.is_numeric_dtype(df[column]):
        df = df[df[column]>=0]
        return df 

        # remove empty string 
        def remove_empty_strings(df):
            df = df.copy()
            df.replace("",np.nan,inplace = True)
            return df 

            # trim spaces 
            def trim_spaces(df):
                df = df.copy()
                for col in df.select_dtpyes(include = "object"):
                    df[col] = df[col].str.strip()
                    return df 

                    #lowecase text 
                    def lowecase_columns(df):
                        df = df.copy()
                        object_cols = df.select_dtype(include = "object").columns
                        for col in object_cols:
                            df[col] = df[col].str.lower()
                            return df                         
#uppercase text 
def uppercase_columns(df):
    object_cols = df.select_dtype(include = "object").columns
    for col in object_cols:
        df[col] = df[col].str.upper()
        return df

# title case function
        def title_case_columns(df):
            df = df.copy()
            object_cols = df.select_dtypes(include="object").columns
            for col in object_cols:
                df[col] = df[col].str.title()
                return df 

               
 # reset indexes
                def reset_index(df):
                    return df.reset_index(drop = True)

# sort values 
def sort_dataframe(df,column,ascending = True):
    return df.sort_values(
        by = column,
        ascending=ascending
    )

    #filter rows
    def filter_rows(df,colum,value):
        return df[df[column] == value]
        
        # LABEL encoder 
        def label_encoder(df,columns):
            df = df.copy()
            encoder = LabelEncoder()
            for col in columns
            if col in df.columns:
                df[col] = encoder.fit_transform(
                    df[col].astype(str)
                )
            return df

            # one hot encoder
            def one_hot_encoder(df,columns):
                df = df.copy()
                df = pd.get_dummies(
                    df,
                    columns=columns
                    drop_first=False
                )    
                return df

                #standard scalar 
                def standar_scale(df, columns):
                    df = df.copy()
                    scaler = standardScaler()
                    df[columns] = scaler.fit_transform(df[columns])
                    return df

                    # minmax scalar 
                    def minmax_scale(df, columns):
                    df = df.copy()
                    scaler = Minmaxscaler()
                    df[columns] = scaler.fit_transform(df[columns])
                    return df

                    # robust scalar
                     def standar_scale(df, columns):
                    df = df.copy()
                    scaler = robustScaler()
                    df[columns] = scaler.fit_transform(df[columns])
                    return df

                    # fill all numeric 
                    def fill_all_numeric(df)
                    df = df.copy()
                    numeric = df.select_dtpyes(include=np.number).columns
                    for col in numeric:
                        df [col] = df[col.fillna(df[col].mean())]
                        return df

                     # fill all categories:
                        def fill_all_categorical(df):
                            categorical = df.select_dtpyes(include = ["object","category"]).columns
                            for col in categorical:
                                mode = df[col].mode()
                                if len(mode) > 0:
                                    df[col] = df[col].fillna(mode[0])
                                    return df

                      # pipeline
                    def preprocess_datasrt(df):
                    df = remove_duplicates(df)
                    df = remove_empty_strings(df)
                    df = fill all numerical(df)
                    df = fill all categorical(df)
                    df = reset_index(df)
                    return df
             
                    



