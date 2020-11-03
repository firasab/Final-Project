import psycopg2

#connect to the db
con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root")

#cursor
cur = con.cursor()

#cur.execute("insert into users (username,password) values (%s,%s)", ("mahdi","123") )

#execute query
cur.execute("select username ,password from users")

rows = cur.fetchall()

for r in rows:
    print (f"username {r[0]} password  {r[1]}")

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()
