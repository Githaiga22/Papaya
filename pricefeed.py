"""
 * @title Papaya Price Feed Oracle
 * @author Allan Robinson
 * @notice Real-time price feeds for crypto and fiat assets
 * @dev Created: January 9, 2026
 * Data Sources: CoinGecko API (crypto), ExchangeRate API (fiat)
 * Supports: BTC, ETH, SOL, XRP, USDC, USDT, KSH
 """

import requests

def get_crypto_price_from_coingecko(crypto_id):
    """Fetch real-time crypto price from CoinGecko API (free, no auth needed)"""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return float(response.json()[crypto_id]["usd"])
        else:
            raise Exception
    except:
        # Fallback prices (approximate)
        fallback_prices = {
            "ripple": 0.52,
            "ethereum": 3500,
            "bitcoin": 42000,
            "solana": 100,
            "tether": 1.0,
            "usd-coin": 1.0
        }
        return fallback_prices.get(crypto_id, 1.0)

def get_fiat_rate(currency_code):
    """Fetch fiat currency rates (KSH = Kenyan Shilling)"""
    try:
        # Map asset names to ISO currency codes
        currency_map = {
            "KSH": "KES",  # Kenyan Shilling ISO code is KES
        }

        # Using exchangerate-api.com (free tier)
        url = f"https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            rates = response.json()["rates"]
            # Use mapped currency code for API lookup
            iso_code = currency_map.get(currency_code, currency_code)
            if iso_code in rates:
                return 1 / rates[iso_code]  # Convert to USD value
            else:
                raise Exception(f"Currency {iso_code} not found in rates")
        else:
            raise Exception
    except:
        # Fallback rates
        fallback_rates = {
            "KSH": 1/130.0,  # 1 USD = ~130 KSH
        }
        return fallback_rates.get(currency_code, 1.0)

def get_exchange_rates():
    """Get real-time exchange rates for all supported assets"""
    rates = {
        # Fiat
        "KSH": get_fiat_rate("KSH"),

        # Stablecoins (always ~$1)
        "USDC": get_crypto_price_from_coingecko("usd-coin"),
        "USDT": get_crypto_price_from_coingecko("tether"),

        # Cryptocurrencies
        "XRP": get_crypto_price_from_coingecko("ripple"),
        "ETH": get_crypto_price_from_coingecko("ethereum"),
        "BTC": get_crypto_price_from_coingecko("bitcoin"),
        "SOL": get_crypto_price_from_coingecko("solana"),
    }
    return rates

if __name__ == "__main__":
    rates = get_exchange_rates()
    print(rates)
