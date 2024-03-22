// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract GreenFarm {
    address public immutable owner;
    
    struct Contact {
        string messageID;
        string name;
        string subject;
        string ref;
        string message;
    }
    
    mapping(string => Contact) public contact;

    constructor() {
        owner = msg.sender;
    }

    function setRecord(string memory messageID, string memory name_, string memory subject_, string memory ref_, string memory message_) public {
        require(msg.sender == owner, "Only the owner can update records");
        contact[messageID].name = name_;
        contact[messageID].subject = subject_;
        contact[messageID].ref = ref_;
        contact[messageID].message = message_;
    }

    function getRecord(string memory messageID) public view returns (Contact memory) {
        return contact[messageID];
    }
}
