# Simple Linear Regression_01 単回帰

import pandas as pd
from sklearn.linear_model import LinearRegression

path = './price.csv'

# read_csv 把数据解析成 Pandas 的 DataFrame object
df = pd.read_csv(path)

# DataFrame object 的其中一个method
print(df.head(5))

# LinearRegression 是 Class
# LinearRegression() 创建一个 LinearRegression object
model = LinearRegression()

# like dic. variablename[key]
x = df[['a']] # DataFrame（二维）
y = df['y'] # Series（一维）

# model.fit(x,y) 训练模型的method
model.fit(x,y)

# model.fit(x,y)训练后，可以读取模型学到的属性
intercept = model.intercept_ # 3.3。 它会return 一个 float
coef = model.coef_ # [2.5]。 它会return一个array
Rscore = model.score(x,y) # method
print (f'y={coef[0]}x+{intercept}')

# price prediction
price_prediction = model.predict(x)
print(price_prediction)
# [12.5 18.3 25.6 30.2]

print(type(price_prediction))
# <class 'numpy.ndarray'>


# ==================================================
# Understanding matplotlib
# ==================================================