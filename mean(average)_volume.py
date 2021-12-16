import pandas

def mean_volume(symbol):
    """Returns company's average stock buying/selling volume"""
    df = pandas.read_csv(f"data/{symbol}.csv")
    return df["Volume"].mean()

def main():
    print("\nCompany average stock volume:")
    print("-" * 30)
    symbols = ["AAPL","FB","DIS","WMT"]
    for symbol in symbols:
        print(symbol + ":", mean_volume(symbol))
    print("-" * 30)

if __name__=="__main__":
    main()