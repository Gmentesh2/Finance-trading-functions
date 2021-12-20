import pandas
# adj close stock changes
def main():
    """This function shows several company's stock changes in a certain period of time"""
    start_date = "2021-10-10"
    end_date = "2021-10-20"
    dates = pandas.date_range(start=start_date,end=end_date)
    datafr = pandas.DataFrame(index=dates)
    dataf_apple = pandas.read_csv(
        "data/AAPL.csv",
        index_col="Date",
        parse_dates=True,
        usecols=["Date","Adj Close"]
    )
    dataf_apple = dataf_apple.rename(columns={"Adj Close": "AAPL"})
    new_df = datafr.join(dataf_apple, how="inner").dropna()
     
    symbols = ["DIS","FB","WMT"]
    for symbol in symbols:
        dataf_temp = pandas.read_csv(
            f"data/{symbol}.csv",
            index_col="Date",
            parse_dates=True,
            usecols=["Date","Adj Close"]
        )
        dataf_temp = dataf_temp.rename(columns={"Adj Close" : symbol})
        new_df = new_df.join(dataf_temp)
    print("                           -Adj Close-")
    print(new_df)
        
    
if __name__=="__main__":
    main()
    
# open stock changes 

def main():
     """This function shows several company's stock changes in a certain period of time"""
     start_date = "2021-03-03"
     end_date = "2021-03-10"
     dates = pandas.date_range(start=start_date,end=end_date)
     first_df = pandas.DataFrame(index=dates)
     pref_df = pandas.read_csv(
         "data/FB.csv",
        index_col="Date",
        parse_dates=True,
        usecols=["Date","Open"]
     )
     pref_df = pref_df.rename(columns={"Open":"FB"})
     first_df = first_df.join(pref_df,how="inner").dropna()
     
     symbols = ["DIS","AAPL","WMT"]
     for symbol in symbols:
         temp_df = pandas.read_csv(
             f"data/{symbol}.csv",
             index_col="Date",
             parse_dates=True,
             usecols=["Date","Open"]
         )
         temp_df = temp_df.rename(columns={"Open": symbol})
         first_df = first_df.join(temp_df)
     
     print(first_df)

if __name__=="__main__":
    main()





