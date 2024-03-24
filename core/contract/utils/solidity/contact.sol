// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract MessageSender {
    address immutable owner;
    
    mapping(string => string) public contactForm;

    constructor() {
        owner = msg.sender;
    }

    function setRecord(string memory messageID, string memory data_) public {
        require(msg.sender == owner, "Only the owner can update records");
        contactForm[messageID] = data_; // data_ contains concatenation of name, subject, ref, and message
    }

    function getRecord(string memory messageID) public view returns (string memory) {
        return contactForm[messageID];
    }
}
