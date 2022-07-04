import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account_1 = "0xd7Ba651Ac22BA3d32C35f2B055AA088D289f3fcd"
account_2 = "0x7b07376e2494427a4EAAe0B6aEe826395291ceE1"
private_key = "94ba518b7381b4fb8c698998e278a04dccc0d9671ce06b2ca37508fe8cd3284a"

# get the nance
nonce = web3.eth.getTransactionCount(account_1)
print(nonce)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei')
}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))
