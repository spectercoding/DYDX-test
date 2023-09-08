import datetime
from decouple import config
from dydx3 import Client
from web3 import Web3
from constants import (
  HOST,
  ETHEREUM_ADDRESS,
  DYDX_API_KEY,
  DYDX_API_SECRET,
  DYDX_API_PASSPHRASE,
  STARK_PRIVATE_KEY,
  HTTP_PROVIDER,
)

from dydx3.constants import NETWORK_ID_GOERLI

# Connect to DYDX
def connect_dydx():

  # Create Client Connection
  client = Client(
      host=HOST,
      api_key_credentials={
          "key": DYDX_API_KEY,
          "secret": DYDX_API_SECRET,
          "passphrase": DYDX_API_PASSPHRASE,
      },
      stark_private_key=STARK_PRIVATE_KEY,
      eth_private_key=config("ETH_PRIVATE_KEY"),
      default_ethereum_address=ETHEREUM_ADDRESS,
      web3=Web3(Web3.HTTPProvider(HTTP_PROVIDER)),
      api_timeout = 30000,
      network_id= NETWORK_ID_GOERLI,
  )
  
  # Confirm client
  # account = client.private.get_account()
  # account_id = account.data["account"]["id"]
  # quote_balance = account.data["account"]["quoteBalance"]
  # print("Connection Successful")
  # print("Account ID: ", account_id)
  # print("Quote Balance: ", quote_balance)

  # Return Client
  return client
