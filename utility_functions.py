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

#>>>

def symbol_to_path(symbol,base_dir="data"):
    return os.path.join(base_dir,f"{symbol}.csv")

def temp(symbols,dates):
    """Returns stock data (Open) for given symbols from CSV file"""
    df1 = pandas.DataFrame(index=dates)
    if "FB" not in symbols:
        symbols.insert(0,"FB")
    for symbol in symbols:
        df2 = pandas.read_csv(
            symbol_to_path(symbol),
            index_col="Date",
            parse_dates=True,
            usecols=["Date","Open"],
            na_values="nan"
            
        )
        
        df2 = df2.rename(columns={"Open": symbol})
        df1 = df1.join(df2, how="inner")
        df1 = df1.dropna()
    return df1

def main():
    dates = pandas.date_range("2021-11-11","2021-11-23")
    symbols = ["DIS","AAPL","WMT"]
    df1 = temp(symbols,dates)
    print(df1)
    
if __name__=="__main__":
    main()
        
    
        
        