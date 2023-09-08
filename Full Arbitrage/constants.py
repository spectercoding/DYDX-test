from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

# !!!! SELECT MODE !!!!
MODE = "DEVELOPMENT"

# Close all open positions and orders
ABORT_ALL_POSITIONS = True

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Manage Exits
MANAGE_EXITS = True

# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 100
USD_MIN_COLLATERAL = 1880

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum Address
ETHEREUM_ADDRESS = "0x26E94A9fd047B1a26C7B5F8420d5c602F399A664"

# KEYS - PRODUCTION
# Must remember to be on mainnet on DYDX
STARK_PRIVATE_KEY_MAINNET = config('STARK_PRIVATE_KEY_MAINNET')
DYDX_API_KEY_MAINNET = config('DYDX_API_KEY_MAINNET')
DYDX_API_SECRET_MAINNET = config('DYDX_API_SECRET_MAINNET')
DYDX_API_PASSPHRASE_MAINNET = config('DYDX_API_PASSPHRASE_MAINNET')

# KEYS - DEVELOPMENT
# Must remember to be on mainnet on DYDX
STARK_PRIVATE_KEY_TESTNET = config('STARK_PRIVATE_KEY_TESTNET')
DYDX_API_KEY_TESTNET = config('DYDX_API_KEY_TESTNET')
DYDX_API_SECRET_TESTNET = config('DYDX_API_SECRET_TESTNET')
DYDX_API_PASSPHRASE_TESTNET = config('DYDX_API_PASSPHRASE_TESTNET')

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/C38A2E03uos12XB0zaw4OhkHEZm5Io8T"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/b9CmjVOibZ3s90EAMdjalLg8Q4sVzfdQ"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET
