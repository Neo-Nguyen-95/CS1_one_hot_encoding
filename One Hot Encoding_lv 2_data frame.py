"""
Objective: one hot encoding
Principle: 
- Input dataframe:
    ID, Trait
    1, "A"
    2, "B"
    3, "C"
    4, "A"
- Output dataframe:
    ID, Trait_A, Trait_B, Trait_C
    1, 1, 0, 0
    2, 0, 1, 0
    3, 0, 0, 1
    4, 1, 0, 0
"""
# Case 2: Using pandas

import pandas as pd

df_in = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Trait": ["geometry", "number", "probability", "geometry"]
    })

print("\nIntput:\n")
print(df_in)
# print("\nUnique values:", df_in["Trait"].unique())
# print("\nUnique value counts:", df_in["Trait"].value_counts())

def one_hot_encoding(df_in, encoding_col):
    dict_out = {}
    for trait in df_in[encoding_col].unique():
        dict_out[encoding_col + "_" + trait] = []
    df_out = pd.DataFrame(dict_out)
    
    for index in range(len(df_in)):
        dict_out = {}
        for trait in df_in[encoding_col].unique():
            if df_in[encoding_col].iloc[index] == trait:
                dict_out[encoding_col + "_" + trait] = [1]
            else:
                dict_out[encoding_col + "_" + trait] = [0]
        df_out = pd.concat([df_out, pd.DataFrame(dict_out)])
    
    df_out = df_out.reset_index()
    df_out.drop(columns="index", inplace=True)
    df_out = df_in.join(df_out)
    
    return df_out

print("\nOutput:\n")
print(one_hot_encoding(df_in, "Trait"))