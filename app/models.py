import psycopg2
con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root")
# for users
cur = con.cursor()
cur.execute("select username, password from users")
userss = cur.fetchall()
# for list of album songs
album_cur = con.cursor()
album_cur.execute("select name,source,category from album")
album_cur_list = album_cur.fetchall()
# for list of {message for admin}
message_cur = con.cursor()
message_cur.execute("select name_of_sender,subject_of_message,source_of_video from message_to_admin")
message_list = message_cur.fetchall()


"""
for r in message_list:
    print (f"username: {r[0]} &&  password: {r[1]}")
"""
#commit the transcation
con.commit()
#close the cursor
cur.close()
album_cur.close()
message_cur.close()
con.close()#close the connection



class users():
   def __init__(self,username,password):
        users.username =username
        users.password=password

   def save_user(self):
       con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root"
      )
       cur = con.cursor()
       cur.execute("insert into users (username, password) values (%s, %s)", (users.username,users.password) )
       con.commit()
       cur.close()
       con.close()

   def check_all_users(self):
       con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root"
      )
       cur = con.cursor()
       all_users=cur.fetchall()
       cur.close()
       con.close()#close the connection
       return all_users


   def check_this_user(self):
       conn = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root"
      )
       cury = conn.cursor()
       cury.execute("select username ,password from users")
       all_users=cury.fetchall()
       for p in all_users:
           if p[0]==users.username and users.username=="Admin":# for admin
               if p[1]==users.password and users.password=="Admin123":
                 cury.close()
                 conn.close()
                 return 2
           if p[0]==users.username:
               if p[1]==users.password:
                 cury.close()
                 conn.close()
                 return 1
        #no username or wrong password
       cury.close()
       conn.close()
       return -1



#               Album Class         #
class album():
   def __init__(self,name,source,category):
        album.name = name
        album.source = source
        album.category=category

   def save_album(self):
       con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root"
      )

       category=-1
       cur = con.cursor()
       if album.category=="sad":
          category=1
       if album.category=="study":
          category=2
       if album.category=="sleep":
          category=3
       if album.category=="romantic":
          category=4
       if album.category=="rap":
          category=5
       if album.category=="dance":
          category=6
       if album.category=="children":
          category=7
       if album.category=="relax":
          category=8
       cur.execute("insert into album (name,source,category) values (%s,%s,%s)", (album.name,album.source,category) )
       con.commit()
       cur.close()
       con.close()


   def check_all_album(self):
       con = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            passwor="root"
      )
       cur = con.cursor()
       all_album=cur.fetchall()
       cur.close()
       con.close()#close the connection
       return all_album




#               Message Class         #
class message():
   def __init__(self,name_of_sender,subject_of_message,source_of_video):
        message.name_of_sender = name_of_sender
        message.subject_of_message = subject_of_message
        message.source_of_video=source_of_video

   def save_message(self):
       con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root"
      )

       cur = con.cursor()
       cur.execute("insert into message_to_admin (name_of_sender,subject_of_message,source_of_video) values (%s,%s,%s)", (message.name_of_sender,message.subject_of_message,message.source_of_video) )
       con.commit()
       cur.close()
       con.close()


   def check_all_message(self):
       con = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            passwor="root"
      )
       cur = con.cursor()
       all_message=cur.fetchall()
       cur.close()
       con.close()#close the connection
       return all_message
