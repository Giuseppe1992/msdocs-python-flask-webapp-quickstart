import pyodbc

server = 'app-service-db-server-north-europe.database.windows.net'
database = 'app-service-db-north-europe'
username = 'giuseppe'
password = 'G1useppe'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Persons")
        row = cursor.fetchone()
        while row:
            print (str(row[2]))
            row = cursor.fetchone()

print(row)