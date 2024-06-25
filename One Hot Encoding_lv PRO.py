import pandas as pd
import numpy as np 

# INPUT
items = pd.DataFrame({
    "Item ID": [1, 2, 3],
    "Specification": ["romantic,horror", "action,romantic", "comedy,anime"]
    })

print("\nIntput:\n")
print(items)

# ONE HOT ENCODING
# specify all specification in a list & index them with dict
specs = ['romantic', 'horror', 'action', 'comedy', 'anime']
spec_index_by_name = {name: index for index, name in enumerate(specs)}

# create a zeros matrix for output, just fill 1 later
item_features = np.zeros((len(items), len(specs)))

# loop through item
for index, specs_item in enumerate(items['Specification']):
    # loop through each item's specification
    for spec in specs_item.split(','):
        # x = index, y = spec_index
        spec_index = spec_index_by_name[spec]
        # replace 1 at target location
        item_features[index, spec_index] = 1

output = items.join(pd.DataFrame(item_features, columns=specs))
print("\nOuttput:\n")
print(output)
