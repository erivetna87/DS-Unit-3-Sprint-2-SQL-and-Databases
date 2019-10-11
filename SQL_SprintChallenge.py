import sqlite3
import pandas as pd
import numpy as np
import pickle as pickle
import pprint 

pp = pprint.PrettyPrinter()
#Creeating sqlite3 file

"""Change These Global Variables as appropriate for grading"""

sql_file = '/Users/ericrivetna/Desktop/sprint_challengeSQL.sqlite3'
north_wind_sql = '/Users/ericrivetna/Desktop/northwind_small.sqlite3'

conn = sqlite3.connect(sql_file)
cur = conn.cursor()


#function to create table with PRIMARY KEY
def create_table(table_name,col_name,field_type):
    conn = sqlite3.connect(sql_file)
    cur.execute("""CREATE TABLE IF NOT EXISTS {tn} ({cn} {ft} PRIMARY KEY)"""\
        .format(tn=table_name, cn=str(col_name), ft=str(field_type)))
    conn.commit()
   
#running function to create table with PRIMARY KEY
create_table('demo','s','VARCHAR(255)')

#function to add columns to table
def alter_table(table_name,col_name,field_type):
    conn = conn = sqlite3.connect(sql_file)
    try:
        cur.execute("""ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"""\
        .format(tn=str(table_name), cn=str(col_name), ct=str(field_type)))
    except sqlite3.OperationalError:
        print('The column {} already exists'.format(col_name))
    conn.commit()
    
#Running alter_table on non-primary key columns
alter_table('demo','x','INTEGER')
alter_table('demo','y','INTEGER')

#Inserting or Replacing Values into sqlite3 DB
cur.execute("""INSERT OR REPLACE INTO demo(s,x,y)\
VALUES('g',3,9),\
('v',5,7),\
('f',8,7);""")
conn.commit()

#Running SQL Queries

cur.execute("""SELECT COUNT(s) FROM demo;""")
print("\n","Count of Rows","\n")
print(cur.fetchall())
cur.execute("""SELECT COUNT(x), COUNT(y) FROM demo where x >= 5 AND y >= 5;""")
print("\n","rows where both `x` and `y` are at least 5","\n")
print(cur.fetchall())
cur.execute("""SELECT COUNT(DISTINCT y) FROM demo;""")
print("\n","Unique Values of y","\n")
print(cur.fetchall())

conn.commit()
conn.close()

"""Northwind Challenge"""

conn_2 = sqlite3.connect(north_wind_sql)
cur2 = conn_2.cursor()

cur2.execute("""SELECT ProductName, UnitPrice
FROM product
ORDER BY UnitPrice DESC
LIMIT 10;""")

print("\n","ten most expensive items (per unit price) in the database","\n")
pp.pprint(cur2.fetchall())

cur2.execute("""SELECT COUNT(LastName) as 'employee_cnt',
(HireDate - BirthDate) as 'employee_age_at_hire',
ROUND(AVG(HireDate - BirthDate),2) as 'average_age',
CAST (SUM((HireDate - BirthDate))/COUNT(LastName) AS FLOAT) as 'chk_figure'
FROM Employee;""")

print("\n","average age of an employee at the time of their hiring","\n")
pp.pprint(cur2.fetchall())


cur2.execute("""SELECT Product.Id, 
Product.UnitPrice,
Supplier.id,
Supplier.CompanyName
FROM Product JOIN Supplier
ON Product.SupplierId = Supplier.id
ORDER BY Product.UnitPrice DESC
LIMIT 10;""")

print("\n","ten most expensive items (per unit price) in the database *and* their suppliers?","\n")
pp.pprint(cur2.fetchall())

"""Why is this returning Category 2?"""

cur2.execute("""SELECT 
CategoryId,
COUNT(DISTINCT Product.id) as 'Total Units by Category'
FROM Product;""")

print("""Why is this returning Category 2?""")
pp.pprint(cur2.fetchone())

#Part 4
"""EmployeeID """

""""Pro: High scalibility
      Con: Not strongly ACID-compliant\
    (Atomic, Consistency, Isolation, Durability)"""
    
"""Trying to bring NoSQL and ACID Compliance together"""



# SELECT DISTINCT Territory.id, 
# Territory.TerritoryDescription, 
# Employee.FirstName, 
# Employee.LastName,
# Employee.Birthdate,
# Employee.HireDate
# FROM Territory JOIN EmployeeTerritory
# ON Territory.Id = EmployeeTerritory.TerritoryId
# JOIN Employee
# ON EmployeeTerritory.EmployeeId = Employee.Id
# GROUP BY Territory.TerritoryDescription;
