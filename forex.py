from forex_python.converter import CurrencyRates

def get_forex_opening_price_difference():
    """Fetch the opening price difference for the day for each forex pair."""
    c = CurrencyRates()
    forex_pairs = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/USD', 'USD/CAD']
    price_difference = {}

    for pair in forex_pairs:
        rates = c.get_rates(pair.split('/')[0])
        opening_rate = rates[pair.split('/')[1]]
        current_rate = c.get_rate(pair.split('/')[0], pair.split('/')[1])
        difference = current_rate - opening_rate
        price_difference[pair] = difference

    return price_difference

# Fetch and print the opening price difference for the day for each forex pair
opening_price_difference = get_forex_opening_price_difference()
for pair, difference in opening_price_difference.items():
    print(f"{pair}: {difference}")

