import csv
import sqlite3
import random
import sys
budget=float(sys.argv[1]) if sys.argv[1] else 0
remainingBudget=budget
cursor=None
sqliteConnection = sqlite3.connect(sys.argv[2]+'/sqlite.db')
# sqlite_create_table_query = f'''SELECT * FROM devto WHERE price < {remainingBudget} ORDER BY price ASC''' 
# cursor = sqliteConnection.cursor()
# cursor.execute(sqlite_create_table_query)
randomItem=[]

while True:
    if budget < 10:
        break
    sqlite_create_table_query = f'''SELECT * FROM devto WHERE price < {remainingBudget} ORDER BY price ASC''' 
    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_query)
    records = cursor.fetchall()
    # print(len(records))
    if len(records)==0:
        break
    n = random.randint(0,len(records)-1)
    popo=records[n]
    randomItem.append(popo)
    remainingBudget-=float(popo[4])
    sqliteConnection.commit()
totalPrice=0
if budget > remainingBudget:
    totalPrice=abs(budget-remainingBudget)
# print(totalPrice)
# print(len(randomItem))
# print(budget)
if cursor:
    cursor.close()
readmeMd=f"""
# TOTAL BUDGET : ${str(budget)}
"""

if budget == remainingBudget:
    readmeMd+="\nYou have insufficient budget to buy in dev.to shop please at least had budget of above or equal of $10"
else:
    readmeMd+=f"""
# REMAINING BUDGET : ${remainingBudget}

# LIST OF RANDOM ITEM YOU CAN BUY AT DEV.TO SHOP

|image|url|title|price|
|-----|---|-----|-----|
"""
    for i in randomItem:
        readmeMd+=f"|<img src='{i[1]}' width='300' height='200' />|{i[2]}|{i[3]}|${str(i[4])}|\n"
    readmeMd+=f"\n# TOTAL PRICE : ${totalPrice}"

f=open("DEVTOSHOP.md","w+")
f.write(readmeMd)
f.close()