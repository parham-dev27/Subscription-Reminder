import sqlite3


def CONNECT():
	con = sqlite3.connect("SUBSCRIPTIONREMINDERDATABASE.db")
	cur = con.cursor()
	cur.execute("""
		CREATE TABLE IF NOT EXISTS SUBSCRIPTIONREMINDERDATABASE (info TEXT)
		""")
	con.commit()
	con.close()


def ADD(info):
	con = sqlite3.connect("SUBSCRIPTIONREMINDERDATABASE.db")
	cur = con.cursor()
	cur.execute("""
		INSERT INTO SUBSCRIPTIONREMINDERDATABASE VALUES (?)
		""", (info,))
	con.commit()
	con.close()


def VIEW():
	con = sqlite3.connect("SUBSCRIPTIONREMINDERDATABASE.db")
	cur = con.cursor()
	cur.execute("""
		SELECT * FROM SUBSCRIPTIONREMINDERDATABASE
		""")
	row = cur.fetchall()
	con.close()
	return row


def DELETE_ALL():
	con = sqlite3.connect("SUBSCRIPTIONREMINDERDATABASE.db")
	cur = con.cursor()
	cur.execute("""
		DELETE FROM SUBSCRIPTIONREMINDERDATABASE
		""")
	con.commit()
	con.close()


def DELETE(info):
	con = sqlite3.connect("SUBSCRIPTIONREMINDERDATABASE.db")
	cur = con.cursor()
	cur.execute("""
		DELETE FROM SUBSCRIPTIONREMINDERDATABASE WHERE info=?
		""", (info,))
	con.commit()
	con.close()


CONNECT()
