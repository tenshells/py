import sqlite3
import csv
dbname = "C:\\codes\\cpp\\ZBolt\\tpch-dbgen\\data\\"

customer_col = "custKey name address nationKey phone acctBal mktSeg comment".split()
customer_types = "int varchar(50) varchar(50) int varchar(15) float(2) varchar(10) varchar(50)".split(' ')
orders_col = "orderKey custKey orderStatus totalPrice orderDate orderPriority clerk shipPriority comment".split()
orders_types = "int int varchar(1) float(2) varchar(12) varchar(10) varchar(15) int varchar(50)".split()
lineItems_col = "orderKey partKey suppKey lineNumber quantity exPrice discount tax returnFlag lineStatus shipDate commitDate receiptDate shipInstruct shipMode comment".split()
linetItems_types = "int int int int int float(2) float(2) float(2) varchar(1) varchar(1) varchar(12) varchar(12) varchar(12) varchar(25) varchar(10) varchar(40)".split()
supplier_col = "suppKey name address nationKey phone acctBal comment".split(' ')
supplier_types = "int varchar(25) varchar(50) int varchar(12) float(2) varchar(60)".split(' ')
nation_col = "nationKey name regionKey comment".split(' ')
nation_types = "int varchar(15) int varchar(25)".split(' ')
region_col = "regionKey name comment".split(' ')
region_types = "int varchar(10) varchar(40)".split(' ')

customer = [customer_col,customer_types,dbname+"customer.tbl","Customer"]
orders = [orders_col,orders_types,dbname+"orders.tbl","Orders"]
lineItem = [lineItems_col, linetItems_types, dbname+"lineitem.tbl","LineItem"]
supplier = [supplier_col,supplier_types,dbname+"supplier.tbl","Supplier"]
nation = [nation_col, nation_types, dbname+"nation.tbl","Nation"]
region = [region_col, region_types, dbname+"region.tbl","Region"]

ourTables = [customer,orders,lineItem,supplier,nation,region]

def createTable(column_names,column_types,tableName,cursor):
    # Create the 'AbelsTable' table
    create_table_query = f"CREATE TABLE IF NOT EXISTS {tableName} ("
    for i in range(len(column_names)):
        create_table_query += f"{column_names[i]} {column_types[i]}"
        if i < len(column_names) - 1:
            create_table_query += ","

    create_table_query += ")"
    print(f"this is create query {create_table_query}")
    cursor.execute(create_table_query)
    return

def updateTable(tableName,cursor,filename,column_types):
    entries=0
    with open(filename) as file:
        reader = csv.reader(file, delimiter='|')
            # Insert the CSV file data into the SQLite table

        for row in reader:
            qb=""
            row.pop()
            for valueIndex in range(len(row)):
                if(column_types[valueIndex][0]=='v'):
                    qb=f"{qb} '{row[valueIndex]}',"
                else:
                    qb=f'{qb} {row[valueIndex]},'
            
            # print(f"qb is rn {qb}")
            query = f"INSERT INTO {tableName} VALUES ({qb.rstrip().rstrip(',')})"
            # print("This is insert query : "+query)
            cursor.execute(query+';')
            
            entries += 1
            # if entries == 1:
            #     break
    print(f"Added {entries:,} items from {filename.split('//')[-1]}")
    return

def createAndUpdateTable(cursor,tableName,column_names,column_types, filename):
    # print(f"Adding {len(column_names)} column names with {len(column_types)} column types in {tableName}")
    createTable(column_names,column_types, tableName,cursor)
    updateTable(tableName,cursor,filename,column_types)

def parseTable(cursor,table):
    createAndUpdateTable(cursor,table[3],table[0],table[1],table[2])


def noOfEntries(cursor,tableName):
    cno=0
    for i in cursor.execute("SELECT COUNT(*) FROM "+tableName):
        cno=i
    sbuild = f"{tableName} has {cno[0]} values"
    return sbuild

conn = sqlite3.connect('local_database2.db')
cursor = conn.cursor()

for table in ourTables:
    parseTable(cursor,table)

# Commit the changes to the database
conn.commit()


q5select = "SELECT n.name,sum(l.exPrice * (1-l.discount)) as revenue "
q5from = "FROM Customer c, Orders o, LineItem l, Supplier s, Nation n, Region r "
q5where = "WHERE c.custKey=o.custKey and l.orderKey=o.orderKey and l.suppKey=s.suppKey and c.nationKey=s.nationKey and s.nationKey=n.nationKey and n.regionKey=r.regionKey and r.name='ASIA' and o.orderDate>='1994-01-01' and o.orderDate<'1995-01-01' "
q5groupBy = "GROUP BY n.name "
q5orderBy = "ORDER BY revenue desc; "

q5where2 = "WHERE c.custKey=o.custKey and l.orderKey=o.orderKey and l.suppKey=s.suppKey and c.nationKey=n.nationKey and s.nationKey=n.nationKey and n.regionKey=r.regionKey and r.name='ASIA' and o.orderDate>='1994-01-01' and o.orderDate<'1995-01-01' "

q5 = q5select+q5from+q5where+q5groupBy+q5orderBy
print(f"Query is {q5}")
qresult = cursor.execute(q5)
for result in qresult:
    print(result)

q52 = q5select+q5from+q5where2+q5groupBy+q5orderBy
print(f"Query is {q52}")
qresult2 = cursor.execute(q52)
for result in qresult2:
    print(result)

# Close the database connection
conn.close()