# Fixed Effects Model（固定効果モデル）

import pandas as pd
import statsmodels.formula.api as smf

path = './panel_data.csv'

# Read CSV into a DataFrame object
df = pd.read_csv(path)
print(df.head(5))

# 3 Features / Explanatory Variables
# a, b, c

# 1 Target / Dependent Variable
# y

# 2 Fixed Effects
# prefecture, year

# Create an OLS model with Fixed Effects
# C() treats a variable as categorical and creates dummy variables
model = smf.ols(
    formula='y ~ a + b + c + C(prefecture) + C(year)',
    data=df
)

# Fit the model
results = model.fit()

# Access estimated coefficients
coef = results.params

# Access R²
Rscore = results.rsquared

# Print coefficients for the 3 features
print(coef[['a', 'b', 'c']])

# Print R²
print(f'R² = {Rscore}')

# Print regression results
print(results.summary())

# Predict y
prediction = results.predict(df)

print(prediction)