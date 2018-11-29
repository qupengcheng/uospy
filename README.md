# uospy library

This library is still a work in progress but currently has the ability to perform all `cluos get` functions without compiling the code.

The library now supports signing transactions/key creation for both python 2.7 and 3.x. This is the first iteration and is very rough. The key creation has not been tested fully and should be used at your own risk.

The cluos commands currently implemented.
```
Usage: /usr/local/bin/cluos get SUBCOMMAND

Subcommands:
  get
    info                        Get current blockchain information
    block                       Retrieve a full block from the blockchain
    account                     Retrieve an account from the blockchain
    code                        Retrieve the code and ABI for an account
    abi                         Retrieve the ABI for an account
    table                       Retrieve the contents of a database table
    currency                    Retrieve information related to standard currencies
    accounts                    Retrieve accounts associated with a public key
    servants                    Retrieve accounts which are servants of a given account
    transaction                 Retrieve a transaction from the blockchain
    actions                     Retrieve all actions with specific account name referenced in authorization or receiver
  system
    newaccount                  Create an account, buy ram, stake for bandwidth for the account
```

This library is very much a work in progress.

## Installation

### Linux
```
# create virtual environment
mkdir -p ~/envs/uospy
virtualenv ~/envs/uospy
# activate the environment
source ~/envs/uospy/bin/activate
# install the library
pip install git+https://github.com/uosnewyork/uospy
```

### Windows

1. Install python
You can use either Python 2.7 or 3.7 however we suggest python 3.7 as we have tested that version more thoroughly.
https://www.howtogeek.com/197947/how-to-install-python-on-windows/
[Python 2.7](https://www.python.org/downloads/release/python-2715/)
[Python 3.7](https://www.python.org/downloads/release/python-370/)

2. Install git
https://www.atlassian.com/git/tutorials/install-git

3. Install uospy
```
pip install git+https://github.com/uosnewyork/uospy
```

## API Endpoints
For a more complete list of API endpoints check out:

https://www.uosdocs.io/resources/apiendpoints/

## Command line Tool Examples
```
# Get chain information
pycluos --url https://api.uosnewyork.io get info

# get information about a block
pycluos --url https://api.uosnewyork.io get block 447

# Retrieve an account from the blockchain
pycluos --url https://api.uosnewyork.io get account --account uosio

# Retrieve the code and ABI for an account
pycluos --url https://api.uosnewyork.io get code --account uosio

# Retrieve the ABI for an account
pycluos --url https://api.uosnewyork.io get abi --account uosio

# Retrieve the contents of a database table
pycluos --url https://api.uosnewyork.io get table --code uosio --scope uosio --table producers

# Retrive currency information
pycluos --url https://api.uosnewyork.io get currency balance --code uosio.token --symbol UOS --account aaaaaaaaaaaa
pycluos --url https://api.uosnewyork.io get currency stats --code uosio.token --symbol UOS

# get accounts associated with public key
pycluos --url https://api.uosnewyork.io get accounts --key UOS52gpRqAPfggYHLXbMuC4TSQd8WWWo94KrMq4umgUcjM62Y2dWF

# get transaction information
pycluos --url https://api.uosnewyork.io get transaction --transaction 42dacd5722001b734be46a2140917e06cd21d42425f927f506c07b4388b07f62

# get account actions
pycluos --url https://api.uosnewyork.io get actions --account aaaaaaaaaaaa

```

## Examples

Check out the examples directory for some examples of how to use the library

