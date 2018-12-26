
# Vuln gauntlet

Time to test your knowledge and see if you can catch what's wrong with some Solidity snippets.

### Example 1

```
function LCOpenTimeout(bytes32 _lcID) public {
    require(msg.sender == Channels[_lcID].partyAddresses[0] && Channels[_lcID].isOpen == false);
    require(now > Channels[_lcID].LCopenTimeout);

    if(Channels[_lcID].initialDeposit[0] != 0) {
        Channels[_lcID].partyAddresses[0].transfer(Channels[_lcID].ethBalances[0]);
    } 
    if(Channels[_lcID].initialDeposit[1] != 0) {
        require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], Channels[_lcID].erc20Balances[0]),"CreateChannel: token transfer failure");
    }

    emit DidLCClose(_lcID, 0, Channels[_lcID].ethBalances[0], Channels[_lcID].erc20Balances[0], 0, 0);

    // only safe to delete since no action was taken on this channel
    delete Channels[_lcID];
}
```

### Example 2

```
pragma solidity ^0.4.18;

contract AddressGuessGame {

    function withdrawWinnings() {
        // Winner if last 8 hex characters of the address are 1
        require(uint32(msg.sender) == 1);
        _sendWinnings();
     }

     function _sendWinnings() {
         msg.sender.transfer(this.balance);
     }
}
```

### Example 3

```
pragma solidity ^0.4.18;

contract Token {
    mapping(address => uint) balances;

    function Token(uint _initialSupply) {
        balances[msg.sender] = _initialSupply;
    }

    function transfer(address _to, uint _value) public returns (bool) {
        require(balances[msg.sender] - _value >= 0);
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        return true;
    }

    function balanceOf(address _owner) public constant returns (uint balance) {
        return balances[_owner];
    }
}
```

### Example 4

```
 // Claim the throne for the given name by paying the currentClaimFee.
function claimThrone(string name) {

    uint valuePaid = msg.value;

    // If they paid too little, reject claim and refund their money.
    if (valuePaid < currentClaimPrice) {
        msg.sender.send(valuePaid);
        return;
    }

    // If they paid too much, continue with claim but refund the excess.
    if (valuePaid > currentClaimPrice) {
        uint excessPaid = valuePaid - currentClaimPrice;
        msg.sender.send(excessPaid);
        valuePaid = valuePaid - excessPaid;
    }
}
```

### Example 5

```
pragma solidity ^0.4.18;

contract AddressGuessGame {

    function withdrawWinnings() {
        // Winner if last 8 hex characters of the address are 1
        require(uint32(msg.sender) == 1);
        _sendWinnings();
     }

     function _sendWinnings() {
         msg.sender.transfer(this.balance);
     }
}
```

### Example 6

```
pragma solidity ^0.4.15;

contract CrowdFundBad {
    address[] private refundAddresses;
    mapping(address => uint) public refundAmount;

    function refundDos() public {
        for(uint i; i < refundAddresses.length; i++) {
            require(refundAddresses[i].transfer(refundAmount[refundAddresses[i]]));
        }
    }
}
```

---

### Answer key

| Example ID | Vulnerability                                                   |
|------------|-----------------------------------------------------------------|
| 1          | Reentrancy                                                      |
| 2          | Access control - sendWinnings gets default (public) visibility  |
| 3          | Arithmetic                                                      |
| 4          | Unchecked calls                                                 |
| 5          | Access control                                                  |
| 6          | Denial of service                                               |
