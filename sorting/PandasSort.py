#### Sorted With Pandas ####
import pandas as pd

data = {'Name': ['Rahul', 'Rohan', 'Sourav', 'DD'],
        'Age': [26, 19, 35, 22]}

df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Age')
print(sorted_df)

