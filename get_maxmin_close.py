import pandas as pd


def get_max_close(symbol):
    """
    Returns company's stock max close 
    """
    df = pd.read_csv(f"data/{symbol}.csv")
    return df["Close"].max()

def main():
    print("\nMax close:")
    for symbol in ["AAPL","FB","DIS","WMT"]:
        print(symbol + ":", get_max_close(symbol))

if __name__=="__main__":
    main()

def get_min_close(symbol):
    """Returns the company's min close
    """
    df = pd.read_csv(f"data/{symbol}.csv")
    return df["Close"].min()

def main():
    print("\nMin close:")
    for symbol in ["AAPL","FB","DIS","WMT"]:
        print(symbol + ":", get_min_close(symbol))

if __name__=="__main__":
    main()

