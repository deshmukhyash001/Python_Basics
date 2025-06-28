import pandas as pd

def main():
    df = pd.read_csv('marks.csv')
    print(df)

    df['Result']=df['sem1']+df['sem2']+df['sem3']+df['sem4']
    print("Addition all sem marks : ",df['Result'])

    df['Average']=df['Result']/4
    print(df['Average'])

    df['Grade']=df['Average'].apply(lambda x: 'pass' if x > 50 else 'fail')
    print(df['Grade'])



if __name__ == '__main__':
    main()
