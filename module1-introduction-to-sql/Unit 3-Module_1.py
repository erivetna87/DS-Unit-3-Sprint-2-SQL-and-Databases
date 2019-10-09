import pandas as pd
import numpy as np
import sqlite3 as sql

df_csv = pd.read_csv('/Users/ericrivetna/Desktop/Lambda School/Lambda Data/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')

sqlite_file = '/Users/ericrivetna/Desktop/Lambda School/Lambda Data/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.sqlite3'
conn = sql.connect(sqlite_file)
cur = conn.cursor()

cur.execute("""
SELECT COUNT(*)
FROM review;""")

cur.execute("""
SELECT Nature, Shopping
FROM review
WHERE Nature >= 100 AND SHOPPING >= 100;
""")

cur.execute("""
SELECT 
AVG(Sports) as 'Average Sports',
AVG(Religious) as 'Average Religious',
AVG(Nature) as 'Average Nature',
AVG(Theatre) as 'Average Theatre',
AVG(Shopping) as 'Average Shopping',
AVG(Picnic) as 'Average Picnic'
FROM review;""") 