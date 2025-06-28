import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('marks.csv')
print(df)
x = df.iloc[:,2:3]

y = df.iloc[:,3:4]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print("x and y train")
print(x_train)
print(y_train)
print("x and y test")
print(x_test)
print(y_test)

lrn = LinearRegression()
lrn.fit(x_train,y_train)
y_predict = lrn.predict(x_test)
print("Prediction of y_ for sem 4 is ",x_test)
