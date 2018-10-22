
- 1 Ether (ETH) = 10^18 wei
    - Is gas specified as wei?

- Big Endian stack machine
- ~185 opcodes
    - Many instructions are similar
        - PUSH1-PUSH32, DUP1-DUP16, SWAP1-SWAP16
    - Intructions have various gas cost
    - See ethervm.io or https://github.com/trailofbits/evm-opcodes

- Solidity is "JavaScript-inspired"

Finding contracts...

```
for b in range(0,6000000):
    block = w.eth.getBlock(b, full_transactions=True)
    for tx in block.transactions:
        if tx['to'] == None:
            r = w.eth.getTransactionReceipt(tx['hash'])
            address = r['contractAddress']
            if address:
                code = w.eth.getCode(address)
                if code == '0x' and r['status'] == 1:
                    saveContract(block, address, tx['input'])
```

- Hybrid approach to finding old transactions
    - Local Ethereum software...
        - Parity
        - Geth
    - ...plus [EtherScan API](https://etherscan.io/apis)
        - `txlist`
        - `txlistinternal`
