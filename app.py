from web3 import Web3

infural_url = "https://mainnet.infura.io/v3/6dd7a97cc9e4449d9c7e3d4414b72067"

web3 = Web3(Web3.HTTPProvider(infural_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

balance = web3.eth.getBalance('0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9')

print(web3.fromWei(balance, 'ether'))
