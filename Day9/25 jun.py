import pandas as pd
from sklearn.model_selection import train_test_split

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

df_d_r = df.drop([1, 3], axis=0)

print(df_d_r)
df_filled = df.fillna(0)
print(df_filled)

df_dropped_any = df.dropna()
print(df_dropped_any)

mean_df = df.groupby('sem1').mean()
print(mean_df)

sum_df = df.groupby('sem1').sum()
print(sum_df)

count_df = df.groupby('sem1').count()
print(count_df)

df['sem4'] = df['sem1'].apply(lambda x: x * 2)
print(df)


DataFrame1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [26,28,25]
})

DataFrame2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Age': [24, 27, 22]
})
print(DataFrame1)
print(DataFrame2)
merged = pd.merge(DataFrame1, DataFrame2, on='Age')
print(merged)

joined = DataFrame1.join(DataFrame2)
print(joined)

result = pd.concat([DataFrame1, DataFrame2])
print(result)
