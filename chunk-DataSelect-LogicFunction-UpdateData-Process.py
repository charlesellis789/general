import database as db

# Only works with serialized primary keys
# the sql argument must end with 'where [primary key] between '
# Parameters:
# - conn = database connection
# - sql (string) = select query that ends with ' where [primary key] between '
# - recordLimit (int) = how many records per iteration
# - logicFunc (function) = function that takes data as tuples for argument and returns sql query as a string
def chunkSequentialPrimaryKey(conn,sql,recordLimit,logicFunc):
	primaryKeyCount = recordLimit
	while True:
		data = db.runSelectQuery(conn,sql + str(primaryKeyCount-recordLimit) + ' and ' + str(primaryKeyCount-1) + ';')
		if len(data) == 0:
			break
		updateSQL = logicFunc(data) # this logic function must return sql as a string to make necessary updates
		db.runSql(updateSQL)
		primaryKeyCount += recordLimit

# Only works when the logic and update modifies the data such that the same query won't return the same data
# the sql passed in should contain a record limit amount aka for postgres '...limit = 10000' or in T-SQL 'select top 10000...'
# Parameters:
# - conn = database connection
# - sql (string) = select query
# - logicFunc (function) = function that takes data as tuples for argument and returns sql query as a string
def chunkDataUpdates(conn,sql,logicFunc):
	while True:
		data = db.runSelectQuery(conn,sql)
		if len(data) == 0:
			break
		updateSQL = logicFunc(data)
		db.runSql(updateSQL,var.databaseName)