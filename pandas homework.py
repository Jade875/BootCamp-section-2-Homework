#Jadesola Kassim
#HW Questions Numpy

#question 1
import pandas as pd
df = pd.read_cvs('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df_20 = df.loc[::20, ['Manufacturer', 'Model', 'Type']]

print(df_20.head())

df = pd.read_cvs('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Min.Price'].fillna(df['Min.Price'].median(), inplace=True)

import pandas as pd

df = pd.DataFrame(np.random.randtint(10, 40, 60).reshape(-1, 4))

rowsover100 = df[df.sum(axis=1) > 100]

print(rowsover100)