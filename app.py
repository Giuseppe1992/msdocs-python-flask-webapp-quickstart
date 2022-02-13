import pyodbc
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
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
         return render_template('hello.html', name = str(row[2]))

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()