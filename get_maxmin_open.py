import pandas as pd 

def get_max_open(symbol):
    """Returs company's max open"""
    df = pd.read_csv(f"data/{symbol}.csv")
    return df["Open"].max()

def main():
    print("\nMax open:")
    for symbol in ["AAPL","DIS","FB","WMT"]:
        print(symbol + ":" , get_max_open(symbol))

if __name__=="__main__":
    main()

def get_min_open(symbol):
    """Returns company's min open"""
    df = pd.read_csv(f"data/{symbol}.csv")
    return df["Open"].min()

def main():
    print("\nMin open:")
    symbols = ["AAPL","DIS","FB","WMT"]
    for symbol in symbols:
        print(symbol + ":", get_min_open(symbol))

if __name__=="__main__":
    main()