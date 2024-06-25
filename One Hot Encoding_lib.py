import pandas as pd

#%% SINGLE VALUE TRAIT
from category_encoders import OneHotEncoder
# INPUT
items = pd.DataFrame({
    "Item ID": [1, 2, 3, 4],
    "Specification": ["LV1", "LV2", "LV3", "LV1"]
    })

ohe = OneHotEncoder(use_cat_names=True)
X = ohe.fit_transform(items[["Specification"]])

print(X)


#%% MULTIPLE VALUE TRAIT
from sklearn.preprocessing import MultiLabelBinarizer

# INPUT
items = pd.DataFrame({
    "Item ID": [1, 2, 3],
    "Specification": [["M1", "M2"], ["M1", "M3"], ["M2", "M3"]]
    })
items
mlb = MultiLabelBinarizer()

X = mlb.fit_transform(items["Specification"])
col_names = mlb.classes_
print(pd.DataFrame(X, columns=col_names, index=items["Item ID"]))
