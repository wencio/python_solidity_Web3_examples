
from web3 import Web3

ganache_url ="http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print (web3.isConnected())
print (web3.eth.blockNumber)

account_1 ="0x826c0aD58e217b234fcA4Fa1E70Da6681de95fdC"
account_2 ="0x26e0F3ec62feB74Ab60C2886A59d789F1b8D49Ee"

private_key ='d90849c9d907dc7a78594f8800f6a9d4d48e3d345f20c102d02ed5fd0515904e'

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)

#build transaction

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1,'ether'),
    'gas':200000,
    'gasPrice':web3.toWei('50','gwei')

}

#sign the transaction

signed_tx = web3.eth.account.signTransaction(tx,private_key)

#send the transaccion

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaccion hash

print (web3.toHex(tx_hash))