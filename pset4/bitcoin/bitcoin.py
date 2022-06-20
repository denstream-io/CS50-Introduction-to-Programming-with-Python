import requests
import sys

if len(sys.argv) == 2:
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        pass
    try:
        n = float(sys.argv[1])
    except ValueError:
        pass
    data = float( r.json()['bpi']['USD']['rate_float'])
    amount = data * n
    print(f"${amount:,.4f}")
else:
    sys.exit("Usage: python bitcoin.py bitcoin_amount")


