# simple_blockchain  
A simple implementation of a ***blockchain*** & a corresponding ***web app*** in order to interact with it  
  
**Built using:**    
-Flask, HashLib(sha256)  
  
**What you can do:**  
-You can retrieve the whole blockchain. -> /get_chain  
-Mine a block. -> /mine_block  
-Check if the chain is valid. -> /is_valid  
(to make sure it has not been tampered with and its integrity is maintained)  

**Files:**   
blockhain.py - The blockchain code  
flaskr.py - The Web App  
blockchain.postman_collection - Postman HTTP requests for testing the routes of the flask web app  
