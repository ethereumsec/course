
## Consensys Academy 2018 notes

Notes from taking the Consensys Academy 2018 developer course.

### Review of blockchain technology

### Blockchain primitives

- **Cryptographic hash functions**
    - Map input data of any size to output data of fixed size
    - 5 main properties
        - Deterministic
            - Same input should always produce the same output
        - Fast
            - Hashing 1 bit versus 1 gigabyte should not take much more time
        - Infeasible to reverse
            - Cannot compute the input data, given the result
            - Therefore a one-way function
        - Slightly different inputs should produce very different outputs
            - Apparent randomness because of this
        - Collision resistant
            - Should not be able to find two different inputs that give same output
    - Applications of hash functions
        - Verifying data integrity
            - Comparing downloaded file's hash against reputable hash is useful
            - Checksums
            - Password hashing
        - Proof of work
            - Prevents service abuse by requiring the requester to put in computationally expensive work
            - Hard for the requester to find a hash within a given threshold
            - Easy for someone to check that the hash is within that threshold (work has been done)
            - This mechanism can be used to reduce spam
        - Data identification
            - Using hashes as data identifiers is common in peer-to-peer file sharing networks
        - Pseudo-random number generation (PRNG)
- **Public key cryptography** (asymmetric cryptography)
    - Any cryptographic system that uses pairs of keys
    - Random data goes into a key generation algorithm which outputs a public key and private key
        - Means of generating that initial random data must be protected
        - Public key may be disseminated widely
        - Private key is known just to owner
        - Owner can sign stuff with private key then others can verify they were the signer with public key
