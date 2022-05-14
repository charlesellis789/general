import psycopg2
	
# Connects to a database
# Parameters: DBName (string) = name of the database connecting to
# Returns the cursor and connection to run queries
def connectToDB(Host,DBName,UserName,Password):
	try:
		conn = psycopg2.connect(
		    host=Host,
		    database=DBName,
		    user=UserName,
		    password=Password)
		conn.autocommit = True
		return conn
	except:
		return False
#	cursor = conn.cursor()
#	return [cursor,conn]

# Creates a new database using the postgres database that already exists. Then adds all starter tables / values to the new database
# Parameters: newDBName (String) = Name of the database being created
# Returns nothing
def createDB(conn,newDBName):
	sql = '''
		CREATE DATABASE ''' + newDBName + '''
		WITH 
		OWNER = postgres
		ENCODING = 'UTF8'
		CONNECTION LIMIT = -1;'''
	try:
		cursor = conn.cursor()
		cursor.execute(sql)
		return True
	except:
		return False

def dropDB(conn,DBName):
	try:
		cursor = conn.cursor()
		cursor.execute('drop database if exists ' + DBName + ';')
		return True
	except:
		return False

# Runs sql that changes the database aka insert, delete, update queries
# Parameters:
# - sql (string) = sql to run
# - DBName (string) = Name of the database to run the sql on
# Returns nothing
def executeSql(conn,sql):
	try:
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()
		return True
	except Exception as e:
		return False

def runSelectQuery(conn,sql):
	try:
		cursor = conn.cursor()
		cursor.execute(sql)
		data = cursor.fetchall()
		return data
	except:
		return False

# Creates a temporary table for more advanced data insertion
# Parameters:
# - tempTableName (string) = desired name of the temporary table
# - columns (string) = all columns necessary in the temp table. *Note: variable type definitions can only be the ones listed below. Please add if necessary
# Returns: sql (string) = all sql necessary to create a new temp table and insert data. Does not include the data.
def createTempTable(tempTableName,columns):
	try:
		tempTableName = str(tempTableName)
		sql = """\ndrop table if exists """ + tempTableName + """;\ncreate temporary table """ + tempTableName + """ (\n"""
		sqlInsert = 'insert into ' + tempTableName + ' (\n'
		sqlCreateColumns = ''
		sqlInsertColumns = ''
		for x in columns:
			sqlCreateColumns += '\t' + str(x[0]) + ' ' + str(x[1]) + ',\n'
			sqlInsertColumns += '\t' + str(x[0]) + ',\n'
		sqlCreateColumns = sqlCreateColumns[:-2] + '\n);\n'
		sqlInsertColumns = sqlInsertColumns[:-2] + '\n)\nvalues\n'
		sql += sqlCreateColumns + sqlInsert + sqlInsertColumns
		return sql
	except:
		return False