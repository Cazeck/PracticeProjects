"""
A simply version of Dictionary that pulls data from a SQL database instead of a
json file.  Come back to this and implement features
"""

import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
# Used to navigate through the table of the database
cursor = con.cursor()

word = input("Enter a word: ")

# Query requesting the data from the database
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

# Extract all information from the tuples that we receive from out Query
if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")
