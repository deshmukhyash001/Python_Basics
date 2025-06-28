import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def main():

    df = pd.read_csv('User_Data.csv')
    print(df)
    x = df.iloc[:,2:3]
    y = df.iloc[:,3:4]
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    lsr=LinearRegression()
    y_pred = lsr.fit(x_train,y_train)
    y_pred = lsr.predict(x_test)
    print(y_pred)


if __name__ == '__main__':
    main()
