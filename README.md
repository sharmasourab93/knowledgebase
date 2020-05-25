# Implement HTTP/REST Server for Knowledge Base Management
An assignment to implement a knowledge base management system using [Pyramid framework](https://trypyramid.com/)


### Requirements
The requirements are as given below <br/>
**Tech stack**: *Python3 + Pyramid + PostgreSQL*

#### Operations:

- Create KB item
- Get KB item by number
- Delete KB item
- Update KB item
- Find KB items by title or text
- List all KB items


*No UI, use JSON format for API.*


**Database**: PostgreSQL


*Tests are mandatory.*


*Server should de delivered as a docker container.*


*Use public github repo.*


The Knowledge Base items should  implement the following Management system

1. Takes word{text} or item{number or text} 
2. Creates a word & meaning based on request
3. Find's a word & meaning based on Word or Item
4. Updates a word's meaning based on Words 
5. Lists all the entries saved

___

## Implementation Per Requirement 

### Problem Statement

As given in the requirements, A Backend system is to be built using **Python3** and **Pyramid** Web Framework. 
The backend application must be able to implement all the operations as listed above. 
The API format is JSON. 
It's additionally good to have unittest cases, and delivery in a docker container. 


### Installation Steps 
Pass 

### Solution 
**Database used** : PostgreSQL
**SQL ORM** : SQLAlchemy


Dependent Packages: [eng_dictionary](https://github.com/sharmasourab93/eng_dictionary) to populate items in the database. 


**Unit tests** : Present


**Dockerfile** : Present

### Implementation Checklist



These are the following routes

#### Create Knowledge Base Item

    ```http://localhost:6543/create/{word}```

{word} takes the word for which the meaning has to be looked up for. 
This view adds the word and the meaning of the word into the database.

#### GET Knowledge Base Item
    ```http://localhost:6543/get/{word}```

{word} takes the word to be search for in the database. 
This view queries the word and meaning of the word in the database.

#### GET Knowledge Base Item By Number
    ```http://localhost:6543/item/{id}```
    
{id} takes the unique id auto assigned to all the entries created in the database. 
This view returns the UID, word and meaning from the database

#### Update Knowledge Base Item
    ```http://localhost:6543/update/{first}/{second}```
    
{first} is the word to be looked up for and {second} is the meaning to be updated for the word {first}.

#### Delete Knowledge Base Item

    ```http://localhost:6543/delete/{word}```

{word} takes the word in the database to be deleted. Returns the list of all items in the database.

#### List All Knowledge Base Items
    ```http://localhost:6543/```

Fetches all the entries in the database and outputs it in the response.

___