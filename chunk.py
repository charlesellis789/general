import db

# Only works with serialized primary keys
def chunkSequentialPrimaryKey(sql, recordLimit, logicFunc):
	primaryKeyCount = recordLimit
	while True:
		data = db.runSelectQueryReturningTuples(sql + str(primaryKeyCount-recordLimit) + ' and ' + str(primaryKeyCount-1) + ';')
		if len(data) == 0:
			break
		primaryKeyCount += recordLimit
		logicFunc(data)
		db.runSql(sql)

# Only works when the logic modifies the data such that the same query won't return the same data
def chunkDataUpdates(sql, logicFunc):
	while True:
		data = db.runSelectQueryReturningTuples(sql)
		if len(data) == 0:
			break
		insertSQL = logicFunc(data)
		db.runSql(insertSQL,var.databaseName)