import requests


def get_prices():
    name = "NAME OF PROJECT"

    crypto_data = requests.get("https://api.pancakeswap.info/api/tokens").json()["data"]

    data = None
    for i in crypto_data:
        current = crypto_data[i]

        if current['name'] == name:
          data = {
              "PriceUSD": current["price"],
              "PriceBNB": current["price_BNB"],
          }

    return data


if __name__ == "__main__":
    print(get_prices())