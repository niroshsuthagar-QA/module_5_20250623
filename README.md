# Data Automation ~ Library Client

## Day 1
Task:
1. Load in the data via a jupyter notebook.
2. Explore the data, clean and visualise.
3. Output cleaned data files.

Stretch: 
Look intot the SQLALCHEMY library and try to get python to write the cleaned files to a local SQL Server. #

## Day 2:

- Create a .py file based on your work yesterday to CLEAN and OUTPUT the library datasets. 
- You must include functions like the following:
    - fileLoader
    - duplicateChecker
    - naChecker
    - dataEnrich 

### PM: Tasks

1. Make sure you have a function that calculates the difference between the time the books were on loan to when they were checked out. 
2. Check my solutions.

Stretch Tasks (speak to Nirosh first):
- Use the Argparse library to toggle the writing to SQL on and off. 
- Using APIs:
    - Find an open API and write a new pyton script that requests data from an API and prints it.
    - List of APIs: https://github.com/public-api-lists/public-api-lists

# Day 4

AM Task:

- Write a unit test for your python app (For the data enrichment where you calculate the number of days on loan).
- Put your data cleaning app as a docker image, run it and show me that it works.




References: 
- assertEqual(a, b)	a == b
- assertNotEqual(a, b)	a != b
- assertTrue(x)	bool(x) is True
- assertFalse(x)	bool(x) is False
- assertIs(a, b)	a is b
- assertIsNot(a, b)	a is not b
- assertIsNone(x)	x is None
- assertIsNotNone(x)	x is not None
- assertIn(a, b)	a in b
- assertNotIn(a, b)	a not in b
- assertIsInstance(a, b)	isinstance(a, b)
- assertNotIsInstance(a, b)	not isinstance(a, b)