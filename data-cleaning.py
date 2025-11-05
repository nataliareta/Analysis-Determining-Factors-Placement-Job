import pandas as pd

df = pd.read_csv('CollegePlacement.csv')
print(df.head(10))

# Statistik numerik
print("\n Deskripsi Data")
print(df.describe())

# Missing Value
print("\n Missing Value")
print(df.isnull().sum())

# Delete Duplicates
df = df.drop_duplicates()

# Sort by ID
df = df.sort_values(by='College_ID')

# Validasi Data
df['College_ID'] = df['College_ID'].astype('category')

df.to_csv('Clean_CollegePlacement.csv', index=False)
