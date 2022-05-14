import psycopg2

# Checks if a database exists. If not, it calls a function to create the database
# Parameters: DBName (string) = Name of the database to check
# Returns nothing
def DBExists(Host,DBName,UserName,Password):
	try: # Attempts to connect to the database
		conn = psycopg2.connect(
			host=Host,
			database=DBName,
			user=UserName,
			password=Password)
		conn.close()
		#return(True)
		return True
	except Exception as e: # If database connection fails, error is caught, user is notified.
		#return (False,e)
		return False

def dropDB(Host,DBName,UserName,Password):
	conn = psycopg2.connect(
			host=Host,
			database=DBName,
			user=UserName,
			password=Password)
	conn.autocommit = True
	cursor = conn.cursor()
	try:
		cursor.execute('drop database if exists ' + DBName + ';')
		return True
	except:
		return False

# Creates a new database using the postgres database that already exists. Then adds all starter tables / values to the new database
# Parameters: newDBName (String) = Name of the database being created
# Returns nothing
def createDB(conn,newDBName):
#	conn = psycopg2.connect(
#			host="localhost",
#			database="postgres",
#			user="postgres",
#			password=var.databasePassword)
	conn.autocommit = True
	cursor = conn.cursor()
	sql = '''
		CREATE DATABASE ''' + newDBName + '''
		WITH 
		OWNER = postgres
		ENCODING = 'UTF8'
		CONNECTION LIMIT = -1;'''
	try:
		cursor.execute(sql)
		conn.close()
		return True
	except:
		return False
	
# Connects to a database
# Parameters: DBName (string) = name of the database connecting to
# Returns the cursor and connection to run queries
def connectToDB(DBName):
	conn = psycopg2.connect(
	    host="localhost",
	    database=DBName,
	    user="postgres",
	    password=var.databasePassword)
	cursor = conn.cursor()
	return [cursor,conn]

# Closes database connection
# Parameters:
# - cursor (cursor object)
# - conn (connection details)
# returns nothing
def closeDBConnection(cursor,conn):
	cursor.close()
	conn.close()

# Runs sql that changes the database aka insert, delete, update queries
# Parameters:
# - sql (string) = sql to run
# - DBName (string) = Name of the database to run the sql on
# Returns nothing
def runSql(sql,DBName):
	[cursor,conn] = connectToDB(DBName)
	cursor.execute(sql)
	conn.commit()
	closeDBConnection(cursor,conn)

def runSqlAutocommit(sql,DBName):
	conn = psycopg2.connect(
	    host="localhost",
	    database=DBName,
	    user="postgres",
	    password=var.databasePassword)
	conn.autocommit = True
	cursor = conn.cursor()
	cursor.execute(sql)
	closeDBConnection(cursor,conn)

def runSelectQuery(sql):
	[cursor,conn] = connectToDB(var.databaseName)
	cursor.execute(sql)
	data = cursor.fetchall()
	closeDBConnection(cursor,conn)
	return data

# Creates a temporary table for more advanced data insertion
# Parameters:
# - tempTableName (string) = desired name of the temporary table
# - columns (string) = all columns necessary in the temp table. *Note: variable type definitions can only be the ones listed below. Please add if necessary
# Returns: sql (string) = all sql necessary to create a new temp table and insert data. Does not include the data.
def createTempTable(tempTableName,columns):
	sql = """\ndrop table if exists """ + tempTableName + """;\n
	create temporary table """ + tempTableName + """ (
	""" + columns + """
	);
	insert into """ + tempTableName + """ (
	""" + columns.replace(' decimal','').replace(' varchar(50)','').replace(' date','').replace(' int','').replace(' boolean','') + """ 
	) values
	"""
	return sql