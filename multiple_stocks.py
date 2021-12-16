import pandas

### >>>

def main():
    """This function shows Walt Disney's stock change between this period of time:"""
    start_date = "2021-02-02"
    end_date = "2021-02-10"
    dates = pandas.date_range(start=start_date,end=end_date)
    dataf = pandas.DataFrame(index=dates)
    df_walt_disney = pandas.read_csv("data/DIS.csv",
                                     index_col="Date",
                                     parse_dates=True,
                                     usecols=["Date","Open","Close","Adj Close"]
                                     )
    dataf2 = dataf.join(df_walt_disney).dropna()
    print("="*35)
    print("Walt disney stock changes:")
    print("="*35)
    print(dataf2)   
    print("\n")                                          

if __name__=="__main__":
    main()
#### new function >>>>> below

def main():
     """This function shows Apple's stock change between this period of time:"""
     start_date = "2021-11-22"
     end_date = "2021-11-30"
     dates = pandas.date_range(start=start_date, end=end_date)
     df = pandas.DataFrame(index=dates)
     df_APPLE = pandas.read_csv("data/AAPL.csv",
                                index_col="Date",
                               parse_dates=True,
                               usecols=["Date","Open","Close","Adj Close"])
    
     df1 = df.join(df_APPLE).dropna()
     print("="*35)
     print("Apple stock changes:")
     print("="*35)
     print(df1)

if __name__=="__main__":
    main()
