import pandas as pd

def main():
    df = pd.read_csv('./data/data_cleaned_2021.csv', index_col='index')
    df = df.drop_duplicates()
    df.to_csv('./data/data_duplicates_dropped.csv')


if __name__ == "__main__":
    main()
