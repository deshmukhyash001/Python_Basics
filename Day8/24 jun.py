import pandas as pd
def main():

    data = {
        'ID': range(1, 16),  # 1 to 15
        'Name': ['Person' + str(i) for i in range(1, 16)],
        'Age': [30 + (i % 5) for i in range(15)],
        'Score': [70 + i for i in range(15)]
        
    }
    df = pd.DataFrame(data)
    print("First 5 rows from datasets : ",df.head(5))
    print("Last 5 rows from datasets : ",df.tail(5))
    print(" ")
    print("Shape Of Dataframe:",df.shape)
    print("\nInformation :")
    df.info()
    print(" ")
    print("Description :",df.describe())
    print(" ")
    df = df.rename(columns={'Name': 'Full Name', 'Age': 'Years'})

    print(df)
    print(" ")

    df['ID'] = df['ID'].astype(str)         
    df['Years'] = df['Years'].astype(float) 
    df['Score'] = df['Score'].astype(int)   
    print("\nData Types After Conversion:")
    print(df.dtypes)
    print(" ")
    df = df.drop('Score', axis=1)
    print(df)
    print(" ")
    print(df['Full Name'])
    print(" ")

    f_df = df[df['Years']>30]
    print(f_df)
    print(" ")

    s_df = df.sort_values(by='ID', ascending=False)
    print(s_df)




if __name__ == '__main__':
    main()
