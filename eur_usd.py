def eur_usd(eur, rate):
    usd = eur * rate
    return f"{usd:0.2f}"



if __name__ == "__main__":
    print(eur_usd(100,0.84))