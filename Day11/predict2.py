import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def main():
    df = pd.read_csv('User_Data.csv')
    print(df)
    x = df.iloc[:,2:4]
    y = df.iloc[:,4:5]
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


    print("Please enter the info :")
    age = float(input("Age:"))
    salary = float(input("Salary:"))
    lsr=LinearRegression()
    lsr.fit(x_train,y_train)
    y_pred = lsr.predict(pd.DataFrame([[age,salary]],columns=x.columns))
    print(y_pred)

    if y_pred>=0.5:
        print("You can buy")
    else:
        print("You can't buy")


if __name__ == '__main__':
    main()
