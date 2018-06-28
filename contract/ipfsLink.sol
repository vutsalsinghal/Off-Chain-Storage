pragma solidity ^0.4.24;

contract IpfsLink{
	address owner;
	uint public lastHashId;
	uint hashCost = 0.001 ether;

	struct IpfsHash{
		address sender;
		string hashString;
		uint timestamp;
	}

	mapping (uint => IpfsHash) hashes;
    
	modifier onlyOwner {
		require(msg.sender == owner);
		_;
	}
	
	constructor() public{
		owner = msg.sender;
		lastHashId = 0;
	}

	function () public payable{
	    
	}
	
	function saveHash(string _hashContent) external payable {
		require(msg.value >= hashCost);

		uint hashId = ++lastHashId;
		hashes[hashId].sender = msg.sender;
		hashes[hashId].hashString = _hashContent;
		hashes[hashId].timestamp = now;
	}

	function findHash(uint _hashId) view public returns (address hashSender, string hashContent, uint hashTimestamp){
		return (hashes[_hashId].sender, hashes[_hashId].hashString, hashes[_hashId].timestamp);
	}
	
	function setHashCost(uint _hashCost) external onlyOwner{
		hashCost = _hashCost;
	}

	function transferEther(uint amount) external onlyOwner{
    	owner.transfer(amount);
    }

	function kill() public onlyOwner{
		selfdestruct(owner);
	}
}
