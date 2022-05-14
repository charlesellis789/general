import database as db

def main():
	print(testIfDBExists())

def testIfDBExists():
	if db.DBExists('localhost','postgres','postgres','admin'):
		if not db.DBExists('localhost','postgres','postgres','testFail'):
			if not db.DBExists('localhost','postgres','testFail','admin'):
				if not db.DBExists('localhost','testFail','postgres','admin'):
					if not db.DBExists('testFail','postgres','postgres','admin'):
						return True
	return False

main()