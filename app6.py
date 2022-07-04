from web3 import Web3

infural_url = "https://mainnet.infura.io/v3/6dd7a97cc9e4449d9c7e3d4414b72067"

web3 = Web3(Web3.HTTPProvider(infural_url))
latest_block = web3.eth.blockNumber
print(web3.isConnected())
print(latest_block)


# print(web3.eth.getBlock(latest_block))

# for i in range(0, 10):
#     print(web3.eth.getBlock(latest_block - i))

# hash = "0x6516dc927528be4dc3d20b78cfadfed25519f481c694d772d3a8955c890016ff"
# print(web3.eth.getTransactionByBlock(hash, 2))
