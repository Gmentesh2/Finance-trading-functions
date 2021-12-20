import os 
import pandas


def s_to_path(symbol, main_dir= "data"):
    """Returns CSV file path to given ticker symbol"""
    return os.path.join(main_dir,f"{symbol}.csv")


def get_data(symbols,dates):
    """Returns stock data (Adj Close) for given symbols from CSV file"""
    data_f = pandas.DataFrame(index=dates)
    if "AAPL" not in symbols:
        symbols.insert(0,"AAPL")
    for symbol in symbols:
        dataframe_temp = pandas.read_csv(
            s_to_path(symbol),
            index_col="Date",
            parse_dates=True,
            usecols=["Date","Adj Close"],
            na_values=["nan"]
        )
        dataframe_temp = dataframe_temp.rename(columns={"Adj Close": symbol})
        data_f = data_f.join(dataframe_temp)
        data_f = data_f.dropna() 
        
    return data_f

def main():
    dates = pandas.date_range("2021-02-02","2021-02-10")
    symbols = ["DIS","FB","WMT"]
    data_f = get_data(symbols, dates) 
    print(data_f)
    
if __name__=="__main__":
    main()

       
        
        
        