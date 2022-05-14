import database as db

def main():
	print("Testing 'connectToDB' function...")
	print('Pass Test: ' + str(testConnectToDB()))
	print("\nTesting 'createDB' function...")
	print('Pass Test: ' + str(testCreateDB()))
	print("\nTesting 'dropDB' function...")
	print('Pass Test: ' + str(testDropDB()))
	print("\nTesting 'executeSql' function...")
	print('Pass Test: ' + str(testExecuteSql()))
	print("\nTesting 'runSelectQuery' function...")
	print('Pass Test: ' + str(testRunSelectQuery()))

def testConnectToDB():
	if db.connectToDB('localhost','postgres','postgres','admin'):
		if not db.connectToDB('testFail','postgres','postgres','admin'):
			if not db.connectToDB('localhost','testFail','postgres','admin'):
				if not db.connectToDB('localhost','postgres','testFail','admin'):
					if not db.connectToDB('localhost','postgres','postgres','testFail'):
						return True
	return False

def testCreateDB():
	conn = db.connectToDB('localhost','postgres','postgres','admin')
	if db.createDB(conn,'test1'):
		if not db.createDB(conn,'test1'):
			conn.close()
			if not db.createDB(conn,'test2'):
				return True
	return False

def testDropDB():
	conn = db.connectToDB('localhost','postgres','postgres','admin')
	if db.dropDB(conn,'test1'):
		if db.dropDB(conn,'DBNameDoesNotExist'):
			conn.close()
			if not db.dropDB(conn,'test1'):
				return True
	return False

def testExecuteSql():
	db.createDB(db.connectToDB('localhost','postgres','postgres','admin'),'test')
	conn = db.connectToDB('localhost','test','postgres','admin')
	sql = 'create table test (id integer); insert into test (id) values (1),(2),(3);'
	if db.executeSql(conn,sql):
		if not db.executeSql(conn,sql[:-2]):
			conn.close()
			if not db.executeSql(conn,sql):
				db.dropDB(db.connectToDB('localhost','postgres','postgres','admin'),'test')
				return True
	db.dropDB(db.connectToDB('localhost','postgres','postgres','admin'),'test')
	return False

def testRunSelectQuery():
	db.createDB(db.connectToDB('localhost','postgres','postgres','admin'),'test')
	conn = db.connectToDB('localhost','test','postgres','admin')
	db.executeSql(conn,'create table test (id integer); insert into test (id) values (1),(2),(3);')
	sql = 'select * from test;'
	if db.runSelectQuery(conn,sql):
		if not db.runSelectQuery(conn,sql[:-2]):
			conn.close()
			if not db.runSelectQuery(conn,sql):
				db.dropDB(db.connectToDB('localhost','postgres','postgres','admin'),'test')
				return True
	db.dropDB(db.connectToDB('localhost','postgres','postgres','admin'),'test')
	return False

def testCreateTempTable():
	columns = [['id','int'],['first_name','varchar(50)'],['surname','varchar(50)']]
	return db.createTempTable('Test',columns)

main()
