import json
from web3 import Web3
infura_url ="https://mainnet.infura.io/v3/550dd3ed604f4342aaf4aa938937a274"
# Conection to the Blockchain
web3 = Web3(Web3.HTTPProvider(infura_url))

#print (web3.isConnected())

latest = web3.eth.blockNumber


#print ( web3.eth.getBlock(latest))

#for i in range(0,10):
 #   print(web3.eth.getBlock(latest -i))

hash = '0x8eeada5db8c6a478f71f1b7e48e59725c352135a77a66a699152543e32260a32'

print(web3.eth.getTransactionByBlock(hash,3))
