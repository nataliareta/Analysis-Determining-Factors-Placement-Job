import pandas as pd
import statsmodels.api as sm
import numpy as np

df = pd.read_csv('Clean_CollegePlacement.csv')

# Target to biner
df['Placement'] = df['Placement'].map({'Yes': 1, 'No': 0})

# Kolom kategori dikonversi jadi angka
for col in df.columns:
    if df[col].dtype == 'object':
        print(f"Kolom {col} berupa object, dan dikonversi ke numeric")
        df[col] = pd.factorize(df[col])[0]

# Variabel independen & dependen
X = df[['IQ', 'Prev_Sem_Result', 'CGPA', 'Academic_Performance',
        'Internship_Experience', 'Extra_Curricular_Score',
        'Communication_Skills', 'Projects_Completed']]
y = df['Placement']

# Ubah semua nilai jadi float
X = X.astype(float)
y = y.astype(float)

# Tambahkan konstanta dan jalankan model
X = sm.add_constant(X)
model = sm.Logit(y, X).fit()
print(model.summary())

odds_ratios = pd.DataFrame({
    "Variable": X.columns,
    "Odds_Ratio": np.exp(model.params)
})
print(odds_ratios)

result = pd.DataFrame({
    'Variable': model.params.index,
    'Coef': model.params.values,
    'Odds_Ratio': np.exp(model.params.values),
    'p_value': model.pvalues.values
})
result.to_csv('logistic_result.csv', index=False)


print(df.dtypes)
