import pandas

def high_max(symbol):
    """Returns company's High's max value"""
    df = pandas.read_csv(f"data/{symbol}.csv")
    return df["High"].max()

def main():
    print("-"*35)
    print("\nHigh max value:")
    print("-" * 35 )
    for symbol in ["AAPL","DIS","FB","WMT"]:
        print(symbol + ":", high_max(symbol))
    print("-" * 35)

if __name__=="__main__":
    main()
############################################
def high_min(symbol):
    """Returns company's high's min value"""
    df = pandas.read_csv(f"data/{symbol}.csv")
    return df["High"].min()

def main():
    print("-"*35)
    print("\nHigh min value:")
    print("-" * 35 )
    symbols = ["AAPL","DIS","FB","WMT"]
    for symbol in symbols:
        print(symbol + ":", high_min(symbol))
    print("-"*35)

if __name__=="__main__":
    main()
############################################

def low_max(symbol):
    """Returns company's low's max value"""
    df = pandas.read_csv(f"data/{symbol}.csv")
    return df["Low"].max()

def main():
    print("=" * 30)
    print("Low max value:")
    print("="*30)
    for symbol in ["AAPL","DIS","FB","WMT"]:
        print(symbol + ":", low_max(symbol))
    print("^"*30)

if __name__=="__main__":
    main()
#############################################
def low_min(symbol):
    """Returns company's low's min value"""
    df = pandas.read_csv(f"data/{symbol}.csv")
    return df["Low"].min()

def main():
    print("="*30)
    print("Low min value:")
    print("=" * 30)
    symbols = ["AAPL","DIS","FB","WMT"]
    for symbol in symbols:
        print(symbol + ":", low_min(symbol))
    print("~"*30)
if __name__=="__main__":
    main(

    )
############################################
