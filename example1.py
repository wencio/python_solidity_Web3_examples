
from web3 import Web3
infura_url ="https://mainnet.infura.io/v3/550dd3ed604f4342aaf4aa938937a274"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
balance = web3.eth.getBalance("0x0D984C3a246Da92cd74B055d730fF15c30805F5f")
print(balance)