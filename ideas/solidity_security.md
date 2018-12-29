
# Solidity security cheat sheet

## Relevant Q+A

#### What's the difference between smart contracts and dapps?

Smart contracts are self-executing contracts where the terms are written directly as code.

A decentralized application (dapp) is a peer-to-peer (P2P) application, running on >1 system. These can run on a distributed virtual machine like Ethereum or a more traditional P2P network like BitTorrent.

Difference between these, if any, is up for debate. Maybe they include each other.

#### What is gas?

TODO

#### What is the block gas limit?

TODO

---

## Standards

- [Decentralized Application Security Project (DASP)](https://www.dasp.co/)
    - Top 10, currently has 2018 list out
    - Initiative of NCC Group
- [Smart contract weakness classifications](https://smartcontractsecurity.github.io/SWC-registry/)
    - Maintained by the Mythril team (Consensys)

**Other high-profile resources, wouldn't exactly call them "standards" though**

- [Solidity documentation's own security considerations](https://solidity.readthedocs.io/en/latest/security-considerations.html)

---

## Risks

### Re-entrancy

> Any interaction from a contract (A) with another contract (B) and any transfer of Ether hands over control to that contract (B). This makes it possible for B to call back into A before this interaction is completed. [1]

> Ether transfer can always include code execution, so the recipient could be a contract that calls back into `withdraw`. [1]

> To avoid re-entrancy, you can use the Checks-Effects-Interactions pattern ... [1]

> Note that re-entrancy is not only an effect of Ether transfer but of any function call on another contract. [1]

<small><i>Appears in: Solidity doc security considerations</i></small>

### Programming quirks put contract in a vulnerable state

These are situations where vulnerability may arise from a developer not understanding a programming quirk.

#### "Private" information and default visibility

From Solidity docs security considerations:

> Everything you use in a smart contract is publicly visible, even local variables and state variables marked `private`. [1]

Thus pseudo-randomness via a normal contract will be predictable because you can't hide the seed, really.

A best practice, still, is always specifying the visibility of all functions in a contract.

If you don't specify the visibility of something...

1. It will default to public
2. `solc` (Solidity compiler) will throw warnings there's no explicit visibility set

<small><i>Appears in: Solidity doc security considerations</i></small>

#### Gas limit and loops

> Loops that do not have a fixed number of iterations, for example, loops that depend on storage values, have to be used carefully ... Either explicitly or just due to normal operation, the number of iterations in a loop can grow beyond the block gas limit which can cause the complete contract to be stalled at a certain point. [1]

Make sure to handle that state/possibility of your contract running out of gas and stalling at the loop.

<small><i>Appears in: Solidity doc security considerations</i></small>

#### Inline assembly

Solidity can support this and it just sounds pretty dangerous.

### Threat actor causes unhandled, vulnerable state

These are ways a malicious actor can force your contract into a possibly unhandled - thus vulnerable - state.

#### Sending and receiving Ether

> Neither contracts nor "external accounts" are currently able to prevent that someone sends them Ether. Contracts can react on and reject a regular transfer, but there are ways to move Ether without creating a message call. One way is to simply "mine to" the contract address and the second way is using `selfdestruct(x)`. [1]

Long story short here is, there are ways for a malicious actor to try and force your contract into an unexpected state by sending Ether at it. Gas running out might not be enough to save you because a malicious actor could forward more gas along.

Cited best practice here which helps a lot of times is to use a **withdraw pattern** instead of a **send pattern**.

<small><i>Appears in: Solidity doc security considerations</i></small>

#### Callstack depth

> External function calls can fail any time because they exceed the maximum call stack of 1024. In such situations, Solidity throws an exception. Malicious actors might be able to force the call stack to a high value before they interact with your contract. [1]

Your contract calls an external contract and has not safely handled the possibility of that failing. An attacker may be able to ensure such a failure, yielding an unexpected state in your contract.

<small><i>Appears in: Solidity doc security considerations</i></small>

### Poor authorization / access control

These are examples of faults in authorization that can be exploited.

#### tx.origin

You should check authorization (i.e. for your wallet's `transferTo` function) as follows...

```
// GOOD
require(msg.sender == owner);

// BAD
require(tx.origin == owner);
```

There are conditions in which an attacker can be the recipient without your knowledge, and you the `tx.origin`

i.e. you send their malicious wallet Ether then they do `TxUserWallet(msg.sender).transferTo(owner, msg.sender.balance)`

<small><i>Appears in: Solidity doc security considerations</i></small>

### Insufficient input validation

These issues are introduced as a result of insufficient input validation.

#### Integer overflow/underflow

Validate inputs using `require` to limit their size to a reasonable range.

Overflow example - the following is true.

```
uint8(255) + uint8(1) == 0
```

Underflow example - the following is true.

```
uint8(0) - uint8(1) == 255
```

Best mitigation is using (*calling*) mathematical libraries which replace the standard math operators (addition, subtraction, multiplication).

i.e. OpenZeppelin SafeMath

Second best, do things how they're done there. These will all cost more gas but it's in the interest of security.

Otherwise - just be very careful.

<small><i>Appears in: Solidity doc security considerations</i></small>

#### Two's complement

This is kind of an obscure subclass of integer overflow and underflow issues.

> In general, read about the limits of two's complement representation, which even has some more special edge cases for signed numbers. [1]

> This [two's complement] method of doing arithmetic is used on almost all systems because the overhead of doing floating point math is so high. [1]

> When integer math is performed, the appropriate bits are flipped , but the result incrementing a large positive number can be a large negative number or zero. [1]

> The result of decrementing a large negative number can be a large positive number. [1]

> If the results require that another bit than is available in the datatype be allocated, the leftmost digit is simply truncated. [2]

Mitigation advice is same as typical integer overflow/underflow.

<small><i>Appears in: Solidity doc security considerations</i></small>

### Compiler bugs

The Solidity documentation maintains a list of known security-relevant bugs that have appeared in the compiler. Includes dates of when a given bug was introduced then when it was fixed.

[https://solidity.readthedocs.io/en/latest/bugs.html](https://solidity.readthedocs.io/en/latest/bugs.html)

---

## Recommendations

### Take all compiler warnings seriously

> If the compiler warns you about something, you should better change it. Even if you do not think that this particular warning has security implications, there might be another issue buried beneath it. [1]

> Also try to enable the “0.5.0” safety features as early as possible ... [1]

Assuming the Solidity version is still <0.5.0 when you read this.

### Restrict how much Ether your contract holds

> Restrict the amount of Ether (or other tokens) that can be stored in a smart contract. If your source code, the compiler or the platform has a bug, these funds may be lost. If you want to limit your loss, limit the amount of Ether. [1]

### Keep your contract small and modular

> Keep your contracts small and easily understandable. Single out unrelated functionality in other contracts or into libraries. [1]

### Use other traditional programming recommendations

> General recommendations about source code quality of course apply: Limit the amount of local variables, the length of functions and so on. Document your functions so that others can see what your intention was and whether it is different than what the code does. [1]

### Implement a fail-safe mode

> You can add a function in your smart contract that performs some self-checks like “Has any Ether leaked?”, “Is the sum of the tokens equal to the balance of the contract?” or similar things. Keep in mind that you cannot use too much gas for that, so help through off-chain computations might be needed there. [1]

> If the self-check fails, the contract automatically switches into some kind of “failsafe” mode, which, for example, disables most of the features, hands over control to a fixed and trusted third party or just converts the contract into a simple “give me back my money” contract. [1]

---

## Patterns

### Checks-Effects-Interactions

> Most functions will first perform some checks (who called the function, are the arguments in range, did they send enough Ether, does the person have tokens, etc.). These checks should be done first. [1]

> As the second step, if all checks passed, effects to the state variables of the current contract should be made. Interaction with other contracts should be the very last step in any function. [1]

---

## Tools

- Mythril OSS
    - *Consensys origin*
    - Does "concolic analysis, taint analysis and control flow checking"
    - Really static analysis, symbolic analysis and control flow checking
        - Can lint source code
        - Can do on-chain analysis
        - Visualizes via a backend LASER-Ethereum
    - Manual inspection is required to verify whether a particular overflow causes an exploitable vulnerability
- Mythril Platform
    - *Consensys origin*
    - All of Mythril OSS as SaaS
    - More "enterprise-ready" (??)
- Slither
    - *Trail of Bits origin*
    - SAST
- Echidna
    - *Trail of Bits origin*
    - Fuzzer, generates potentially malicious inputs to send at your binary
- Manticore
    - *Trail of Bits origin*
    - Dynamic binary analysis with EVM support
- Oyente
    - Believe that also looks at binary
    - Would call it DAST
- solidity-coverage
    - Code coverage tool for Solidity testing
- Remix
    - For smaller development stuff, in the browser
- Truffle
    - For bigger development stuff, local

---

## Footnotes

[1] [Solidity documentation 0.4.25](https://solidity.readthedocs.io/en/v0.4.25/security-considerations.html)

[2] [Texas Tech University cybersecurity](https://discl.cs.ttu.edu/cybersecurity/doku.php?id=vulnerability_case_study:integer_overflows_and_underflows)

---

## Further reading

https://github.com/sigp/solidity-security-blog - lots of vulnerability info with real-world examples from the biggest Ethereum hacks

https://github.com/sigp/presentations - includes presentations on web3 and Solidity security

---

## (Dump)

Visualization tools

Linters

Bug finding tools

Verification tools

- Preferred
    - Manticore - symbolic execution tool for EVM
- Other options
    - KEVM - K semantics of the EVM

Reversing tools


https://hackernoon.com/your-private-solidity-variable-is-not-private-save-it-before-it-becomes-public-52a723f29f5e

https://blog.positive.com/predicting-random-numbers-in-ethereum-smart-contracts-e5358c6b8620
