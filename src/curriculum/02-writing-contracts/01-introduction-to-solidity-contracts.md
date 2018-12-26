
# Introduction to Solidity contracts

Ethereum contracts can be written in any language as long as you can compile it to EVM (Ethereum virtual machine) bytecode.

With our eyes toward security, though, it's best for us to learn whatever language(s) clients will tend to write in.

As of this writing, Solidity is that language. Maybe also Vyper in the future though.

Solidity is officially backed by The Ethereum Foundation and nothing else seems to come close when you look at deployments.

While official documents say Solidity is "JavaScript-like", it might give you more of a C-like feel if you know that.

Take the following "Hello world" Solidity script from ethereum.org -

```
contract Mortal {
    /* Define variable owner of the type address */
    address owner;

    /* This function is executed at initialization and sets the owner of the contract */
    function Mortal() { owner = msg.sender; }

    /* Function to recover the funds on the contract */
    function kill() { if (msg.sender == owner) selfdestruct(owner); }
}

contract Greeter is Mortal {
    /* Define variable greeting of the type string */
    string greeting;

    /* This runs when the contract is executed */
    function Greeter(string _greeting) public {
        greeting = _greeting;
    }

    /* Main function */
    function greet() constant returns (string) {
        return greeting;
    }
}
```

And especially this "Minimum viable token" script from the same place -

```
pragma solidity ^0.4.20;

contract MyToken {
    /* This creates an array with all balances */
    mapping (address => uint256) public balanceOf;

    /* Initializes contract with initial supply tokens to the creator of the contract */
    function MyToken(
        uint256 initialSupply
        ) public {
        balanceOf[msg.sender] = initialSupply;              // Give the creator all initial tokens
    }

    /* Send coins */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value);           // Check if the sender has enough
        require(balanceOf[_to] + _value >= balanceOf[_to]); // Check for overflows
        balanceOf[msg.sender] -= _value;                    // Subtract from the sender
        balanceOf[_to] += _value;                           // Add the same to the recipient
        return true;
    }
}
```

## Required reading

For this first page of the section, things will be kept light.

1. [Token Foundry: What is a smart contract?](https://blog.tokenfoundry.com/what-is-a-smart-contract/)
