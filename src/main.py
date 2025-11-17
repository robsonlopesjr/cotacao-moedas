from clients import CoinConversorService

client = CoinConversorService()
conversion = client.converter("BTC", "BRL")

print(conversion)