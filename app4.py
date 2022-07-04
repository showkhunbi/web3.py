import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = "0x863325174DBCBb76e11aC492555BD693F78b221c"

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting("NEW GREETING").transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print(f"Updated greeting: {contract.functions.greet().call()}")
