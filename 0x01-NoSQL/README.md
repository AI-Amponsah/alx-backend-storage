# 0x01. NoSQL
A project introduction to NoSQL with MongoDB

- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File
- All files are  interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- The first line of all files is a comment: // my comment

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) 
  and PyMongo (version 3.10)
- All codes use the pycodestyle style (version 2.5.*)

## Files

### MongoDB Command Files
`0-list_databases`

- a script that lists all databases in MongoDB.

`1-use_or_create_database`

- a script that creates or uses the database my_db

`2-insert`

- a script that inserts a document in the collection school

`3-all`

- a script that lists all documents in the collection school

`4-match`

- a script that lists all documents with name="Holberton school" in the collection school

`5-count`

- a script that displays the number of documents in the collection school

`6-update`

- a script that adds a new attribute to a document in the collection school

`7-delete`

- a script that deletes all documents with name="Holberton school" in the collection school

`8-all.py`

- a Python function that lists all documents in a collection

`9-insert_school.py`

- a Python function that inserts a new document in a collection based on kwargs
#

### Python scripts

`10-update_topics.py`

- a Python function that changes all topics of a school document based on the name

`100-find`

-  a Python function that returns the list of school having a specific topic

`101-students.py`

- a Python function that returns all students sorted by average score

`102-log_stats.py`

- Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs

`11-schools_by_topic.py`

- a Python function that returns the list of school having a specific topic

`12-log_stats.py`

- a Python script that provides some stats about Nginx logs stored in MongoDB

## Main files
- Main functions for some python scripts
