The Given requirement was:
  Tech stack: python3+pyramid
   In brief: Implement HTTP/REST server for knowledge base management.
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
   
Knowledgebase is basically an implementation of an English Dictionary. 
There is additional module being used called dictionary 
in views to fetch meaning of a word from Cambridge univ site.   

The Following KB Management system 

	1. Takes word{text} or item{number or text} 
	2. Creates a word & meaning based on request
	3. Find's a word & meaning based on Word or Item
	4. Updates a word's meaning based on Words 
	5. Lists all the entries saved
	
	Database used : PostgreSQL
	Unit tests: Present

   
 These are the following routes with their respective functionalities and pattern to test the application 
 Route 							Pattern 		 							Functionality 
 '/create' 						/create?word=<whatever word>			To Create a new word to lookup meaning
 '/one'							/one?word=<whatever word>				To Find meaning of a word based on the word/text
 '/item'						/item?item=<NUM>						To Find the word & meaning against the i {NUM}
 'update/{first}/{second}'      /update/<first_word>/<second_word>      To update a word's meaning to second_word
 '/delete'						/delete?word=<word whatever> 			To Delete a word & it's entry from DB
 '/'							/										To return all the words & respective meanings
 
 