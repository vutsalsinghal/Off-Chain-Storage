# Off-Chain-Storage

## Ðapp Preview
<div align="center">
    <img src="https://pyofey.pythonanywhere.com/static/dapp.png"><br><br>
 </div>

## Requirements

- (Use of virtualenv is strongly recommended!) `pip install requirements.txt`
- MetaMask [extension](https://metamask.io/)
- Remix - Solidity [IDE](https://remix.ethereum.org/#optimize=true)

## Deployment

- Create ethereum account using MetaMask. Make sure to choose "Ropsten Test Network"
- Request few ethers from the test [faucet](https://faucet.metamask.io/)
- Go to Remix solidity IDE and copy-paste the contents of opinion.sol file in the IDE.
- Click on "Start to compile" from the Compile tab in the top right corner.
- After compiling it, go to Run tab and click on "deploy". Metamask should bring up a popup asking you to confirm the transaction. If not, just open the Metamask extension and do it there.
- A message at the bottom of the Remix console will notify you when the contract is deployed. You can click on the link to explore the transaction on [ropsten.etherscan.io](https://ropsten.etherscan.io/). Note the contracts address!
- Download Django source code.
- Now the root folder of source code:
    ```bash
    $ mkvirtualenv --python=python3 venv
    $ pip install requirements.txt
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    $ ./manage.py runserver
  ```
- Now navigate to `localhost:8000/ipfsLink`
