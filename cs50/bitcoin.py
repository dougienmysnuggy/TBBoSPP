# bitcoin

# Wes Leonard 2025-08-21

import requests, sys

def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')

    try:
        n = float(sys.argv[1])
    except Exception:
        sys.exit('Command-line argument is not a number')

    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=8875b58c7442775aded30b775906421f154a3fef932fb73784ddc106363c0f70')
    response = r.json()
    price = float(response['data']['priceUsd'])

    total = price * n

    print(f'${total:,.4f}')


if __name__ == "__main__":
    main()