#!/usr/bin/python3
import pandas as pd
def main():
    excel_file = 'movies.xls'

    movies = pd.read_excel(excel_file) #create a Dataframe object
    print(movies.head())
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    #chooses the first column "Title as index"

    print(movies_sheet1.head())

    movies_sheet1.head(5).to_excel("5movies.xlsx") #export 5 movies from top dataframe to excel
    movies_sheet1.head(5).to_json("5movies.json")
    movies_sheet1.head(5).to_json("5movies.csv")
    
if __name__ == "__main__":
    main()

