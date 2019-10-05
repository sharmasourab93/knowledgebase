The Given requirement:
  
  Tech stack: **_python3+pyramid_**
   
   **Implement HTTP/REST server for knowledge base management**.
   
   Operations:
   - Create KB item
   - Get KB item by number
   - Delete KB item
   - Update KB item
   - Find KB items by title or text
   - List all KB items
   
   No UI, use JSON format for API.
   
   Database: PostgreSQL
   
   Tests are mandatory.
   
   Server should de delivered as a docker container.
   
   Use public github repo.


_`Knowledgebase is basically an implementation of an English Dictionary.
There is an additional module called eng_dictionary.This module enables  
one to fetch meaning of a word from Cambridge univ site using beautifulsoup parser.`_   

The Following KB Management system 

	1. Takes word{text} or item{number or text} 
	2. Creates a word & meaning based on request
	3. Find's a word & meaning based on Word or Item
	4. Updates a word's meaning based on Words 
	5. Lists all the entries saved
	
	Database used : PostgreSQL
	Unit tests: Present

   
 These are the following routes 
 
  **Create Knowledge Base Item**
  -_`http://localhost:6543/create/{word}`_
   
   {word} takes the word for which the meaning has to be looked up for.
   This view adds the word and the meaning of the word into the database. 
   
   **GET Knowledge Base Item**
   - _`http://localhost:6543/get/{word}`_
   
   {word} takes the word to be search for in the database. 
   This view queries the word and meaning of the word in the database. 
      
   **GET Knowledge Base Item By Number**
   - _`http://localhost:6543/item/{id}`_
   
   {id} takes the unique id auto assigned to all the entries created in the database.
   This view returns the UID, word and meaning from the database 
   
   **Update Knowledge Base Item**
   - _`http://localhost:6543/update/{first}/{second}`_
   
   {first} is the word to by looked up for and 
   {second} is the meaning to be updated for the word {first}. 
   
   **Delete Knowledge Base Item**
   - _`http://localhost:6543/delete/{word}`_
   
   {word} takes the word in the database to be deleted.
   
   **List All Knowledge Base Items**
   - _`http://localhost:6543/`_
   
   Fetches all the entries in the database and outputs it in the response. 
 