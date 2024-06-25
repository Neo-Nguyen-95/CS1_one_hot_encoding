"""
Objective: one hot encoding
Principle: 
- Input dataframe:
    ID, Trait
    1, "A"
    2, "B,C"
    3, "C,A"
    4, "B"
- Output dataframe:
    ID, Trait_A, Trait_B, Trait_C
    1, 1, 0, 0
    2, 0, 1, 1
    3, 1, 0, 1
    4, 1, 0, 0
"""
# Case 3: Using pandas, input dataframe can have multiple index

import pandas as pd

# import input dataframe
df_in = pd.DataFrame({
    "item": [1, 2, 3, 4],
    "competency": ["A", "A, B, C", "C,A", "B"]
    })

print("Input:\n")
print(df_in)

def one_hot_encoding(df_in, encoding_col):
    # create a trait list
    trait_list = []
    for i in range(len(df_in)):
        for trait in df_in[encoding_col].iloc[i].replace(" ","").split(","):
            trait_list.append(trait)
    trait_list = set(trait_list)
    
    # create a blank output
    dict_out = {}
    for trait in trait_list:
        dict_out[encoding_col + "_" + trait] = []
    df_out = pd.DataFrame(dict_out)
    
    # fill the output row by row
    for index in range(len(df_in)):
        dict_out = {}
        
        for trait in trait_list:
            for item_trait in (df_in[encoding_col].iloc[index]
                               .replace(" ","").split(",")):
                if item_trait == trait:
                    dict_out[encoding_col + "_" + trait] = [1]
        df_out = pd.concat([df_out, pd.DataFrame(dict_out)])
    
    # join output with input
    df_out = df_out.reset_index()
    df_out.drop(columns="index", inplace=True)
    df_out.fillna(0, inplace=True)
    df_out = df_in.join(df_out)
    
    return df_out

df_out = one_hot_encoding(df_in, "competency")

print("\nOutput:\n")
print(df_out)