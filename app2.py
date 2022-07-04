import json
from web3 import Web3

infural_url = "https://mainnet.infura.io/v3/6dd7a97c    c9e4449d9c7e3d4414b72067"

web3 = Web3(Web3.HTTPProvider(infural_url))

abi = ""
address = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"
