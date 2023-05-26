from sklearn import preprocessing
import pandas as pd


df = pd.read_csv('biomechanics_processed.csv')

le = preprocessing.LabelEncoder()
le.fit(df.iloc[ :, -1:])
df.iloc[ :, -1:] = le.transform(df.iloc[ :, -1:])

print(df)