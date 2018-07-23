# [Off-Chain-Storage](http://dapp.pythonanywhere.com/ipfsLink)

Web 3.0 apps (Ðapp) now-a-days need to store/retrieve data just like Web 2.0 (conventional/centralized) apps. But it is extremely costly (computationally and hence monetarily) to store data (> few bytes) for eg PDF, images, etc on EVM. The EVM allow us to save variables/state in permanent storage cheaply. So a possible solution to store large data is to save the data off-chain using options such as: [IPFS](https://ipfs.io/) and [Swarm](http://swarm-guide.readthedocs.io/en/latest/introduction.html). In this Ðapp, IPFS has been used for off-chain storage!

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
- Now open the root folder of the source code in terminal:
    ```bash
    $ mkvirtualenv --python=python3 venv
    $ pip install requirements.txt
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    $ ./manage.py runserver
  ```
- Now navigate to `localhost:8000/ipfsLink`
