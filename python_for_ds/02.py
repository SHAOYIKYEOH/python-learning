# Multiple Linear Regression（重回帰分析）

import pandas as pd
from sklearn.linear_model import LinearRegression

path = './score.csv'

df = pd.read_csv(path)
print(df.head(5))

# 3 Features / Explanatory Variables（説明変数）
# 1 Target / Dependent Variable（目的変数）
x = df[['a', 'b', 'c']]  # DataFrame（2D）
y = df['y']             # Series（1D）

# Create a LinearRegression object
model = LinearRegression()
model.fit(x, y)

# Attributes learned during training
intercept = model.intercept_  # Scalar (Float)
coef = model.coef_            # NumPy Array

# score() returns R² (Coefficient of Determination)
Rscore = model.score(x, y)

print(f'y = {coef[0]}a + {coef[1]}b + {coef[2]}c + {intercept}')
print(f'R² = {Rscore}')

# score prediction
score_prediction = model.predict(x)
print(score_prediction)
# [12.5 18.3 25.6 30.2]

print(type(score_prediction))
# <class 'numpy.ndarray'>

# ==================================================
# Understanding Regression Coefficients
# ==================================================

# 假设：
# intercept = 3.3
# coef = [2.5, 3.4, 5.2]
#
# 那么回归方程为：
# ŷ = 3.3 + 2.5a + 3.4b + 5.2c
#
# coef[0] = 2.5 → a 的回归系数
# coef[1] = 3.4 → b 的回归系数
# coef[2] = 5.2 → c 的回归系数
# intercept = 3.3 → 常数项（截距）
#
# IMPORTANT:
# coef_ 的顺序与 X 的 Column Order 一致。
#
# 如果：
# x = df[['a', 'b', 'c']]
# coef[0] → a
# coef[1] → b
# coef[2] → c
#
# 如果：
# x = df[['c', 'a', 'b']]
# coef[0] → c
# coef[1] → a
# coef[2] → b
#
# 因此，解释 coef_ 时必须注意 X 的 Column Order。