- **Merkle trees**
    - *Resources*
        - [Wikipedia](https://en.wikipedia.org/wiki/Merkle_tree)
        - [Brilliant.org](https://brilliant.org/wiki/merkle-tree/)
- **General blockchain structure**
    - Blockchains maintain a system state that everyone participating can agree on
        - Various participants agree on updates
    - Features of blockchain
        - Maintain state in a peer-to-peer network
        - Manage state updates
            - All participants agree that updates are valid
            - Consensus on new system state
- Updates are broken into sets (blocks)
    - Summarized via Merkle tree root hash
- Blocks also reference previous blocks
    - Creates a chain
    - Creates a continual link back through time to the beginning of the system
- **Simple block example**
    - A block includes
        - A list of transactions
        - A Merkle tree based on the list of transactions
        - A hash of the previous block
        - A nonce
            - Used in proof-of-work
            - Modified to get valid block hash
            - Consensus on new system state
    - Once constructed, a valid block is broadcast to the network
        - Other participants can easily verify the validity of the block
        - Created (accepted) blocks are immutable
            - Chain of immutability runs through the system
            - Changing one previous block makes the whole thing unacceptable because of the hashes linking all data
    - Then work begins on finding the next block
        - Newly discovered block includes hash of the valid block before it
- **Smart contracts**
    - Term generally refers to a computer protocol that digitally executes terms of a contract
    - More specific definition for this course's context
        - Code stored on the blockchain that self-executes using the trust and security of the blockchain network
        - Application logic that runs in a distributed fashion on the Ethereum blockchain and operates using the EVM
    - Should have the following features...
        - Trustless
            - No third-parties or intermediaries
            - Universally accessible
        - Trackable
            - All transactions can be traced
            - Auditability
        - Irreversible
            - Transactions are final
            - Security is paramount
        - Self-executing
            - Reduce costs
            - Increase speed
            - Use-case variability
    - Notable papers
        - Nick Szabo's 1994 one on smart contracts
            - Smart contracts = "set of promises, specified in digital form, including protocols within which the parties perform on these promises"
        - Bitcoin paper from Satoshi Nakamoto
        - Vitalik Buterin's Ethereum whitepaper
            - Titled "A next-generation smart contract and decentralized application platform"
            - Smart contracts = "cryptographic 'boxes' that contain value that only unlock if certain conditions are met"
    - Ethereum Virtual Machine (EVM)
        - Developers can define their own instructions
        - Digitally binding agreements are coded on a public ledger
        - Allows anyone to build a wide array of decentralized applications (DApps)
    - Multiple Turing-complete programming languages for EVM now
        - Solidity
            - Most notable
            - Similar to JavaScript
            - Develop contracts and compile to EVM bytecode
            - Most robust docs, most popular among developers
        - Viper
        - Low-level List-like Language (LLL)
            - Used to write assembly code that interacts with the EVM
            - Much smaller binaries than Solidity contracts
- **Nodes**
    - Traditional Internet applications are *server-based*
        - Slow
        - Have a single point of failure (the server)
        - Huge bandwidth demand placed on the server because it has to serve so many people
    - Decentralized applications (DApps) are *peer-based*
        - Fast
        - All computers share information
        - No privileged users (all *nodes* get the same thing)
    - Blockchains operate on *peer-to-peer networks*
        - Nodes participate by running the appropriate software
        - Your computer could be any of the following depending on what software it runs
            - Bitcoin node
            - Ethereum node
            - BitTorrent node
    - Connecting in Ethereum peer-to-peer networks?
        - Computer with a Web3-capable browser
            - ...uses RPC to talk to a...
        - Ethereum node (gateway)
            - ...uses P2P connection(s) to talk to...
        - Whole Ethereum network
    - 3 ways nodes can participate in Ethereum network
        - 1. Run a light client
            - Shallow copy of the blockchain
            - Suited for less-powerful computers
        - 2. Full node
            - Full copy of the blockchain
            - Also check against double-spending and other bad stuff
        - 3. Mining
            - All of the above
            - Plus they verify transactions, working towards more blocks
- **Blockchain forks**
    - Fork occurs when a blockchain splits into two competing, concurrent chains
    - Can happen for various reasons
        - Intentional or unintentional
            - Intentional could be a big software upgrade
            - Unintentional could be a competitor reveals itself
        - Network changes
        - Community disagreement
    - Also *hard forks* and *soft forks*
        - Hard forks
            - The new chain is incompatible with the old one
            - The two chains never meet again
            - Nodes must switch to new software to continue generating blocks
            - Used if clear consensus is established around a change
            - If a clear winner chain isn't established, the economics, politics can ruin the project
        - Soft forks
            - The change is backward compatible with the original state of the software before the fork
                - Both rulesets exist in the same chain
                - If a 51% of the network adopts the new rules, old rules will no longer be accepted
            - Mostly used for smaller network changes
    - Unintentional forks!
        - Happens in proof-of-work or consensus systems when 2 miners find a block at the same time
        - Each miner broadcasts their block discovery at the same time
            - Nodes start mining on whichever of the 2 blocks they hear about first
        - 2 concurrent chains are constructed, both with valid histories
        - But eventually one chain will get ahead of the over and that will be the sole accepted chain again
            - This is why the general rule is to wait for 6 block confirmations
            - If you go 6 confirmations, the likelihood your chain is correct is very close to 100%

### Ethereum basics

- **Accounts**
    - In Ethereum, the state is made up of objects called *accounts*.
        - Each account...
            - ...is stored in a Merkle Patricia tree
            - ...has a 20-byte address
        - 2 types of accounts
            - *Externally owned* accounts are owned by people
                - Their state includes balance (Ether/ETH)
                - Features include...
                    - Ether balance
                    - Send transactions
                        - Transfer value
                        - Initiate contract code
                    - Controlled by private keys
                    - Nonce
            - *Contract* accounts are generated by smart contracts
                - Their state includes balance (Ether/ETH) and storage
                - Features include...
                    - Ether balance
                    - Can transfer value
                    - Can call other contracts
                    - Have an associated smart contract
                        - Initiated by external transactions
                        - Can manipulate its storage
                    - Nonce
    - Generating accounts
        - Externally owned accounts
            - Whenever a user generates a private-public keypair, a corresponding account is created as well
            - Randomness is used to create the private and public keys
            - The 20-byte address is derived from the public key
        - Contract accounts
            - Can be generated by externally owned accounts or other contract accounts
- **Transactions**
    - A transaction is a message sent from an externally owned account
    - Transactions update state
        - Ether (ETH) balance
        - Contract storage
    - They're always signed by their sender
    - Not on the blockchain until they're mined and included in the block
    - Transactions are not required to send Ether
    - They optionally include
        - Ether
        - Data
    - If the target is a contract then code executes with data as input
        - Thus the transaction that kicks this off will include data
    - If the target account is 0
        - Transaction creates a new contract
        - Transaction data is executed
            - Output is stored as the contract
    - So Ethereum transactions have...
        - Recipient specified
        - Nonce from the sender's account
            - Transaction count from the sender
        - Cryptographic variables: V, R, and S
            - Make up the sender's signature
            - Verify that the sender's signature is valid
        - Value
            - Optional
            - Amount of Ether to send with the transaction
            - Defaults to 0
            - Is in wei, which is a subdenomination or base unit of Ethereum
        - Data
            - Optional
            - Specifies contract instructions or deployment instructions
        - Gas Limit or Start Gas
            - The maximum number of computational steps the transaction execution is allowed to take
        - Gas Price
            - The fee the sender pays per computational step
            - The more you're willing to pay, the faster your transaction will get processed
- **Gas & Fees**
    - Gas is the metering unit of the Ethereum Virtual Machine
    - Executing operations on Ethereum costs a fee
        - The network is like a public utility, like the electric grid
        - Gas fees are incentives for miners
        - Miners collect all gas used in a block as a reward
    - Each operation on the EVM consumes gas
        - Different operations cost different amounts
            - Multiplication = 5 gas
            - Addition = 3 gas
    - Gas is paid for with Ether
    - Gas limit and price is specified per transaction
    - Gas limit is the max gas allowed for the transaction
    - Gas price is how much Ether the sender pays per gas
    - On gas usage
        - Every operation consumes a predetermined amount of gas
            - Thus the cost of a transaction can be estimated in this sense
        - Set transaction gas limit at the beginning of a transaction
            - Start gas / gas limit
            - Start gas is sent with transaction to pay for processing
        - Every operation consumes gas
            - Remaining gas is reduced every step
            - *Can think of the gas limit as how much is in the tank to begin with*
    - Out of gas
        - If the transaction runs out of gas with steps remaining, it fails
        - The sender gets nothing in return
    - Successful transaction
        - Upon successful execution, remaining gas is returned to the sender of the transaction
    - Fees help protect the network
        - If sending transactions was free or too cheap, bad actors could flood the network
            - Reduce spam
            - Halt bad code
        - The EVM offers a Turing-complete computing environment
            - Every step costs something
            - Infinite loops will run out of funds
                - Otherwise they could break the system
    - Additional resources
        - [EthGasStation](https://ethgasstation.info/)
        - [Consensys blog post on gas](https://media.consensys.net/ethereum-gas-fuel-and-fees-3333e17fe1dc)
- **Ethereum Structure**
    - Ethereum is an open source, public blockchain-based network
        - Anyone can download the software to set up a node
        - Permissionless
            - There are no special privileges required to sign up or create an account
            - Anyone can join or contribute
        - The blockchain features provide...
            - State management
            - Trustlessness
            - Trackability
            - Irreversible
        - The Ethereum Virtual Machine
            - Execution environment
        - All this makes Ethereum an ideal system for running smart contracts
    - Distributed computing
        - Ethereum is a worldwide distributed computer
        - Ethereum Virtual Machine (EVM)
            - Runs on every node participating in the network
            - Handles all transaction processing to determine the current state of the network
            - Turing complete
            - Operates on bytecode
        - The EVM is slow
            - 10-20 transactions per second at this time
            - Every transaction is processed by every node
                - This is in order to maintain a trustless environment
                - But there are slow and fast computers
                - Only as fast as the slowest machine
            - There are upsides to this architecture...
                - Immutability
                - Significantly improved fault tolerance
                - Zero downtime
    - The EVM executes bytecode
        - Bytecode is a low level stack based language
            - Specifies how state transitions are applied to the network's state
        - Transactions contain bytecode
    - Smart contracts exist as bytecode
        - Contract accounts keep contract bytecode in storage
        - EVM executes contract bytecode when a transaction is received
        - There are several high level languages developers use to write smart contracts that compile to bytecode
            - Solidity
            - Focus of this course
            - Vyper
            - LLL (Lower-level Lisp-like Language)
    - How the network operates in the current proof-of-work system
        - Transactions are broadcast to the network
        - Miners observe these transactions and race to include them in blocks
            - Transactions grouped into sets called blocks
        - Miners compute a valid network state by applying the transactions they've included in the block
        - Trying to find a valid block hash
            - Block header with
                - Previous block hash
                - *State root* from the state Merkle tree
                - *Transactions root* from the transactions Merkle tree
                - *Receipts root* from the receipts Merkle tree
        - When a valid block is found the block is broadcast with
            - Transaction list
            - Uncles list
            - Block header
                - Previous block hash
                - *State root* from the state Merkle tree
                - *Transactions root* from the transactions Merkle tree
                - *Receipts root* from the receipts Merkle tree
                - Also includes
                    - Block number
                    - Gas used
                    - Timestamp
                    - Nonce
                    - Some other data
            - *A valid block that is found and not included in the main chain is called an uncle*
                - Uncles are a consequence of Ethereum's short block time and proof of work
                - A discovered block not included in the main chain is an uncle
                - In Bitcoin these are known as orphan blocks
                - Ethereum blocks are currently found about every 15 seconds
                    - Calls for low difficulty
                    - Low difficulty causes simultaneous discovery
                - Network latency causes an advantage to miners who are physically/geographically close to the last successful miner
                    - Nodes that get the message of a discovered block first get a head start on mining a new block
                    - This does promote centralization to physically close mining pools
                - Discovering uncle blocks is rewarded in Ethereum though
                    - Incentivization to stay decentralized
                    - Makes mining pools less attractive
    - Ethereum as a platform
        - Turing completeness allows for smart contracts
        - Accounts in Ethereum allow for digital identity management
        - Ether allows users and smart contracts to easily transfer real value
        - Applications on Ethereum
            - Use the underlying Ethereum security
            - Benefit from Ethereum protocol development
        - Interoperability
            - Standard protocol
    - Ethereum roadmap
        - In 2015 Ethereum launched its first phase called *Frontier"*
            - Barebones version of Ethereum
            - Low usability for non-technical people
        - Upgraded to *Homestead*
        - After Homestead came *Metropolis*
            - We are in Metropolis stage 1 right now, *Byzantium*
            - Homestead to Byzantium brought enhanced privacy features to the blockchain
            - Metropolis stage 2 is *Constantinople*
                - Expected sometime before end of 2018 still
        - Fourth and final phase of development is called *Serenity*
            - Serenity protocol upgrade will enable important scalability features
                - By moving Ethereum from proof-of-work secured to proof-of-stake
                    - "Casper"
                    - Scaling solutions
                - Likely several years away from now (2018) still

### Traditional & decentralized application development

- **Introducing decentralized application development**
    - Knowing when to use a blockchain is as important as knowing how to build applications for the blockchain
    - When to use a blockchain?
        - Is the system defining digital relationships?
            - Yes = account management offered by blockchain may be appropriate
            - No = blockchain not appropriate
        - Should application data by dynamic and auditable? Should there be a record of changes to the dataset?
            - Yes = blockchains record and store data updates
            - No = traditional database or decentralized storage may be a better option
        - Should data be managed by a central authority?
            - No = decentralization offered by blockchains can guarantee an immutable transaction history when a central authority cannot be trusted
            - Yes = privacy is paramount, the public nature of transactions on the blockchain is too transparent'
        - Is the speed of the network important?
            - No = consistency is more important than speed so blockchain is OK
            - Yes = blockchain not appropriate if speed trumpts consistency
    - Sample architecture for a simple DApp built on Ethereum
        - Web3-capable browser
            - HTTP/S to...
        - Static front-end (HTML/CSS/JS)
            - RPC...
        - Ethereum Node (Gateway)
            - DevP2P to Network...
        - The rest of the Ethereum network
    - Core developer tools and components
        - Blockchain
            - Ethereum protocol
        - Infrastructure
            - Infura
        - Dev tools
            - Truffle
        - Core components
            - Metamask
            - uPort
- **Traditional vs. decentralized application architectures**
- **Introducing the Ethereum development stack**
- **Overview of key developer tools**
- **Outline of Ethereum application development workflow**
    - Development blockchain options
        - Ethereum mainnet
            - Pros
                - Highest security
                - Real value
                - Immutable
                - Public
            - Cons
                - Expensive
                - Slow
                - Highest risk
        - Testnets
            - Pros
                - Public
                - Free ether
            - Cons
                - Not final
                - Still slow
        - Private network
            - Pros
                - Fast
                - Free
                - Private
            - Cons
                - Isolated
                - No real value
    - Can go from private to testnet to mainnet
    - Geth
        - Helps you transfer between any public blockchain (?)
        - Or set up a private network or consortium for testing
        - `-> public / private blockchain`
    - Ganache
        - Local private development blockchain
    - Remix
        - Browser-based
        - Has blockchain simulator
    - Metamask
        - `-> public / private blockchain`
    - Development workflow
        - Create account
            - Geth allows you to create and manage accounst via Javascript console
            - Metamask allows for account creation and manage accounts, but requires a browser and interface as it's only a browser extension
            - Ganache initializes a blockchain with 10 accounts with 100 ether each
            - Remix comes with 5 pre-funded accounts with 100 ether each
        - Fund account
            - Private net you just get ether no big deal
            - On testnets, Google for a faucet
        - Develop
            - Remix gives you a browser-based Solidity smart contract development IDE
            - More traditional text editors can do this via plugin
        - Compile to bytecode
            - Remix has a Solidity smart contract compiler
            - SolC is a command-line Solidity compiler
            - Truffle framework comes with a compiler
        - Sign & deploy
            - Mist3 is a web3-enabled browser with wallet and contract deployment
            - Remix can connect to an Ethereum node and deploy contracts
            - Truffle allows sophisticated contract migration
        - Interact & test
            - Remix includes functionality for transacting with deployed contracts
            - Metamask allows you to interact with deployed applications via browser
            - Truffle includes an automated testing framework

### Development frameworks & environment

### Smart contract fundamentals

- **Data types**
    - Solidity is a statically typed, compiled language
    - All types must be known at compile time
        - Elementary types (value)
            - Boolean
            - Integer
            - Address
            - Byte arrays
            - Enums
        - Complex types are combinations of elementary (reference)
            - Arrays
            - Structs
        - Mappings (essentially hash tables)
    - Type-wise, at least, Solidity reminds me a lot of C
    - See [**Solidity docs - Types**](https://solidity.readthedocs.io/en/latest/types.html)
- **Functions**
    - You can overload functions in Solidity
        - Multiple functions with same name
        - Each must have a different number of arguments
    - Returns
        - These are valid returns
            - `function add(uint a, uint b) returns (uint){ return (a+b); }`
            - `function add(uint a, uint b) returns (uint c){ c = a + b; }`
            - `function add(uint a, uint b) returns (uint){ uint c = a + b; return c; }`
        - This is not a valid return
            - `function add(uint a, uint b) { return (a+b) }`
    - Child functions can overload/override parent functions
        - Just needs same name in that case
- **Storage and memory**
    - Storage and memory are analogous to hard disk and RAM in a PC
    - Storage is expensive because it's written to every node
    - Memory is cheaper because its life is more-or-less contained to a function call
    - Data location will vary depending on the variable type
    - Bugs can hide in assumptions about where a variable is being stored
    - State variables are always in storage
    - Function arguments are always in memory
    - For most types, data location cannot be specified because the variables are copied every time they are used
        - With exception of arrays, structs, mappings (?)
    - Structs, arrays, and mappings are passed by reference
        - Use the `memory` keyword to copy to memory
- **Contract structure**
    - Solidity is similar to other object-oriented programming languages
    - Contracts are similar to classes and can contain:
        - State variables
        - Functions
        - Function modifiers
        - Events
        - Structs
        - Enums
    - The first line in every Solidity (`.sol`) file is the `pragma` statement
        - Indicates the valid compiler versions
        - i.e. `pragma solidity ^0.4.10` indicates between 0.4.0 and 0.4.10 is valid
    - Next is contract declaration
        - Capitalize the contract name
        - Convention is to name the file the same as the contract
            - `SimpleStorage.sol`
            - `contract SimpleStorage { ... }`
        - Contract goes in the curly braces
    - State variable declarations typically come first in the actual contract code
    - After that storage declaration, define events
        - Name events so they are clearly events
            - `event LogChange(uint newValue);`
    - Then we define function modifiers
    - Then functions
        - The contract constructor is defined with the same name as the contract
        - It is run when the contract is deployed
    - Side note on inline assembly
        - Inline assembly (EVM bytecode) is available in Solidity
        - Offers more control over the EVM stack
        - Beyond the scope of this course
            - But just be aware that it exists, be able to recognize it
            - Understanding gives insight into how the EVM works
- **Reading smart contracts**
    - What keywords are used to describe a function that does not modify the contracts' state?
        - `constant`
        - `view`
        - `pure`
        - NOT `public`
        - NOT `payable`
        - NOT `memory`
- **Smart contract ABI**
    - Essentially a list of the contract's functions and their arguments in JSON
    - Allows access to the binary stuff in the smart contract (thus "Application Binary Interface")
        - Stores contract specifications using encoding standards for the EVM
        - Provides function signatures to calculate hashes to identify function's bytecode
    - Remix can show you the ABI for what you compiled
- **Events and logs**
    - True about events...
        - Contracts cannot directly read events emitted by other contracts
        - Events are useful for making contract calls visible to a front-end
    - *False* about events...
        - Events can be declared with 'event changeStorage(sender, newStorage, oldStorage);'
        - As many parameters as an event has can be indexed for easy searchability
- **Factory contracts**
- **Remix deep dive**

### Writing smart contracts

- **Introductory smart contracts**
    - Truffle pet shop tutorial
        - Recommends following along with this in Remix
    - Writing code is easy, designing good decentralized applications is hard
        - You will pick up syntax and nuances
        - Understand Ethereum features and limitations
    - Designing the pet shop
        - Needs to keep track of 16 pets and their owners
        - Pets
            - 16 of them
            - `petId` field of type `uint`
        - People (adopters)
            - address
        - Can put all this in an array with length of 16
            - Where index is the pet's ID effectively and the value is an address
            - If address is its default initialization value of 0 then pet hasn't been adopted
            - Otherwise has the address of the adopter person
        - Functions
            - `adopt()`
                - Let user adopt pet
            - `getAdopters()`
                - Get all the adopter data from the contract
            - Functions with `view` keyword cost 0 gas because they do not alter the state of the contract

```
browser/Adoption.sol

pragma solidity ^0.4.17;

contract Adoption {

    address[16] public adopters;

    function adopt(uint petId)
        public
        returns(uint)
    {
        require(petId >= 0 && petId <= 15);
        require(adopters[petId] == 0);
        adopters[petId] = msg.sender;
        return petId;
    }

    function getAdopters()
        public
        view
        returns(address[16])
    {
        return adopters;
    }

}
```

- **Inter-contract execution**
    - Important to view contracts as first-class members of the Ethereum network who have **the same privileges as external actors**
        - Ability to issue message calls to other contracts
        - Ability to issue new contracts themselves
    - Any time one contract talks to another it uses the same ABI we would use to call it
        - Thus our **compiler must know the source code of this contract we want to call** so we know how to access its functions
    - When passed a series of contracts **the compiler assumes the contract you wish to deploy is the final one**
        - Assumes any other contracts it encounters are to be ignored until referenced in that main contract
    - Creating a new contract
        - Above we **called** another contract from a contract but we can also **create a new contract**
        - The full source code needs to be known for the contract we're creating
            - It's uploaded to the blockchain when we deploy it

```
contract metaCoin {

    mapping (address => uint) public balances;

    function metaCoin() {
        balances[tx.origin] = 10000;
    }

    function sendToken(address receiver, uint amount)
        returns(bool successful)
    {
        if (balances[msg.sender] < amount) return false;

        balances[msg.sender] -= amount;
        balances[receiver] += amount;

        return false;
    }

}

contract coinSpawn {
    function createCoin() {
        new metaCoin();
    }
}
```

- **Inheritance**
    - Similar to inheritance in Python
    - Only one contract is deployed on the blockchain
    - Uses the `is` keyword
    - The derived contract inherits state and functions
    - A contract that inherits code from another does not reference that base contract in the bytecode at all
    - Contracts can inherit multiple base contracts
    - Can override functions from base contracts
        - The following should be the same
            - Name
            - Inputs
            - Outputs
    - If a base contract constructor requires arguments, they'll go in the header
    - For multiple inheritance, order of inheritance matters
    - Specify order from the "most base like" contract to the "most derived"
    - Function, modifier, and event names must also be unique

```
pragma solidity ^0.4.0;

// This will not compile

contract X {}
contract A is X {}
contract C is A, X {}

// This is OK

contract D is X, A {}
```

    - Abstract contracts
        - Can be missing some function implementations
        - Do not compile by themselves
        - But can be used as a base contract
    - Interface contracts
        - Similar to abstract but cannot have *any* functions implemented
        - Defined with the keyword `interface`
        - No constructor, variables, structs, or enums
        - Basically limited to what the contract ABI represents

- **Libraries and EthPM**
    - Brings us to some Ethereum drawbacks
        - Every node has to execute and verify every transaction just by nature of the Ethereum system
            - Can be expensive
            - Users of the system pay for this with gas
        - There are (currently) few standard libraries for Solidity
            - Somewhat related: managing arrays and strings can be painful
        - It is relatively difficult to get verified data into the blockchain
            - Blockchains are isolated environments
            - There are not APIs like we are used to in traditional web development
            - Must use services called *oracles* to get external data into the blockchain
        - The immutability of deployed contracts makes upgradings them more difficult than upgrades in other systems
            - However we can enable "upgradability" by design if we pay extra attention to this
    - Libraries overall can help address these aforementioned drawbacks
    - Attributes of libraries
        - Contracts that do not have storage
        - Cannot hold ether
        - Cannot inherit or be inherited by other contracts
        - Do not have a state
            - Though *can* modify the calling contracts' state
    - Can be seen as implicit base contracts for the contracts that use them
    - Exist for the purpose of code reuse
        - Contracts can call library functions without having to implement or deploy those functions
        - Developers use code that has already been audited and road-tested
    - Use the `library` keyword in place of the normal `contract` keyword
    - After defining a library you can import it with an `import` statement at the top of your Solidity file
    - Libraries use the `DELETECALL` opcode of the EVM
        - Preserves the context of the contract from which the library method is being called
        - Thus allows libraries to modify the state of calling contracts
    - Libraries offer other benefits in terms of contract system design
        - Reduces the size of factory output contracts
            - A contract using the contract factory design pattern might be deploying several additional contracts
            - Can save a lot of gas in deployment costs over the lifetime of the factory contract
            - Can reduce the size of the factory output contract
            - However note that calling library functions from the factory output contracts is a bit more expensive than calling internal functions
                - Consider this in the overall tradeoff
                - If the factory output contract functions are frequently called it may be better to pay the higher deployment cost to get cheaper function calls
    - To connect to a library, you need the library contract as well as the address of the deployed instance
        - Address management will be handled by Truffle when you deploy the library yourself
        - Otherwise the address of the deployed library has to be added to the bytecode by a linker
            - (Manual stuff in Truffle for this)
    - EthPM
        - Simplifies library and contract package management
        - Essentially npm for Ethereum contracts
        - Truffle has support for it
        - Browse available packages at [ethpm.com](https://ethpm.com)
        - Can do `truffle install <package_name>`
        - Add an `ethpm.json` file to your project to track which packages and versions you are using
        - To importing into a Solidity file add the file path reference at the top of your script
- **Smart contract system design**
    - *Designing* a contract is often more difficult than coding or implementing the contract in Solidity
    - Designing a voting system
        - Users send a token to one of two contract addresses
        - Problem: how are votes distributed?
            - One human one vote? No concept of individuals on the blockchain
            - One token one vote? How are they distributed?
                - Vote is proportional to holdings
                - Split holdings and voting tokens...
        - Problem: everyone needs to vote "at the same time"
            - Vote with associated token weight, then transfer tokens to a friend to increase their weight
            - Token locking - not transfers after vote cast - locks value in a vote, skews incentives
                - Cons: total transparency (who voted for what) - skews incentives
        - Possible solution: collect all votes and count at the end?
            - Gas limits prevent transactions of indeterminate size from being an effective solution
        - Commit / reveal
            - Voters sign a vote and submit the hash
            - Reveal your own vote - only accepted if hashes match
    - Case study: Colony
        - Colony platform is for decentralized organizations
        - Voting is essential for operations
        - Users should be able to easily create polls
        - Implements a token weighted partial lock voting protocol
        - High level design
            - TokenLibrary
                - Manages Colony tokens
            - VotingLibrary
                - Contains poll and voting logic
            - Libraries hold logic, a generic contract holds the data
                - Separation of concerns
                - Good design for upgradability
        - Requirements for a poll = attributes in a data structure
            - Description
            - Options: yes, no
            - Start time
            - Close time
            - Poll status: created, active, resolved
        - Each attribute is a mapping
            - Key is the hash of the `pollId` and the attribute
            - Value is a `string` or `uint`
        - Global properties
            - Poll count
            - Options count for each poll
    - "Vote secrets"
        - A sorted double-linked list is efficiently used here
            - Sorting can be an expensive operation
            - Solution: delegrate sorting to the user
                - The location of a new node is determined by the application (client-side?)
                - The location is validated by the smart contract
    - "Secret voting"
        - `secret = sha3(salt, pollOptionId);`
        - Salt is additional random input data to obfuscate the vote
            - It should be nonsensitive info as it is going to be revealed
            - It should be unique
        - Submit vote
            - `pollId`
            - Secret
            - `prevTimestamp` = for inserting into outer linked list
            - `prevPollId` = for inserting into inner linked list
    - "Address locking"
        - An address is locked if the poll that they have voted in in closed and they have yet to reveal their vote
        - How to check this?
            - `isAddressLocked(address)`
- **Other uses of commit-reveal**

### Ethereum & the end user

- **Introduction to Web3**
- **Building Truffle for the web**
- **Integrating with React**

### Smart contract pitfalls, testing, debugging

- **Testing smart contracts**
    - Unit testing
        - Write tests to verify correct contract behavior
        - Consider edge cases
        - Consider the range of possible user input
        - Writing tests is not about finding bugs
            - It is about defining contract behavior
            - *"TDD is a robust way of designing software components ('units') interactively so that their behaviour is specified through unit tests."*
    - Truffle provides a great integrated testing environment
    - Some tenets
        - Testing contracts should not extend any other contracts
        - Truffle provides an `Assert.sol` library but you can provide your own library
        - `DeployedAddresses.sol`
        - Contract being tested
        - Contract name must begin with 'Test'

```
pragma solidity ^0.4.17;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Adoption.sol";

contract TestAdoption {
    Adoption adoption = Adoption(DeployedAddresses.Adoption());
}
```

    - Testing functions
        - Contract function begins with 'test'
        - Call the `adopt` function on the deployed contract
        - Set expected value
        - Check result

```
// Testing the adopt() function from Pet Shop
function testUserCanAdoptPet() public {
    uint returnedId = adoption.adopt(8);

    uint expected = 8;

    Assert.equal(returnedId, expected, "Adopted of pet ID 8 should be recorded.");
}
```

    - Hooks
        - Same as hooks in the Mocha Javascript testing framework
            - `beforeEach()`
            - `beforeAll()`
            - `afterEach()`
            - `afterAll()`
        - Use to setup and teardown before and after each test
        - Possible for setup function to exceed block gas limit
            - `beforeEachAgain()`
    - You can test fully with Javascript if you want but there are some differences

- **Smart contract best practices**
    - Smart contract programming requires a different engineering mindset than other programming domains
        - There is a high cost of failure
        - Can be difficult to change
    - Here it is generally not a good idea to "move fast and break things"
        - Move slow and be careful!
    - Prepare to fail
        - Bugs are inevitable so prepare
        - "Circuit Breaker" design pattern
        - Roll out carefully as catching bugs before release is always preferable
            - Automated testing
            - Use testnets
            - Time locking alpha and beta releases
            - Third party security audits
            - Bug bounties
    - Keep it simple
        - Greater complexity == more bugs
        - Don't roll your own code when you don't have to
        - Reuse audited code when possible
        - Clarity is almost always better than performance
        - Only use the blockchain when it is appropriate
    - This is a unique environment
        - Be wary of calling external contracts
        - Functions are public
            - Malicious actors will try to call your functions in unintended ways
        - Contract data is public
        - System constraints
            - Gas price
            - Block gas limits
    - Tradeoffs
        - Between engineering and security perspectives
            - Rigidity vs. upgradability
                - First for security
                - Increases attack surface
            - Monolithic vs. modular
                - First for security
            - Code duplication vs. reuse
                - If you are unsure whether you should use another contract, don't
                - Play it safe and write your own
- **Safety checklist**
    - [Consensys Known Attacks](https://consensys.github.io/smart-contract-best-practices/known_attacks/)
        - Reentrancy
            - Involves functions that can be called repeatedly before the first invocation of the function was finished
            - Can cause the different invocations of the function to interact destructively
            - Like if you send money via external function call *then* change or zero the user's balance
        - Cross-function race conditions
            - Like reentrancy, this is a race condition
            - Involves multiple functions that share same state
        - Pitfalls in race condition solutions
        - Transaction-ordering dependence (TOD) / front running
        - Timestamp dependence
        - Integer overflow and/or underflow
        - DoS with (unexpected) revert
        - DoS with block gas limit
        - Forcibly sending ether to a contract
- **Design patterns + examples**
- **Using security tools**

### Smart contract advanced topics

- **uPort integration**
- **The Ethereum name service**
- **Introduction to IPFS**
- **Upgradable contracts**
- **Oracles**
- **Design patterns**
- **Exploits and dangers**
- **Formal verification**

### Learning further

- **LLL**
- **Vyper**
- **The Ethereum Improvement Proposal**
